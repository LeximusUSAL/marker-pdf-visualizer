# Visualizador de Conversiones Marker

Herramienta para generar interfaces HTML interactivas que permiten revisar conversiones PDF→Markdown realizadas con Marker.

## 🚀 Inicio rápido

```bash
# 1. Instalar dependencia
pip install PyMuPDF

# 2. Ejecutar
python3 generador_visualizacion_marker.py documento.pdf documento/ visualizacion.html

# 3. Abrir en navegador
open visualizacion.html
```

## 📖 Documentación completa

Lee el [TUTORIAL_VISUALIZADOR_MARKER.md](./TUTORIAL_VISUALIZADOR_MARKER.md) para:
- Guía paso a paso
- Ejemplos de uso
- Procesamiento por lotes
- Solución de problemas

## 📁 Archivos

| Archivo | Descripción |
|---------|-------------|
| `generador_visualizacion_marker.py` | Script principal (usar este) |
| `TUTORIAL_VISUALIZADOR_MARKER.md` | Tutorial completo |
| `README_VISUALIZADOR.md` | Este archivo (referencia rápida) |

## ✨ Características

- ✅ Vista comparativa PDF original vs texto extraído
- ✅ Navegación página por página
- ✅ Galería de imágenes extraídas
- ✅ Estadísticas de conversión
- ✅ Atajos de teclado (← → ESC)
- ✅ Diseño responsive y ligero (~100KB)

## 🔍 Ejemplo de salida

La visualización muestra:

```
┌─────────────────────────────────────────────────────────┐
│  📄 Visualizador Marker - documento.pdf                │
│  ← Anterior | Siguiente →  Página: [1] de 20           │
├──────────────────────────┬──────────────────────────────┤
│  📑 PDF Original         │  📝 Texto Extraído          │
│  ┌────────────────────┐  │  # Título                    │
│  │                    │  │  Contenido del texto...      │
│  │  [Imagen del PDF]  │  │  ## Subtítulo               │
│  │                    │  │  Más texto extraído...       │
│  └────────────────────┘  │                              │
├──────────────────────────┴──────────────────────────────┤
│  🖼️ Imágenes Extraídas por Marker                      │
│  [img1] [img2] [img3]                                   │
└─────────────────────────────────────────────────────────┘
```

## 📊 Requisitos

- Python 3.8+
- PyMuPDF (fitz)
- Archivos de Marker:
  - `documento.md` (texto extraído)
  - `documento_meta.json` (metadatos)
  - `_page_N_*.jpeg` (imágenes extraídas)

## 🐛 Problemas comunes

| Error | Solución |
|-------|----------|
| `ModuleNotFoundError: No module named 'fitz'` | `pip install PyMuPDF` |
| `FileNotFoundError` | Verifica rutas del PDF y directorio Marker |
| Las imágenes no se ven | Abre el HTML desde el mismo directorio |
| El texto no corresponde | Verifica que `_meta.json` tenga `table_of_contents` |

## 💡 Casos de uso

- Control de calidad de digitalizaciones masivas
- Revisión manual de OCR con IA
- Documentación de procesos de conversión
- Detección de errores en extracción de texto
- Investigación de fuentes históricas

## 🎓 Proyecto académico

Desarrollado para **LexiMus: Léxico y ontología de la música en español**
(PID2022-139589NB-C33)

---

**Última actualización:** 27 octubre 2025 | **Versión:** 3.0
