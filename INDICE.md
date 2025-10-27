# Índice de Recursos - Conversión y Visualización con Marker

Este directorio contiene herramientas para convertir PDFs a Markdown con Marker y generar visualizaciones HTML para revisión de calidad.

---

## 📚 Documentación

| Archivo | Descripción |
|---------|-------------|
| **[INDICE.md](./INDICE.md)** | Este archivo - Índice general |
| **[README_VISUALIZADOR.md](./README_VISUALIZADOR.md)** | Referencia rápida del visualizador |
| **[TUTORIAL_VISUALIZADOR_MARKER.md](./TUTORIAL_VISUALIZADOR_MARKER.md)** | Tutorial completo del visualizador |
| **[TUTORIAL_CONVERTIR_PDF.md](./TUTORIAL_CONVERTIR_PDF.md)** | Tutorial de conversión con Marker |

---

## 🛠️ Scripts y Herramientas

### Visualización HTML

| Archivo | Descripción | Uso |
|---------|-------------|-----|
| **`generador_visualizacion_marker.py`** | Script principal para generar visualizaciones HTML | `python3 generador_visualizacion_marker.py <pdf> <dir_marker> [salida.html]` |
| **`procesar_lote.sh`** | Script bash para procesar múltiples PDFs por lotes | `./procesar_lote.sh` |

---

## 🚀 Flujo de trabajo completo

### 1. Convertir PDF con Marker

```bash
# Convertir un PDF
marker documento.pdf --output_dir .
```

**Salida:**
```
documento/
├── documento.md              # Texto extraído en Markdown
├── documento_meta.json       # Metadatos de la conversión
├── _page_0_Picture_1.jpeg   # Imágenes extraídas
└── ...
```

### 2. Generar visualización HTML

```bash
# Generar visualización para un documento
python3 generador_visualizacion_marker.py \
  documento.pdf \
  documento \
  visualizacion_documento.html
```

**Salida:**
```
visualizacion_documento.html   # Interfaz web interactiva
pdf_pages/                     # Páginas del PDF renderizadas
└── page_0.png
└── page_1.png
└── ...
```

### 3. Revisar en navegador

```bash
open visualizacion_documento.html
```

---

## 📋 Inicio rápido

### Instalación de dependencias

```bash
# Instalar Marker (solo primera vez)
pip install marker-pdf

# Instalar PyMuPDF para el visualizador
pip install PyMuPDF
```

### Ejemplo completo

```bash
# 1. Convertir PDF
marker mi_revista_1930.pdf --output_dir .

# 2. Generar visualización
python3 generador_visualizacion_marker.py \
  mi_revista_1930.pdf \
  mi_revista_1930 \
  revision_revista.html

# 3. Abrir en navegador
open revision_revista.html
```

---

## 🔄 Procesamiento por lotes

### Opción 1: Script automatizado

```bash
# Procesar todos los PDFs del directorio actual
./procesar_lote.sh
```

El script:
- ✅ Busca todos los PDFs con sus directorios de conversión
- ✅ Genera visualizaciones para cada uno
- ✅ Guarda resultados en `visualizaciones/`
- ✅ Muestra resumen con estadísticas

### Opción 2: Loop manual

```bash
for pdf in *.pdf; do
    nombre="${pdf%.pdf}"
    python3 generador_visualizacion_marker.py \
      "$pdf" \
      "$nombre" \
      "visualizacion_${nombre}.html"
done
```

---

## 📁 Estructura de archivos recomendada

```
proyecto_digitalizacion/
│
├── INDICE.md                          ← Este archivo
├── README_VISUALIZADOR.md             ← Referencia rápida
├── TUTORIAL_VISUALIZADOR_MARKER.md    ← Tutorial completo
├── TUTORIAL_CONVERTIR_PDF.md          ← Tutorial de conversión
│
├── generador_visualizacion_marker.py  ← Script principal
├── procesar_lote.sh                   ← Script por lotes
│
├── originales/                        ← PDFs originales
│   ├── revista_1930_01.pdf
│   └── revista_1930_02.pdf
│
├── revista_1930_01/                   ← Salida de Marker
│   ├── revista_1930_01.md
│   ├── revista_1930_01_meta.json
│   └── _page_*_*.jpeg
│
├── revista_1930_02/                   ← Salida de Marker
│   └── ...
│
├── visualizaciones/                   ← Visualizaciones HTML
│   ├── visualizacion_revista_1930_01.html
│   └── visualizacion_revista_1930_02.html
│
└── pdf_pages/                         ← Renders de PDFs
    ├── page_0.png
    ├── page_1.png
    └── ...
```

