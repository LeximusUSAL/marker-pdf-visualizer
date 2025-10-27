#!/usr/bin/env python3
"""
Generador de visualización HTML para Marker - Versión 3
Usa tabla de contenidos del JSON para dividir el Markdown correctamente por páginas.
"""

import json
import re
from pathlib import Path
import fitz  # PyMuPDF
from typing import Dict, List
from collections import defaultdict

def extract_pdf_pages_as_images(pdf_path: str, output_dir: Path) -> List[str]:
    """Extrae cada página del PDF como imagen."""
    pdf_images = []
    doc = fitz.open(pdf_path)

    for page_num in range(len(doc)):
        page = doc[page_num]
        mat = fitz.Matrix(2.0, 2.0)
        pix = page.get_pixmap(matrix=mat)

        img_path = output_dir / f"page_{page_num}.png"
        pix.save(str(img_path))
        pdf_images.append(f"pdf_pages/page_{page_num}.png")

        if (page_num + 1) % 5 == 0:
            print(f"Renderizadas {page_num + 1} páginas...")

    doc.close()
    print(f"✓ {len(pdf_images)} páginas renderizadas")
    return pdf_images

def parse_markdown_by_toc(md_path: Path, metadata: dict, total_pages: int) -> Dict[int, str]:
    """Usa la tabla de contenidos del JSON para dividir el Markdown por páginas."""

    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extraer tabla de contenidos
    toc = metadata.get('table_of_contents', [])

    # Crear mapa: page_id -> lista de títulos que aparecen en esa página
    page_titles = defaultdict(list)
    for entry in toc:
        page_id = entry.get('page_id')
        title = entry.get('title', '').strip()
        if page_id is not None and title:
            page_titles[page_id].append(title)

    # También buscar todas las referencias _page_N_ para ayudar
    page_markers = {}
    for match in re.finditer(r'_page_(\d+)_', content):
        page_num = int(match.group(1))
        if page_num not in page_markers:
            page_markers[page_num] = match.start()

    print(f"Títulos encontrados en TOC: {len(toc)}")
    print(f"Páginas con marcadores de imagen: {sorted(page_markers.keys())}")

    # Dividir contenido por títulos principales
    lines = content.split('\n')
    pages_content = defaultdict(list)
    current_page = 0

    for i, line in enumerate(lines):
        # Detectar cambio de página por referencia de imagen
        page_ref = re.search(r'_page_(\d+)_', line)
        if page_ref:
            new_page = int(page_ref.group(1))
            if new_page != current_page:
                current_page = new_page

        # Detectar cambio de página por título en TOC
        line_clean = line.strip()
        for page_id, titles in page_titles.items():
            for title in titles:
                # Buscar coincidencia de título (puede estar en encabezado markdown)
                title_pattern = re.escape(title)
                if re.search(title_pattern, line_clean, re.IGNORECASE):
                    if page_id != current_page:
                        current_page = page_id
                        break

        pages_content[current_page].append(line)

    # Convertir a texto
    result = {}
    for page_num in range(total_pages):
        if page_num in pages_content:
            result[page_num] = '\n'.join(pages_content[page_num])
        else:
            result[page_num] = f"[Página {page_num + 1}]\n\n(Sin contenido de texto extraído por Marker)"

    print(f"✓ Texto distribuido en {len([p for p in result.values() if 'Sin contenido' not in p])} páginas")
    return result

def collect_page_images(conversion_dir: Path) -> Dict[int, List[str]]:
    """Recolecta imágenes extraídas por Marker organizadas por página."""
    page_images = {}

    for img_file in sorted(conversion_dir.glob('_page_*')):
        if img_file.is_file() and img_file.suffix.lower() in ['.jpg', '.jpeg', '.png']:
            match = re.search(r'_page_(\d+)_', img_file.name)
            if match:
                page_num = int(match.group(1))
                if page_num not in page_images:
                    page_images[page_num] = []
                page_images[page_num].append(f"{conversion_dir.name}/{img_file.name}")

    print(f"✓ {sum(len(imgs) for imgs in page_images.values())} imágenes encontradas")
    return page_images

