# Tutorial: Visualizador HTML para Revisión de Conversiones Marker

## 📋 Índice

1. [¿Qué hace esta herramienta?](#qué-hace-esta-herramienta)
2. [Requisitos previos](#requisitos-previos)
3. [Instalación de dependencias](#instalación-de-dependencias)
4. [Uso básico](#uso-básico)
5. [Ejemplos de uso](#ejemplos-de-uso)
6. [Interpretación de resultados](#interpretación-de-resultados)
7. [Solución de problemas](#solución-de-problemas)

---

## ¿Qué hace esta herramienta?

El **Generador de Visualización Marker** crea una interfaz HTML interactiva que permite revisar la calidad de las conversiones realizadas por [Marker](https://github.com/VikParuchuri/marker), comparando:

- **PDF Original** (renderizado como imagen)
- **Texto extraído** por Marker (OCR con IA)
- **Imágenes extraídas** del documento

### Casos de uso

✅ **Control de calidad** de digitalizaciones
✅ **Revisión manual** de transcripciones OCR
✅ **Detección de errores** en la extracción de texto
✅ **Validación** de procesamiento por lotes
✅ **Documentación** del proceso de conversión

---

## Requisitos previos

### 1. Software necesario

- **Python 3.8 o superior**
- **Marker** instalado y funcionando
- **PDFs convertidos** con Marker

### 2. Estructura de archivos esperada

Después de ejecutar Marker sobre un PDF, deberías tener:

```
marker-conversions/
├── documento.pdf                    ← PDF original
└── documento/                       ← Directorio de salida de Marker
    ├── documento.md                 ← Texto extraído (Markdown)
    ├── documento_meta.json          ← Metadatos de la conversión
    ├── _page_0_Picture_1.jpeg       ← Imágenes extraídas
    ├── _page_1_Picture_2.jpeg
    └── ...
```

---

## Instalación de dependencias

### Instalar PyMuPDF (fitz)

```bash
pip install PyMuPDF
```

Este es el único paquete adicional necesario (aparte de las librerías estándar de Python).

### Verificar instalación

```bash
python3 -c "import fitz; print('PyMuPDF instalado correctamente')"
```

---

## Uso básico

### Sintaxis del comando

```bash
python3 generador_visualizacion_marker.py <pdf_original> <directorio_marker> [archivo_html_salida]
```

### Parámetros

| Parámetro | Descripción | Obligatorio |
|-----------|-------------|-------------|
| `<pdf_original>` | Ruta al PDF original que fue convertido | ✅ Sí |
| `<directorio_marker>` | Directorio con los archivos de salida de Marker | ✅ Sí |
| `[archivo_html_salida]` | Nombre del archivo HTML a generar | ❌ No (por defecto: `visualizacion_marker.html`) |

### Ejemplo mínimo

```bash
python3 generador_visualizacion_marker.py \
  documento.pdf \
  documento
```

Esto generará `visualizacion_marker.html` en el directorio actual.

---

## Ejemplos de uso

### Ejemplo 1: Conversión simple

```bash
# Convertir con Marker
marker documento.pdf --output_dir ./conversiones

# Generar visualización
python3 generador_visualizacion_marker.py \
  documento.pdf \
  conversiones/documento \
  revision_documento.html

# Abrir en navegador
open revision_documento.html
```

### Ejemplo 2: Procesamiento por lotes

```bash
#!/bin/bash
# Script para procesar múltiples PDFs

for pdf in *.pdf; do
    nombre="${pdf%.pdf}"

    echo "Procesando: $nombre"

    # Convertir con Marker (si aún no está convertido)
    if [ ! -d "$nombre" ]; then
        marker "$pdf" --output_dir .
    fi

    # Generar visualización
    python3 generador_visualizacion_marker.py \
      "$pdf" \
      "$nombre" \
      "visualizacion_${nombre}.html"

    echo "✓ Generado: visualizacion_${nombre}.html"
done

echo "¡Todas las visualizaciones generadas!"
```

### Ejemplo 3: Revistas musicales históricas

```bash
# Procesar revista musical de 1930
python3 generador_visualizacion_marker.py \
  /Users/maria/Documents/revistas/ritmo_1930_enero.pdf \
  /Users/maria/Documents/marker-conversions/ritmo_1930_enero \
  revision_ritmo_enero_1930.html
```

---

## Interpretación de resultados

### Estadísticas mostradas

Al ejecutar el script, verás un resumen:

```
📄 Extrayendo páginas del PDF original...
Renderizadas 5 páginas...
Renderizadas 10 páginas...
✓ 20 páginas renderizadas

📋 Cargando metadatos de Marker...

📝 Procesando texto extraído por Marker...
Títulos encontrados en TOC: 69
Páginas con marcadores de imagen: [0, 1, 4, 6, 7, 9, 10, 11, 18, 19]
✓ Texto distribuido en 20 páginas

🖼️  Recolectando imágenes extraídas...
✓ 19 imágenes encontradas

✅ Visualización generada: visualizacion_1000203211.html
   Tamaño HTML: 111.6 KB

📂 Estructura:
   • HTML: visualizacion_1000203211.html
   • Imágenes PDF: pdf_pages/
   • Imágenes Marker: 1000203211/
```

### Archivos generados

| Archivo/Directorio | Descripción |
|-------------------|-------------|
| `visualizacion_*.html` | Interfaz web interactiva |
| `pdf_pages/` | Renders de cada página del PDF original (PNG) |
| `documento/` | Directorio original de Marker (no se modifica) |

### Interfaz HTML

La visualización HTML incluye:

1. **Estadísticas en la parte superior:**
   - Total de páginas
   - Páginas con imágenes extraídas
   - Total de imágenes extraídas
   - Método OCR utilizado (SURYA, Tesseract, etc.)

2. **Navegación:**
   - Botones "Anterior" / "Siguiente"
   - Selector directo de página
   - Atajos de teclado: `←` `→` para navegar, `ESC` para cerrar zoom

3. **Vista comparativa:**
   - Panel izquierdo: PDF original renderizado
   - Panel derecho: Texto extraído por Marker en formato Markdown

4. **Galería de imágenes:**
   - Miniatura de todas las imágenes extraídas de la página actual
   - Click para ver en tamaño completo (lightbox)

5. **Opciones de visualización:**
   - "🔄 Comparar": Vista lado a lado (por defecto)
   - "📝 Solo texto": Vista únicamente del texto extraído

---

## Solución de problemas

### Error: `ModuleNotFoundError: No module named 'fitz'`

**Causa:** PyMuPDF no está instalado

**Solución:**
```bash
pip install PyMuPDF
# o
pip3 install PyMuPDF
```

### Error: `FileNotFoundError: [Errno 2] No such file or directory`

**Causa:** Ruta incorrecta al PDF o directorio de Marker

**Solución:** Verifica las rutas:
```bash
ls documento.pdf              # Debe existir
ls documento/documento.md     # Debe existir
ls documento/documento_meta.json  # Debe existir
```

### Las imágenes del PDF no se ven en el HTML

**Causa:** Las rutas relativas son incorrectas

**Solución:**
- Abre el HTML desde el **mismo directorio** donde ejecutaste el script
- O usa rutas absolutas al ejecutar:
  ```bash
  python3 /ruta/completa/generador_visualizacion_marker.py \
    $(pwd)/documento.pdf \
    $(pwd)/documento \
    $(pwd)/visualizacion.html
  ```

### El texto no corresponde a las páginas correctas

**Causa:** Marker no tiene suficientes marcadores de página en el Markdown

**Solución:** Este script usa la **tabla de contenidos** del JSON de Marker para mapear el texto. Si el problema persiste:
1. Verifica que `documento_meta.json` contenga `table_of_contents`
2. Revisa manualmente el archivo `documento.md`
3. Reporta el problema en el repositorio de Marker si es un bug de la conversión

### El HTML pesa demasiado

**Causa:** Muchas páginas o imágenes de alta resolución

**Solución:** Este script usa referencias a archivos locales (no embebe imágenes), así que el HTML siempre será ligero (~100KB). Si necesitas compartir la visualización:
```bash
# Comprimir todo
zip -r revision_completa.zip visualizacion.html pdf_pages/ documento/
```

### Error: `json.decoder.JSONDecodeError`

**Causa:** El archivo `_meta.json` está corrupto

**Solución:**
1. Re-ejecuta la conversión con Marker
2. Verifica que la conversión se completó correctamente
3. Revisa el contenido del JSON:
   ```bash
   cat documento/documento_meta.json | python3 -m json.tool
   ```

---

## Consejos y buenas prácticas

### 1. Organización de archivos

Mantén una estructura clara:

```
proyecto/
├── originales/           ← PDFs originales
│   ├── doc1.pdf
│   └── doc2.pdf
├── conversiones/         ← Salidas de Marker
│   ├── doc1/
│   └── doc2/
└── revisiones/          ← Visualizaciones HTML
    ├── doc1.html
    └── doc2.html
```

### 2. Procesamiento por lotes eficiente

```bash
# Crear directorios
mkdir -p conversiones revisiones

# Procesar todos los PDFs
for pdf in originales/*.pdf; do
    nombre=$(basename "$pdf" .pdf)

    # Marker
    marker "$pdf" --output_dir conversiones

    # Visualización
    python3 generador_visualizacion_marker.py \
      "$pdf" \
      "conversiones/$nombre" \
      "revisiones/${nombre}.html"
done
```

### 3. Control de calidad

Para revisar sistemáticamente:

1. Abre la visualización HTML
2. Navega página por página con las flechas del teclado
3. Verifica:
   - ✅ El texto corresponde a la página mostrada
   - ✅ No hay errores graves de OCR
   - ✅ Las imágenes se extrajeron correctamente
   - ✅ El formato markdown es correcto
4. Anota problemas detectados para re-procesamiento

### 4. Compartir resultados

Para enviar revisiones a colaboradores:

```bash
# Comprimir visualización completa
zip -r revision_completa.zip \
  visualizacion.html \
  pdf_pages/ \
  documento/

# O subir a servidor web
scp -r visualizacion.html pdf_pages/ documento/ \
  usuario@servidor:/var/www/revisiones/
```

---

## Información técnica

### Tecnologías utilizadas

- **Python 3**: Lenguaje de scripting
- **PyMuPDF (fitz)**: Renderizado de páginas PDF a imágenes
- **HTML5 + CSS3**: Interfaz web
- **JavaScript ES6**: Interactividad
- **JSON**: Metadatos de Marker

### Características del HTML generado

- ✅ **Standalone**: Una sola página, sin frameworks
- ✅ **Responsive**: Se adapta a diferentes tamaños de pantalla
- ✅ **Ligero**: ~100KB típicamente
- ✅ **Offline**: Funciona sin conexión a internet
- ✅ **Accesible**: Atajos de teclado y navegación clara

### Compatibilidad de navegadores

- ✅ Chrome/Chromium (recomendado)
- ✅ Firefox
- ✅ Safari
- ✅ Edge
- ❌ Internet Explorer (no soportado)

---

## Preguntas frecuentes

**P: ¿Puedo modificar el diseño del HTML?**
R: Sí, el HTML generado incluye todo el CSS embebido. Puedes editarlo manualmente o modificar el template en el script Python.

**P: ¿Funciona con PDFs de cualquier idioma?**
R: Sí, mientras Marker soporte el idioma. El visualizador es agnóstico al idioma.

**P: ¿Puedo usar esto para documentos confidenciales?**
R: Sí, todo el procesamiento es local. No se envía nada a internet.

**P: ¿Cuánto espacio ocupan las visualizaciones?**
R: Depende del número de páginas. Aproximadamente:
- HTML: ~100KB
- Cada página renderizada: 10-20MB (PNG de alta calidad)
- Total para 20 páginas: ~300-400MB

**P: ¿Puedo eliminar los archivos `pdf_pages/` después?**
R: Sí, pero entonces la visualización no mostrará el PDF original. Si solo necesitas el texto, conserva solo el HTML y el directorio de Marker.

---

## Contacto y contribuciones

Este script fue desarrollado para el proyecto **LexiMus: Léxico y ontología de la música en español**.

Para reportar problemas o sugerir mejoras, contacta con el equipo del proyecto.

---

## Licencia

Este script es de uso libre para proyectos académicos y de investigación.

---

**Última actualización:** 27 de octubre de 2025
**Versión del script:** 3.0
