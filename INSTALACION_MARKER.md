# Tutorial: Instalación y Uso de Marker

Guía completa para instalar y usar [Marker](https://github.com/VikParuchuri/marker), una herramienta de conversión PDF a Markdown impulsada por IA que ofrece resultados superiores a los OCR tradicionales.

---

## 📋 Tabla de Contenidos

1. [¿Qué es Marker?](#qué-es-marker)
2. [Requisitos del sistema](#requisitos-del-sistema)
3. [Instalación](#instalación)
4. [Uso básico: marker_single](#uso-básico-marker_single)
5. [Opciones avanzadas](#opciones-avanzadas)
6. [Ejemplos prácticos](#ejemplos-prácticos)
7. [Solución de problemas](#solución-de-problemas)

---

## ¿Qué es Marker?

**Marker** es una herramienta de conversión PDF a Markdown que utiliza modelos de IA (incluyendo SURYA OCR) para:

- ✅ Extraer texto con alta precisión (incluso de PDFs escaneados)
- ✅ Preservar el formato (encabezados, listas, tablas)
- ✅ Extraer imágenes automáticamente
- ✅ Manejar documentos multiidioma
- ✅ Procesar layouts complejos (columnas, cuadros de texto)

### Ventajas sobre OCR tradicional

| Característica | Tesseract/OCR Tradicional | Marker |
|----------------|---------------------------|--------|
| Precisión | 85-90% | 95-98% |
| Formato preservado | ❌ No | ✅ Sí (Markdown) |
| Tablas | ⚠️ Limitado | ✅ Bien |
| Multiidioma | ⚠️ Requiere configuración | ✅ Automático |
| Layouts complejos | ❌ Difícil | ✅ Excelente |
| Velocidad | Rápido | Medio (GPU recomendada) |

---

## Requisitos del Sistema

### Mínimos

- **Sistema operativo:** Linux, macOS, Windows (WSL2)
- **Python:** 3.8 o superior
- **RAM:** 4 GB
- **Espacio en disco:** 5 GB libres

### Recomendados

- **Python:** 3.10+
- **RAM:** 8-16 GB
- **GPU:** NVIDIA con CUDA (acelera 5-10x)
- **Espacio en disco:** 10 GB libres

### Verificar Python

```bash
python3 --version
# Debe mostrar: Python 3.8.x o superior
```

---

## Instalación

### Opción 1: Instalación con pip (Recomendado)

Esta es la forma más sencilla y funciona en la mayoría de sistemas:

```bash
# Instalar Marker
pip install marker-pdf

# Verificar instalación
marker_single --help
```

Si ves el mensaje de ayuda, ¡la instalación fue exitosa!

### Opción 2: Instalación desde el repositorio

Para la versión de desarrollo o contribuir al proyecto:

```bash
# Clonar repositorio
git clone https://github.com/VikParuchuri/marker.git
cd marker

# Instalar en modo editable
pip install -e .

# Verificar
marker_single --help
```

### Instalación con GPU (Opcional pero muy recomendado)

Si tienes una GPU NVIDIA con CUDA:

```bash
# Desinstalar torch CPU
pip uninstall torch torchvision

# Instalar torch con CUDA 11.8
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118

# O para CUDA 12.1
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121

# Verificar GPU disponible
python3 -c "import torch; print('GPU disponible:', torch.cuda.is_available())"
```

### Verificar instalación completa

```bash
# Verificar que todos los comandos están disponibles
marker_single --version
python3 -c "import marker; print('Marker importado correctamente')"
```

---

## Uso Básico: marker_single

El comando `marker_single` convierte un único archivo PDF a Markdown.

### Sintaxis básica

```bash
marker_single <archivo_pdf> <directorio_salida> [opciones]
```

### Ejemplo mínimo

```bash
marker_single documento.pdf salida/
```

Esto crea:
```
salida/
└── documento/
    ├── documento.md              # Texto extraído en Markdown
    ├── documento_meta.json       # Metadatos de la conversión
    ├── _page_0_Picture_1.jpeg   # Imágenes extraídas
    ├── _page_0_Picture_2.jpeg
    └── ...
```

### Estructura de la salida

| Archivo | Descripción |
|---------|-------------|
| `documento.md` | Texto completo en formato Markdown |
| `documento_meta.json` | Metadatos: número de páginas, método OCR, tabla de contenidos |
| `_page_N_Picture_M.jpeg` | Imágenes extraídas (N=página, M=número de imagen) |
| `_page_N_Figure_M.jpeg` | Figuras/diagramas extraídos |

---

## Opciones Avanzadas

### Idioma del documento

```bash
# Documento en español
marker_single documento.pdf salida/ --langs Spanish

# Documento multiidioma (español e inglés)
marker_single documento.pdf salida/ --langs Spanish,English

# Documento en francés
marker_single documento.pdf salida/ --langs French
```

**Idiomas soportados:** Spanish, English, French, German, Portuguese, Italian, Chinese, Japanese, Korean, Arabic, Russian, y más.

### Aumentar velocidad de procesamiento

```bash
# Aumentar batch multiplier (usa más RAM pero es más rápido)
marker_single documento.pdf salida/ --batch_multiplier 2

# Para PDFs muy grandes
marker_single documento.pdf salida/ --batch_multiplier 4
```

⚠️ **Nota:** Valores altos (4+) requieren 8GB+ de RAM.

### Rango de páginas específico

```bash
# Solo páginas 1-10
marker_single documento.pdf salida/ --page_range 1-10

# Páginas específicas: 1, 5, 10
marker_single documento.pdf salida/ --pages 1,5,10
```

### Forzar OCR en todo el documento

```bash
# Útil para PDFs escaneados de baja calidad
marker_single documento.pdf salida/ --force_ocr
```

### Deshabilitar extracción de imágenes

```bash
# Solo extraer texto (más rápido)
marker_single documento.pdf salida/ --disable_image_extraction
```

### Configurar dispositivo (CPU/GPU)

```bash
# Forzar CPU (si GPU da problemas)
marker_single documento.pdf salida/ --device cpu

# Usar GPU específica (si tienes varias)
marker_single documento.pdf salida/ --device cuda:0
```

### Todas las opciones juntas

```bash
marker_single documento.pdf salida/ \
  --langs Spanish \
  --batch_multiplier 2 \
  --force_ocr \
  --device cuda:0
```

---

## Ejemplos Prácticos

### Ejemplo 1: Revista histórica en español (1930)

```bash
marker_single revista_ritmo_enero_1930.pdf conversiones/ \
  --langs Spanish \
  --batch_multiplier 2
```

**Salida:**
```
conversiones/revista_ritmo_enero_1930/
├── revista_ritmo_enero_1930.md
├── revista_ritmo_enero_1930_meta.json
├── _page_0_Picture_1.jpeg    # Portada
├── _page_1_Picture_1.jpeg    # Fotografía de músico
└── ...
```

### Ejemplo 2: Documento multiidioma

```bash
marker_single informe_bilingue.pdf conversiones/ \
  --langs Spanish,English \
  --batch_multiplier 2
```

### Ejemplo 3: Solo páginas de interés

```bash
# Solo procesar páginas 50-100 de un libro grande
marker_single libro_completo.pdf conversiones/ \
  --page_range 50-100 \
  --langs Spanish
```

### Ejemplo 4: Procesamiento rápido sin imágenes

```bash
# Solo texto, sin extraer imágenes
marker_single articulo.pdf conversiones/ \
  --disable_image_extraction \
  --batch_multiplier 4
```

### Ejemplo 5: Lote de PDFs

```bash
#!/bin/bash
# Script para procesar múltiples PDFs

for pdf in *.pdf; do
    echo "Procesando: $pdf"
    marker_single "$pdf" conversiones/ \
      --langs Spanish \
      --batch_multiplier 2
    echo "✓ Completado: $pdf"
done
```

Guarda como `convertir_lote.sh`, da permisos y ejecuta:
```bash
chmod +x convertir_lote.sh
./convertir_lote.sh
```

---

## Solución de Problemas

### Error: `marker_single: command not found`

**Causa:** Marker no está instalado o el PATH no está configurado

**Soluciones:**

1. Verificar instalación:
```bash
pip list | grep marker
```

2. Reinstalar:
```bash
pip install --upgrade marker-pdf
```

3. Usar ruta completa:
```bash
python3 -m marker.convert_single documento.pdf salida/
```

### Error: `CUDA out of memory`

**Causa:** GPU sin suficiente memoria VRAM

**Soluciones:**

1. Reducir batch multiplier:
```bash
marker_single documento.pdf salida/ --batch_multiplier 1
```

2. Usar CPU:
```bash
marker_single documento.pdf salida/ --device cpu
```

3. Procesar por páginas:
```bash
marker_single documento.pdf salida/ --page_range 1-10
```

### Error: `ModuleNotFoundError: No module named 'torch'`

**Causa:** PyTorch no está instalado

**Solución:**
```bash
pip install torch torchvision
```

### Marker es extremadamente lento

**Causa:** Ejecutándose en CPU

**Soluciones:**

1. Verificar si GPU está disponible:
```bash
python3 -c "import torch; print(torch.cuda.is_available())"
```

2. Si es `False`, instalar CUDA:
```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
```

3. Especificar GPU:
```bash
marker_single documento.pdf salida/ --device cuda:0
```

### La calidad del OCR es baja

**Soluciones:**

1. Forzar OCR:
```bash
marker_single documento.pdf salida/ --force_ocr
```

2. Especificar idioma correcto:
```bash
marker_single documento.pdf salida/ --langs Spanish
```

3. Aumentar batch multiplier:
```bash
marker_single documento.pdf salida/ --batch_multiplier 4
```

### Error: `RuntimeError: CUDA error: no kernel image is available`

**Causa:** Versión de PyTorch incompatible con tu GPU

**Solución:**

1. Verificar versión de CUDA:
```bash
nvcc --version
```

2. Instalar PyTorch compatible:
```bash
# Para CUDA 11.8
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118

# Para CUDA 12.1
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
```

### El PDF es muy grande (>1000 páginas)

**Solución:** Dividir en lotes:

```bash
# Páginas 1-500
marker_single libro.pdf salida_parte1/ --page_range 1-500

# Páginas 501-1000
marker_single libro.pdf salida_parte2/ --page_range 501-1000

# Páginas 1001-1500
marker_single libro.pdf salida_parte3/ --page_range 1001-1500
```

---

## Consejos de Rendimiento

### Para máxima velocidad

```bash
marker_single documento.pdf salida/ \
  --batch_multiplier 4 \
  --device cuda:0 \
  --disable_image_extraction
```

### Para máxima calidad

```bash
marker_single documento.pdf salida/ \
  --langs Spanish \
  --force_ocr \
  --batch_multiplier 2
```

### Para documentos grandes

```bash
# Procesar en chunks
for i in {0..10}; do
    start=$((i*100+1))
    end=$((start+99))
    marker_single documento.pdf salida_parte_$i/ \
      --page_range $start-$end \
      --batch_multiplier 2
done
```

---

## Verificación de la Conversión

Después de convertir, verifica la calidad:

```bash
# Ver estadísticas
cat salida/documento/documento_meta.json | python3 -m json.tool

# Ver primeras líneas del Markdown
head -50 salida/documento/documento.md

# Contar imágenes extraídas
ls salida/documento/_page_*.jpeg | wc -l
```

---

## Recursos Adicionales

- **Repositorio oficial:** https://github.com/VikParuchuri/marker
- **Documentación:** Incluida en el repositorio
- **Issues/Problemas:** https://github.com/VikParuchuri/marker/issues

---

## Siguiente Paso

Una vez que hayas convertido tus PDFs con Marker, usa nuestro **Visualizador HTML** para revisar la calidad de las conversiones:

👉 [Tutorial del Visualizador](./docs/TUTORIAL_VISUALIZADOR.md)

```bash
python3 scripts/generador_visualizacion.py \
  documento.pdf \
  salida/documento \
  revision.html
```

---

**Última actualización:** Octubre 2025
**Versión de Marker:** 0.2.x