def generate_html(pdf_path: str, conversion_dir: str, output_html: str):
    """Genera el HTML interactivo."""

    pdf_path_obj = Path(pdf_path)
    conversion_dir_obj = Path(conversion_dir)

    # Crear directorio para imágenes del PDF
    pdf_pages_dir = conversion_dir_obj.parent / 'pdf_pages'
    pdf_pages_dir.mkdir(exist_ok=True)

    print("\n📄 Extrayendo páginas del PDF original...")
    pdf_images = extract_pdf_pages_as_images(pdf_path, pdf_pages_dir)

    # Cargar metadatos
    print("\n📋 Cargando metadatos de Marker...")
    meta_file = conversion_dir_obj / f"{pdf_path_obj.stem}_meta.json"
    with open(meta_file, 'r', encoding='utf-8') as f:
        metadata = json.load(f)

    total_pages = len(pdf_images)

    print("\n📝 Procesando texto extraído por Marker...")
    md_file = conversion_dir_obj / f"{pdf_path_obj.stem}.md"
    pages_text = parse_markdown_by_toc(md_file, metadata, total_pages)

    print("\n🖼️  Recolectando imágenes extraídas...")
    page_images = collect_page_images(conversion_dir_obj)

    # Generar datos de páginas
    pages_data = {}
    for i in range(total_pages):
        pages_data[str(i)] = {
            'pdf_img': pdf_images[i],
            'text': pages_text.get(i, 'Sin contenido'),
            'images': page_images.get(i, [])
        }

    # Generar HTML (mismo template que antes)
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Visualizador Marker - {pdf_path_obj.name}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}

        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #1a1a1a;
            color: #e0e0e0;
        }}

        .header {{
            background: #2d2d2d;
            padding: 20px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.3);
            position: sticky;
            top: 0;
            z-index: 1000;
        }}

        .header h1 {{
            color: #4CAF50;
            font-size: 24px;
            margin-bottom: 10px;
        }}

        .subtitle {{
            color: #aaa;
            font-size: 14px;
            margin-bottom: 15px;
        }}

        .navigation {{
            display: flex;
            align-items: center;
            gap: 15px;
            flex-wrap: wrap;
        }}

        .nav-btn {{
            background: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 14px;
            transition: background 0.3s;
            font-weight: 500;
        }}

        .nav-btn:hover:not(:disabled) {{
            background: #45a049;
        }}

        .nav-btn:disabled {{
            background: #555;
            cursor: not-allowed;
            opacity: 0.5;
        }}

        .page-selector {{
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        .page-selector input {{
            width: 70px;
            padding: 8px;
            border: 1px solid #555;
            border-radius: 5px;
            background: #333;
            color: #e0e0e0;
            text-align: center;
            font-size: 14px;
        }}

        .page-info {{
            color: #aaa;
            font-size: 14px;
        }}

        .view-toggle {{
            display: flex;
            gap: 10px;
        }}

        .toggle-btn {{
            background: #555;
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 5px;
            cursor: pointer;
            transition: background 0.3s;
            font-size: 13px;
        }}

        .toggle-btn.active {{
            background: #4CAF50;
        }}

        .container {{
            max-width: 1800px;
            margin: 0 auto;
            padding: 20px;
        }}

        .stats {{
            background: #2d2d2d;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 15px;
        }}

        .stat-item {{
            text-align: center;
            padding: 15px;
            background: #1a1a1a;
            border-radius: 5px;
            border: 1px solid #444;
        }}

        .stat-value {{
            font-size: 28px;
            color: #4CAF50;
            font-weight: bold;
            margin-bottom: 5px;
        }}

        .stat-label {{
            color: #aaa;
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}

        .comparison-view {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
        }}

        .panel {{
            background: #2d2d2d;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        }}

        .panel h2 {{
            color: #4CAF50;
            margin-bottom: 15px;
            font-size: 18px;
            border-bottom: 2px solid #4CAF50;
            padding-bottom: 10px;
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        .pdf-viewer {{
            background: white;
            padding: 20px;
            border-radius: 5px;
            text-align: center;
            min-height: 400px;
            display: flex;
            align-items: center;
            justify-content: center;
        }}

        .pdf-viewer img {{
            max-width: 100%;
            height: auto;
            box-shadow: 0 2px 8px rgba(0,0,0,0.2);
        }}

        .markdown-content {{
            background: #1a1a1a;
            padding: 20px;
            border-radius: 5px;
            max-height: 800px;
            overflow-y: auto;
            line-height: 1.8;
            border: 1px solid #444;
            min-height: 400px;
        }}

        .markdown-content h1 {{
            color: #4CAF50;
            margin-top: 20px;
            margin-bottom: 10px;
            font-size: 24px;
        }}

        .markdown-content h2 {{
            color: #66BB6A;
            margin-top: 15px;
            margin-bottom: 8px;
            font-size: 20px;
        }}

        .markdown-content h3 {{
            color: #81C784;
            margin-top: 12px;
            margin-bottom: 6px;
            font-size: 18px;
        }}

        .markdown-content h4 {{
            color: #A5D6A7;
            margin-top: 10px;
            margin-bottom: 5px;
            font-size: 16px;
        }}

        .markdown-content p {{
            margin-bottom: 10px;
        }}

        .markdown-content img {{
            max-width: 100%;
            height: auto;
            margin: 10px 0;
            border-radius: 5px;
        }}

        .extracted-images {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 15px;
            margin-top: 15px;
            min-height: 100px;
        }}

        .extracted-images img {{
            width: 100%;
            height: auto;
            border-radius: 5px;
            border: 2px solid #444;
            transition: transform 0.3s, border-color 0.3s;
            cursor: pointer;
        }}

        .extracted-images img:hover {{
            transform: scale(1.05);
            border-color: #4CAF50;
        }}

        .no-images {{
            color: #666;
            text-align: center;
            padding: 40px;
            font-style: italic;
            grid-column: 1 / -1;
        }}

        .lightbox {{
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.95);
            z-index: 2000;
            justify-content: center;
            align-items: center;
        }}

        .lightbox.active {{
            display: flex;
        }}

        .lightbox img {{
            max-width: 90%;
            max-height: 90%;
            box-shadow: 0 0 30px rgba(76, 175, 80, 0.5);
        }}

        .lightbox-close {{
            position: absolute;
            top: 20px;
            right: 40px;
            font-size: 50px;
            color: #4CAF50;
            cursor: pointer;
            transition: transform 0.3s;
        }}

        .lightbox-close:hover {{
            transform: scale(1.2);
        }}

        ::-webkit-scrollbar {{
            width: 10px;
        }}

        ::-webkit-scrollbar-track {{
            background: #1a1a1a;
        }}

        ::-webkit-scrollbar-thumb {{
            background: #4CAF50;
            border-radius: 5px;
        }}

        ::-webkit-scrollbar-thumb:hover {{
            background: #45a049;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>📄 Visualizador Marker - {pdf_path_obj.name}</h1>
        <p class="subtitle">Revisión de conversión: PDF Original vs Texto extraído por Marker</p>

        <div class="navigation">
            <button class="nav-btn" id="prevBtn" onclick="changePage(-1)">← Anterior</button>
            <button class="nav-btn" id="nextBtn" onclick="changePage(1)">Siguiente →</button>

            <div class="page-selector">
                <span class="page-info">Página:</span>
                <input type="number" id="pageInput" min="1" max="{total_pages}" value="1" onchange="goToPage()">
                <span class="page-info">de {total_pages}</span>
            </div>

            <div class="view-toggle">
                <button class="toggle-btn active" id="compareBtn" onclick="setView('compare')">🔄 Comparar</button>
                <button class="toggle-btn" id="textBtn" onclick="setView('text')">📝 Solo texto</button>
            </div>
        </div>
    </div>

    <div class="container">
        <div class="stats">
            <div class="stat-item">
                <div class="stat-value">{total_pages}</div>
                <div class="stat-label">Total páginas</div>
            </div>
            <div class="stat-item">
                <div class="stat-value">{len([p for p in page_images if page_images[p]])}</div>
                <div class="stat-label">Páginas con imágenes</div>
            </div>
            <div class="stat-item">
                <div class="stat-value">{sum(len(imgs) for imgs in page_images.values())}</div>
                <div class="stat-label">Imágenes extraídas</div>
            </div>
            <div class="stat-item">
                <div class="stat-value">{metadata.get('page_stats', [dict()])[0].get('text_extraction_method', 'N/A').upper() if metadata.get('page_stats') else 'N/A'}</div>
                <div class="stat-label">Método OCR</div>
            </div>
        </div>

        <div id="compareView" class="comparison-view">
            <div class="panel">
                <h2>📑 PDF Original</h2>
                <div class="pdf-viewer" id="pdfViewer">
                    <div style="color: #4CAF50;">Cargando...</div>
                </div>
            </div>

            <div class="panel">
                <h2>📝 Texto Extraído por Marker</h2>
                <div class="markdown-content" id="markdownViewer">
                    <div style="color: #4CAF50;">Cargando...</div>
                </div>
            </div>
        </div>

        <div class="panel" style="margin-top: 20px;">
            <h2>🖼️ Imágenes Extraídas por Marker</h2>
            <div class="extracted-images" id="extractedImages">
                <div style="color: #4CAF50;">Cargando...</div>
            </div>
        </div>
    </div>

    <div class="lightbox" id="lightbox" onclick="closeLightbox(event)">
        <span class="lightbox-close">&times;</span>
        <img id="lightboxImg" src="" alt="Imagen ampliada">
    </div>

    <script>
        const pagesData = {json.dumps(pages_data, indent=2, ensure_ascii=False)};
        const totalPages = {total_pages};

        let currentPage = 0;
        let currentView = 'compare';

        function updatePage() {{
            const pageData = pagesData[currentPage.toString()];
            if (!pageData) return;

            // Actualizar PDF viewer
            document.getElementById('pdfViewer').innerHTML =
                `<img src="${{pageData.pdf_img}}" alt="Página ${{currentPage + 1}}">`;

            // Actualizar Markdown viewer con mejor formato
            const text = pageData.text || 'Sin contenido';
            const markdownHtml = text
                .replace(/&/g, '&amp;')
                .replace(/</g, '&lt;')
                .replace(/>/g, '&gt;')
                .replace(/^#### (.*$)/gm, '<h4>$1</h4>')
                .replace(/^### (.*$)/gm, '<h3>$1</h3>')
                .replace(/^## (.*$)/gm, '<h2>$1</h2>')
                .replace(/^# (.*$)/gm, '<h1>$1</h1>')
                .replace(/!\\[([^\\]]*)\\]\\(([^)]+)\\)/g, '<div style="margin: 10px 0;"><em style="color: #666;">Imagen: $1</em></div>')
                .replace(/\\n\\n/g, '</p><p>')
                .replace(/\\n/g, '<br>');

            document.getElementById('markdownViewer').innerHTML = '<p>' + markdownHtml + '</p>';

            // Actualizar imágenes extraídas
            const imagesContainer = document.getElementById('extractedImages');
            if (pageData.images && pageData.images.length > 0) {{
                imagesContainer.innerHTML = pageData.images.map((img, idx) =>
                    `<img src="${{img}}" alt="Imagen ${{idx + 1}}" onclick="openLightbox('${{img}}')">`
                ).join('');
            }} else {{
                imagesContainer.innerHTML = '<div class="no-images">No se extrajeron imágenes de esta página</div>';
            }}

            // Actualizar controles
            document.getElementById('pageInput').value = currentPage + 1;
            document.getElementById('prevBtn').disabled = currentPage === 0;
            document.getElementById('nextBtn').disabled = currentPage === totalPages - 1;

            // Scroll al top
            window.scrollTo({{ top: 0, behavior: 'smooth' }});
        }}

        function changePage(delta) {{
            const newPage = currentPage + delta;
            if (newPage >= 0 && newPage < totalPages) {{
                currentPage = newPage;
                updatePage();
            }}
        }}

        function goToPage() {{
            const input = document.getElementById('pageInput');
            const page = parseInt(input.value) - 1;
            if (page >= 0 && page < totalPages) {{
                currentPage = page;
                updatePage();
            }} else {{
                input.value = currentPage + 1;
            }}
        }}

        function setView(view) {{
            currentView = view;
            document.getElementById('compareBtn').classList.toggle('active', view === 'compare');
            document.getElementById('textBtn').classList.toggle('active', view === 'text');

            const compareView = document.getElementById('compareView');
            const pdfPanel = compareView.querySelector('.pdf-viewer').parentElement;

            if (view === 'text') {{
                compareView.style.gridTemplateColumns = '1fr';
                pdfPanel.style.display = 'none';
            }} else {{
                compareView.style.gridTemplateColumns = '1fr 1fr';
                pdfPanel.style.display = 'block';
            }}
        }}

        function openLightbox(imgSrc) {{
            document.getElementById('lightboxImg').src = imgSrc;
            document.getElementById('lightbox').classList.add('active');
        }}

        function closeLightbox(e) {{
            if (e.target.id === 'lightbox' || e.target.classList.contains('lightbox-close')) {{
                document.getElementById('lightbox').classList.remove('active');
            }}
        }}

        // Atajos de teclado
        document.addEventListener('keydown', (e) => {{
            if (e.key === 'ArrowLeft') changePage(-1);
            if (e.key === 'ArrowRight') changePage(1);
            if (e.key === 'Escape') closeLightbox({{ target: document.getElementById('lightbox') }});
        }});

        // Inicializar
        window.addEventListener('load', () => {{
            updatePage();
            console.log('✅ Visualizador cargado');
            console.log(`📊 Total de páginas: ${{totalPages}}`);
        }});
    </script>
</body>
</html>
"""

    # Guardar HTML
    output_path = Path(output_html)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"\n✅ Visualización generada: {output_path}")
    print(f"   Tamaño HTML: {output_path.stat().st_size / 1024:.1f} KB")
    print(f"\n📂 Estructura:")
    print(f"   • HTML: {output_path}")
    print(f"   • Imágenes PDF: {pdf_pages_dir}/")
    print(f"   • Imágenes Marker: {conversion_dir_obj}/")

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print("Uso: python visualizador_marker_v3.py <pdf_path> <conversion_dir> [output_html]")
        sys.exit(1)

    pdf_path = sys.argv[1]
    conversion_dir = sys.argv[2]
    output_html = sys.argv[3] if len(sys.argv) > 3 else 'visualizacion_marker.html'

    generate_html(pdf_path, conversion_dir, output_html)
