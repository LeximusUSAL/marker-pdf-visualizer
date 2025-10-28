# 📄 Marker PDF Converter & Visualizer

Herramientas para convertir PDFs a Markdown con [Marker](https://github.com/VikParuchuri/marker) y generar visualizaciones HTML interactivas para revisión de calidad de las transcripciones OCR.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python 3.8+">
  <img src="https://img.shields.io/badge/License-Academic-green.svg" alt="License">
  <img src="https://img.shields.io/badge/OCR-Marker-orange.svg" alt="Marker OCR">
</p>

---

## 🎯 ¿Qué hace este proyecto?

Este repositorio proporciona:

1. **Tutorial de instalación y uso de Marker** - Guía completa para convertir PDFs a Markdown de forma automática
2. **Visualizador HTML interactivo** - Herramienta para revisar la calidad de las conversiones
3. **Scripts de automatización** - Procesamiento por lotes de múltiples documentos
4. **Documentación exhaustiva** - Tutoriales, ejemplos y solución de problemas

### Casos de uso

✅ Digitalización de documentos históricos
✅ Extracción de texto de revistas y periódicos antiguos
✅ Control de calidad de transcripciones OCR
✅ Corpus textuales para análisis lingüístico
✅ Preservación de patrimonio documental

---

## 🚀 Inicio Rápido

### 1. Instalar Marker

```bash
# Opción 1: Con pip (recomendado)
pip install marker-pdf

# Opción 2: Desde el repositorio
git clone https://github.com/VikParuchuri/marker.git
cd marker
pip install -e .
```

### 2. Convertir un PDF

```bash
# Conversión básica
marker_single documento.pdf salida/

# Con opciones avanzadas
marker_single documento.pdf salida/ \
  --langs Spanish \
  --batch_multiplier 2
```

### 3. Generar visualización HTML

```bash
# Clonar este repositorio
git clone https://github.com/tu-usuario/marker-visualizador.git
cd marker-visualizador

# Instalar dependencia
pip install PyMuPDF

# Generar visualización
python3 generador_visualizacion_marker.py \
  documento.pdf \
  salida/documento \
  revision.html

# Abrir en navegador
open revision.html
```

---

## 📂 Estructura del Repositorio

```
marker-visualizador/
│
├── README.md                          ← Este archivo
├── INSTALACION_MARKER.md              ← Tutorial de instalación de Marker
├── INDICE.md                          ← Índice completo del proyecto
├── LEEME_PRIMERO.txt                  ← Guía de inicio rápido
│
├── docs/                              ← Documentación
│   ├── README_VISUALIZADOR.md         ← Referencia rápida del visualizador
│   ├── TUTORIAL_VISUALIZADOR.md       ← Tutorial completo del visualizador
│   └── TUTORIAL_CONVERTIR_PDF.md      ← Tutorial de conversión con Marker
│
├── scripts/                           ← Herramientas
│   ├── generador_visualizacion.py     ← Generador de visualizaciones HTML
│   └── procesar_lote.sh               ← Procesamiento por lotes
│
└── ejemplos/                          ← Ejemplos y casos de uso
    └── ejemplo_salida.md              ← Ejemplo de salida de Marker
```

---

## 📖 Documentación

### Tutoriales Principales

| Documento | Descripción |
|-----------|-------------|
| **[INSTALACION_MARKER.md](./INSTALACION_MARKER.md)** | Cómo instalar y usar Marker (paso a paso) |
| **[docs/TUTORIAL_VISUALIZADOR.md](./docs/TUTORIAL_VISUALIZADOR.md)** | Tutorial completo del visualizador HTML |
| **[docs/TUTORIAL_CONVERTIR_PDF.md](./docs/TUTORIAL_CONVERTIR_PDF.md)** | Guía detallada de conversión con Marker |
| **[INDICE.md](./INDICE.md)** | Índice general con todos los recursos |

### Referencias Rápidas

- [LEEME_PRIMERO.txt](./LEEME_PRIMERO.txt) - Inicio rápido visual
- [docs/README_VISUALIZADOR.md](./docs/README_VISUALIZADOR.md) - Comandos básicos del visualizador

---

## 🛠️ Herramientas Incluidas

### 1. Generador de Visualizaciones HTML

Script Python que crea una interfaz web interactiva para revisar conversiones:

```bash
python3 scripts/generador_visualizacion.py <pdf> <dir_marker> [salida.html]
```

**Características:**
- Vista comparativa lado a lado (PDF original vs texto extraído)
- Navegación página por página
- Galería de imágenes extraídas con zoom
- Estadísticas de conversión
- HTML ligero (~100KB) que funciona offline

### 2. Procesador por Lotes

Script bash para procesar múltiples PDFs automáticamente:

```bash
./scripts/procesar_lote.sh
```

Procesa todos los PDFs del directorio actual que tengan su carpeta de conversión de Marker.

---

## 💡 Ejemplos de Uso

### Ejemplo 1: Conversión Simple

```bash
# 1. Convertir PDF con Marker
marker_single revista_1930.pdf conversiones/

# 2. Generar visualización
python3 scripts/generador_visualizacion.py \
  revista_1930.pdf \
  conversiones/revista_1930 \
  revision_revista.html

# 3. Abrir en navegador
open revision_revista.html
```

### Ejemplo 2: Procesamiento por Lotes

```bash
# Organizar archivos
mkdir -p pdfs conversiones revisiones

# Mover PDFs a procesar
mv *.pdf pdfs/

# Convertir todos con Marker
for pdf in pdfs/*.pdf; do
    marker_single "$pdf" conversiones/
done

# Generar visualizaciones
cd conversiones
../scripts/procesar_lote.sh
```

### Ejemplo 3: Documento Multiidioma

```bash
# PDF con español e inglés
marker_single documento.pdf salida/ \
  --langs Spanish,English \
  --batch_multiplier 2

# Visualización
python3 scripts/generador_visualizacion.py \
  documento.pdf \
  salida/documento \
  revision_multiidioma.html
```

---

## 🎨 Vista Previa del Visualizador

El visualizador HTML genera una interfaz interactiva como esta:

```
╔════════════════════════════════════════════════════════════╗
║  📄 Visualizador Marker - documento.pdf                   ║
║  ← Anterior | Siguiente →  Página: [5] de 20             ║
╠═══════════════════════════╦════════════════════════════════╣
║  📑 PDF Original          ║  📝 Texto Extraído            ║
║  ┌─────────────────────┐  ║  # Título del documento       ║
║  │                     │  ║                                ║
║  │  [Imagen del PDF]   │  ║  Contenido del texto          ║
║  │                     │  ║  transcrito por Marker...     ║
║  │                     │  ║                                ║
║  └─────────────────────┘  ║  ## Sección 2                 ║
║                           ║  Más contenido...             ║
╠═══════════════════════════╩════════════════════════════════╣
║  🖼️ Imágenes Extraídas por Marker                         ║
║  [img1] [img2] [img3] [img4]                              ║
╠════════════════════════════════════════════════════════════╣
║  📊 Estadísticas: 20 páginas | 15 imágenes | OCR: SURYA  ║
╚════════════════════════════════════════════════════════════╝
```

**Funcionalidades:**
- Navegación con teclado (← → para páginas, ESC para cerrar zoom)
- Vista comparativa o solo texto
- Zoom en imágenes (click)
- Desplazamiento sincronizado
- Diseño responsive

---

## 📊 Requisitos del Sistema

### Software Necesario

- **Python 3.8 o superior**
- **pip** (gestor de paquetes de Python)
- **Git** (para clonar repositorios)
- **4GB RAM mínimo** (8GB recomendado para PDFs grandes)
- **GPU CUDA** (opcional, pero acelera significativamente Marker)

### Dependencias Python

#### Para Marker:
```bash
pip install marker-pdf
```

#### Para el Visualizador:
```bash
pip install PyMuPDF
```

### Espacio en Disco

- Marker instalado: ~2GB
- Por cada PDF procesado: ~300-500MB (depende del número de páginas)

---

## 🔧 Instalación Detallada

### Paso 1: Clonar el Repositorio

```bash
git clone https://github.com/tu-usuario/marker-visualizador.git
cd marker-visualizador
```

### Paso 2: Instalar Marker

Sigue el tutorial completo en [INSTALACION_MARKER.md](./INSTALACION_MARKER.md)

```bash
# Instalación rápida
pip install marker-pdf

# Verificar instalación
marker_single --help
```

### Paso 3: Instalar Dependencias del Visualizador

```bash
pip install PyMuPDF
```

### Paso 4: Probar con un Ejemplo

```bash
# Descargar PDF de prueba (o usar tu propio PDF)
# Convertir
marker_single ejemplo.pdf salida/

# Visualizar
python3 scripts/generador_visualizacion.py \
  ejemplo.pdf \
  salida/ejemplo \
  prueba.html

open prueba.html
```

---

## 🐛 Solución de Problemas

### Error: `marker_single: command not found`

**Causa:** Marker no está instalado o no está en el PATH

**Solución:**
```bash
pip install marker-pdf
# o
python3 -m pip install marker-pdf
```

### Error: `ModuleNotFoundError: No module named 'fitz'`

**Causa:** PyMuPDF no está instalado

**Solución:**
```bash
pip install PyMuPDF
```

### Marker es muy lento

**Causa:** Ejecutándose en CPU en lugar de GPU

**Solución:**
```bash
# Instalar soporte CUDA (si tienes GPU NVIDIA)
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
```

### Las imágenes no se ven en el visualizador

**Causa:** Rutas relativas incorrectas

**Solución:** Abre el HTML desde el mismo directorio donde ejecutaste el script:
```bash
cd directorio_trabajo
open visualizacion.html
```

Ver más en [docs/TUTORIAL_VISUALIZADOR.md](./docs/TUTORIAL_VISUALIZADOR.md) sección "Solución de problemas"

---

## 🎓 Proyecto Académico

Este proyecto fue desarrollado como parte de:

**PID ID2025/280 LOS SOPORTES EFÍMEROS EN EL AULA UNIVERSITARIA**
coordinado por el Dr. Santiago Ruiz Torres- UNIVERSIDAD DE SALAMANCA

**Grupo de transferencia del conocimiento MUSLYME**
Música, Lenguaje y Medios de Comunicación- UNIVERSIDAD DE SALAMANCA

**LexiMus: Léxico y ontología de la música en español**
PID2022-139589NB-C33 UNIVERSIDAD DE SALAMANCA

Instituciones participantes:
- Universidad de Salamanca
- Instituto Complutense de Ciencias Musicales
- Universidad de La Rioja

### Corpus procesado

- **25.8 millones** de palabras
- **3,238** archivos de texto
- **19** revistas musicales españolas
- Período: **1842-2024** (182 años de historia musical)

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para contribuir:

1. Fork este repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 📜 Licencia

Este proyecto está destinado para uso académico y de investigación.

---

## 🔗 Enlaces Útiles

- [Marker - Repositorio Oficial](https://github.com/VikParuchuri/marker)
- [PyMuPDF Documentation](https://pymupdf.readthedocs.io/)
- [Marker Documentation](https://github.com/VikParuchuri/marker/blob/master/README.md)

---

## 📧 Contacto

Para preguntas sobre este proyecto, contacta con el equipo de LexiMus.

---

## ⭐ Agradecimientos

- [VikParuchuri](https://github.com/VikParuchuri) por crear Marker
- Equipo del proyecto LexiMus
- Comunidad de Python y OCR

---

**Última actualización:** Octubre 2025
**Versión:** 3.0
**Mantenedor:** Proyecto LexiMus