---

## ✨ Características del visualizador

### Interfaz HTML interactiva

- ✅ **Vista comparativa** lado a lado: PDF original vs texto extraído
- ✅ **Navegación fluida** con teclado (← →) o botones
- ✅ **Galería de imágenes** con zoom (lightbox)
- ✅ **Estadísticas** de conversión
- ✅ **Diseño responsive** que se adapta a cualquier pantalla
- ✅ **Ligero** (~100KB) y funciona offline

### Estadísticas mostradas

- Total de páginas procesadas
- Páginas con imágenes extraídas
- Total de imágenes extraídas
- Método OCR utilizado (SURYA, Tesseract, etc.)

---

## 🎯 Casos de uso

### Investigación académica
- Digitalización de fuentes históricas
- Corpus textuales para análisis lingüístico
- Preservación de patrimonio documental

### Control de calidad
- Revisión manual de transcripciones OCR
- Detección de errores en extracción de texto
- Validación de procesamiento masivo

### Documentación
- Evidencia de proceso de conversión
- Comparación antes/después
- Material para informes de proyecto

---

## 🐛 Solución de problemas

### Error común 1: `ModuleNotFoundError: No module named 'fitz'`

```bash
pip install PyMuPDF
```

### Error común 2: `FileNotFoundError`

Verifica que existen:
```bash
ls documento.pdf                    # PDF original
ls documento/documento.md           # Markdown de Marker
ls documento/documento_meta.json    # Metadatos de Marker
```

### Error común 3: Las imágenes no se ven

Abre el HTML desde el **mismo directorio** donde ejecutaste el script:
```bash
cd /Users/maria/Documents/marker-conversions
open visualizacion.html
```

Ver tutorial completo para más detalles: [TUTORIAL_VISUALIZADOR_MARKER.md](./TUTORIAL_VISUALIZADOR_MARKER.md)

---

## 📖 Documentación adicional

### Para Marker
- Repositorio oficial: https://github.com/VikParuchuri/marker
- Documentación: Incluida en el repositorio

### Para PyMuPDF
- Documentación: https://pymupdf.readthedocs.io/
- Repositorio: https://github.com/pymupdf/PyMuPDF

---

## 🎓 Proyecto académico

Herramientas desarrolladas para:

**LexiMus: Léxico y ontología de la música en español**
PID2022-139589NB-C33

Instituciones participantes:
- Universidad de Salamanca
- Instituto Complutense de Ciencias Musicales
- Universidad de La Rioja

---

## 📊 Estadísticas del proyecto

### Corpus procesado
- **25.8 millones** de palabras
- **3,238** archivos de texto
- **19** revistas musicales españolas
- Período: **1842-2024** (182 años)

### Revistas incluidas
ONDAS, Revista Musical Hispanoamericana, Revista Musical de Bilbao, Revista Triunfo, El Sol, MondoSonoro, y más.

---

## 📝 Notas de versión

**Versión actual: 3.0**

### Versión 3.0 (27/10/2025)
- ✅ División correcta de texto por páginas usando TOC de Marker
- ✅ Referencias a archivos locales (HTML ligero)
- ✅ Interfaz responsive mejorada
- ✅ Script de procesamiento por lotes
- ✅ Documentación completa

### Versión 2.0
- División básica por marcadores de imágenes
- Primera versión funcional

### Versión 1.0
- Prototipo inicial con imágenes embebidas

---

## 🤝 Contribuciones

Para reportar problemas o sugerir mejoras, contacta con el equipo del proyecto LexiMus.

---

**Última actualización:** 27 de octubre de 2025
