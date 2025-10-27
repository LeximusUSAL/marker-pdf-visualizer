# Ejemplo de Salida de Marker

Este es un ejemplo de cómo se ve un documento convertido por Marker de PDF a Markdown.

## Documento Original: Revista Musical Ilustrada RITMO (1930)

### Metadatos

- **Páginas:** 20
- **Método OCR:** SURYA
- **Idioma detectado:** Spanish
- **Imágenes extraídas:** 19

---

## Extracto del Contenido Convertido

# REVISTA MUSICAL ILUSTRADA

Año II

Director: ROGELIO DEL VILLAR

Núm. 5

![Imagen de portada](_page_0_Picture_4.jpeg)

## EDITORIALES

### Españoladas

No hace mucho daban cuenta los periódicos de un concierto de música española celebrado en Berlín, organizado por la Asociación de Compositores alemanes, a cuyo concierto concurrieron representantes de la Embajada, de la Prensa y colonia española, y se decía que entre los asistentes figuraba Ricardo Strauss.

El programa, integrado por pasodobles, tangos, marchas toreras de autores indocumentados, fué una vergüenza, contribuyendo a perpetuar la falsa leyenda de la plebeyez de nuestra música, poniéndonos en ridículo.

Por esto es consolador, y de ello nos congratulamos, que artistas del rango de Conchita Supervía haya obtenido en París un resonante triunfo con motivo de un concierto de gran gala celebrado en la Sala Gaveau...

### La Orquesta Nacional

La creación de la Orquesta Nacional es una aspiración ha tiempo en proyecto que no acaba de cuajar esperando una mano inteligente y activa que le organice definitivamente.

El actual Gobierno, ejecutivo y rápido en sus resoluciones, es el más indicado para amparar este proyecto que dotaría a la capital de España de una formidable entidad artística...

---

## Características de la Conversión

### Formato Preservado

- ✅ **Encabezados jerárquicos** (H1, H2, H3)
- ✅ **Listas** (numeradas y con viñetas)
- ✅ **Referencias a imágenes** con rutas relativas
- ✅ **Negritas e itálicas** cuando corresponde
- ✅ **Estructura de párrafos** mantenida

### Imágenes Extraídas

Las imágenes se guardan con nomenclatura clara:

```
_page_0_Picture_4.jpeg    ← Imagen 4 de la página 0
_page_1_Picture_1.jpeg    ← Imagen 1 de la página 1
_page_1_Picture_14.jpeg   ← Imagen 14 de la página 1
```

### Metadatos Generados (JSON)

```json
{
  "table_of_contents": [
    {
      "title": "REVISTA MUSICAL ILUSTRADA",
      "heading_level": null,
      "page_id": 0
    },
    {
      "title": "EDITORIALES",
      "heading_level": null,
      "page_id": 2
    }
  ],
  "page_stats": [
    {
      "page_id": 0,
      "text_extraction_method": "surya",
      "block_counts": [
        ["Line", 7],
        ["Text", 4],
        ["Picture", 1]
      ]
    }
  ]
}
```

---

## Comparación con OCR Tradicional

### Tesseract (OCR Tradicional)

```
REVISTA MYSICAL ILVSTRADA
Ano II
Director ROGELIO DEL VILLAR
Num 5

EDITORIALES
Espanoladas
No hace mucho daban cuenta los periodicos...
```

❌ Sin formato
❌ Errores de reconocimiento ("MYSICAL" en lugar de "MUSICAL")
❌ Caracteres especiales perdidos
❌ Sin estructura jerárquica

### Marker (IA-Powered OCR)

```markdown
# REVISTA MUSICAL ILUSTRADA

Año II

Director: ROGELIO DEL VILLAR

Núm. 5

## EDITORIALES

### Españoladas

No hace mucho daban cuenta los periódicos...
```

✅ Formato Markdown preservado
✅ Reconocimiento preciso
✅ Caracteres especiales correctos
✅ Estructura jerárquica completa

---

## Casos de Uso Reales

Este tipo de conversión es ideal para:

1. **Digitalización de patrimonio documental**
   - Revistas históricas
   - Periódicos antiguos
   - Libros fuera de catálogo

2. **Corpus textuales**
   - Análisis lingüístico
   - Minería de texto
   - Investigación histórica

3. **Accesibilidad**
   - Texto extraído puede ser leído por lectores de pantalla
   - Búsqueda de contenido
   - Indexación automática

4. **Preservación digital**
   - Formato abierto (Markdown)
   - Separación texto/imágenes
   - Metadatos estructurados

---

## Cómo se Generó este Ejemplo

```bash
# 1. Conversión con Marker
marker_single revista_ritmo_1930_enero.pdf salida/ \
  --langs Spanish \
  --batch_multiplier 2

# 2. Visualización HTML
python3 scripts/generador_visualizacion.py \
  revista_ritmo_1930_enero.pdf \
  salida/revista_ritmo_1930_enero \
  revision_ritmo.html

# 3. Revisión en navegador
open revision_ritmo.html
```

---

**Para más información, consulta:**
- [INSTALACION_MARKER.md](../INSTALACION_MARKER.md) - Tutorial de instalación
- [docs/TUTORIAL_VISUALIZADOR.md](../docs/TUTORIAL_VISUALIZADOR.md) - Uso del visualizador
- [README.md](../README.md) - Documentación general
