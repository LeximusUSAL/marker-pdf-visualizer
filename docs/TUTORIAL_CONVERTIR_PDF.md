# Tutorial: Extraer Texto e Imágenes de PDFs con marker_single

## ¿Qué hace marker_single?

`marker_single` es un comando que **automáticamente**:
- Convierte documentos PDF a texto (formato Markdown)
- **Extrae TODAS las imágenes, figuras, gráficos y tablas** del PDF como archivos de imagen separados
- Conserva la estructura del documento (títulos, párrafos, listas)

**Perfecto para**: Artículos científicos, libros, documentos con muchas imágenes, tesis, informes técnicos.

---

# 📋 PARTE 1: INSTALACIÓN (Solo una vez)

## Para Windows

### Paso 1: Instalar Python
1. Ve a https://www.python.org/downloads/
2. Descarga Python (versión 3.8 o superior)
3. Durante la instalación, **marca la casilla** "Add Python to PATH"
4. Haz clic en "Install Now"

### Paso 2: Abrir la Terminal (Símbolo del sistema)
1. Presiona la tecla `Windows` y escribe **cmd**
2. Haz clic en "Símbolo del sistema" o "Command Prompt"
3. Se abrirá una ventana negra

### Paso 3: Instalar marker_single
Copia y pega este comando y presiona `Enter`:
```bash
pip install marker-pdf
```

---

## Para macOS

### Paso 1: Verificar Python
Python ya viene instalado en Mac. No necesitas hacer nada.

### Paso 2: Abrir la Terminal
1. Presiona `Cmd + Espacio`
2. Escribe **Terminal**
3. Presiona `Enter`

### Paso 3: Instalar marker_single
Copia y pega este comando y presiona `Enter`:
```bash
pip install marker-pdf
```

Si aparece un error, prueba con:
```bash
pip3 install marker-pdf
```

---

## Para Linux (Ubuntu/Debian)

### Paso 1: Verificar Python
Abre la terminal (Ctrl + Alt + T) y escribe:
```bash
python3 --version
```

Si no está instalado:
```bash
sudo apt update
sudo apt install python3 python3-pip
```

### Paso 2: Instalar marker_single
```bash
pip3 install marker-pdf
```

---

# 🚀 PARTE 2: USAR marker_single

## Entendiendo el comando básico

El comando tiene 3 partes:

```
marker_single [RUTA_DEL_PDF] [CARPETA_DE_DESTINO]
```

- **[RUTA_DEL_PDF]**: Dónde está tu archivo PDF
- **[CARPETA_DE_DESTINO]**: Dónde quieres guardar los resultados

---

## 🪟 INSTRUCCIONES PARA WINDOWS

### Método 1: Guardar en Documentos (Fácil)

1. **Mueve tu PDF** a la carpeta `Documentos`
2. **Anota el nombre exacto** del archivo (ejemplo: `articulo.pdf`)
3. Abre el **Símbolo del sistema** (tecla Windows + escribe "cmd")
4. Copia y pega este comando (cambia `NOMBRE.pdf` por tu archivo):

```bash
marker_single %USERPROFILE%\Documents\NOMBRE.pdf %USERPROFILE%\Documents\resultados-marker
```

**Ejemplo real:**
```bash
marker_single %USERPROFILE%\Documents\articulo_cientifico.pdf %USERPROFILE%\Documents\resultados-marker
```

### Método 2: Guardar en cualquier carpeta que elijas

1. **Crea una carpeta** donde quieras guardar los resultados (ejemplo: `C:\MisPDFs\resultados`)
2. Anota la ruta completa de tu PDF
3. Usa este formato:

```bash
marker_single "C:\ruta\a\tu\archivo.pdf" "C:\MisPDFs\resultados"
```

**Ejemplo real:**
```bash
marker_single "C:\Users\Maria\Desktop\documento.pdf" "D:\Extracciones\proyecto1"
```

### Método 3: Arrastrar y soltar (Más fácil)

1. Abre el Símbolo del sistema
2. Escribe: `marker_single ` (con un espacio al final)
3. **Arrastra tu PDF** desde el Explorador de archivos a la ventana negra
4. Escribe un espacio y luego: `"C:\carpeta\donde\guardar"`
5. Presiona `Enter`

---

## 🍎 INSTRUCCIONES PARA macOS

### Método 1: Guardar en Documentos (Fácil)

1. **Mueve tu PDF** a la carpeta `Documentos`
2. **Anota el nombre exacto** (ejemplo: `articulo.pdf`)
3. Abre la **Terminal** (Cmd + Espacio, escribe "Terminal")
4. Copia y pega (cambia `NOMBRE.pdf` por tu archivo):

```bash
marker_single ~/Documents/NOMBRE.pdf ~/Documents/resultados-marker
```

**Ejemplo real:**
```bash
marker_single ~/Documents/tesis_doctoral.pdf ~/Documents/resultados-marker
```

### Método 2: Guardar en cualquier carpeta que elijas

1. **Crea una carpeta** donde quieras (ejemplo: carpeta "PDFs-Procesados" en el Escritorio)
2. Usa este formato:

```bash
marker_single /ruta/completa/al/archivo.pdf /ruta/donde/guardar
```

**Ejemplo real:**
```bash
marker_single ~/Downloads/informe.pdf ~/Desktop/PDFs-Procesados
```

### Método 3: Arrastrar y soltar (Más fácil)

1. Abre la Terminal
2. Escribe: `marker_single ` (con espacio al final)
3. **Arrastra tu PDF** desde el Finder a la Terminal
4. Escribe un espacio
5. **Arrastra la carpeta de destino** a la Terminal (o escribe la ruta)
6. Presiona `Enter`

---

## 🐧 INSTRUCCIONES PARA LINUX

### Método 1: Guardar en Documentos (Fácil)

1. **Mueve tu PDF** a `~/Documentos` o `~/Documents`
2. Abre la Terminal (Ctrl + Alt + T)
3. Copia y pega (cambia `NOMBRE.pdf`):

```bash
marker_single ~/Documents/NOMBRE.pdf ~/Documents/resultados-marker
```

### Método 2: Guardar en cualquier carpeta

```bash
marker_single /home/tu_usuario/ruta/archivo.pdf /home/tu_usuario/carpeta_destino
```

**Ejemplo real:**
```bash
marker_single ~/Descargas/paper.pdf ~/Proyectos/extraccion-imagenes
```

### Método 3: Usando rutas absolutas

```bash
marker_single "$(pwd)/archivo.pdf" "$(pwd)/resultados"
```

Esto usa la carpeta actual donde estés en la terminal.

---

# 📁 PARTE 3: ¿QUÉ OBTIENES?

## Archivos generados automáticamente

Cuando `marker_single` termina, crea una **carpeta con un número** (ejemplo: `1000203211`) dentro de tu carpeta de destino.

Dentro encontrarás:

### 1. Archivo `.md` (Texto del documento)
- Contiene TODO el texto del PDF en formato Markdown
- Puedes abrirlo con cualquier editor de texto
- El nombre será algo como `1000203211.md`

### 2. Imágenes extraídas automáticamente
Todas las imágenes, con nombres descriptivos:
- `_page_0_Picture_4.jpeg` - Imagen de la página 0
- `_page_1_Picture_1.jpeg` - Imagen de la página 1
- `_page_7_Figure_0.jpeg` - Figura de la página 7
- etc.

**¡Marker extrae TODAS las imágenes automáticamente sin necesidad de hacerlo manualmente!**

### 3. Archivo `_meta.json`
- Información técnica sobre el procesamiento
- Normalmente no necesitas abrirlo

---

# ⏱️ PARTE 4: ESPERAR EL PROCESO

## ¿Cuánto tarda?

| Tamaño del PDF | Tiempo aproximado |
|---------------|-------------------|
| 5-20 páginas | 1-5 minutos |
| 20-50 páginas | 5-15 minutos |
| 50-100 páginas | 15-30 minutos |
| 100+ páginas | 30-90 minutos |

**Importante:**
- **NO cierres la ventana** mientras está procesando
- Verás mucho texto pasando - ¡es normal!
- Al finalizar verás: `[INFO] marker: Total time: XXX`

---

# 🎯 EJEMPLOS COMPLETOS PASO A PASO

## Ejemplo 1: Estudiante con tesis en Windows

**Situación**: Tienes `mi_tesis.pdf` en el Escritorio y quieres guardarlo en una carpeta llamada `Tesis-Procesada`

```bash
# Paso 1: Crear la carpeta de destino
mkdir %USERPROFILE%\Desktop\Tesis-Procesada

# Paso 2: Procesar
marker_single %USERPROFILE%\Desktop\mi_tesis.pdf %USERPROFILE%\Desktop\Tesis-Procesada
```

## Ejemplo 2: Investigador en macOS con artículo descargado

**Situación**: Descargaste `paper_2024.pdf` y quieres guardarlo en Documentos

```bash
marker_single ~/Downloads/paper_2024.pdf ~/Documents/articulos-procesados
```

## Ejemplo 3: Usuario de Linux procesando múltiples documentos

**Situación**: Tienes varios PDFs en una carpeta y quieres procesarlos

```bash
# Procesar el primero
marker_single ~/Documentos/libro1.pdf ~/Documentos/extracciones

# Procesar el segundo
marker_single ~/Documentos/libro2.pdf ~/Documentos/extracciones

# Procesar el tercero
marker_single ~/Documentos/libro3.pdf ~/Documentos/extracciones
```

---

# 🔧 SOLUCIÓN DE PROBLEMAS

## Error: "command not found" o "no se reconoce"

**Problema**: marker_single no está instalado correctamente

**Solución Windows**:
```bash
pip install marker-pdf
```

**Solución macOS/Linux**:
```bash
pip3 install marker-pdf
```

## Error: "No such file or directory"

**Problema**: La ruta del archivo es incorrecta

**Soluciones**:
1. Verifica que el nombre esté bien escrito
2. Asegúrate de incluir la extensión `.pdf`
3. Si el nombre tiene espacios, usa comillas:
   ```bash
   marker_single "~/Documents/Mi Artículo con Espacios.pdf" ~/Documents/resultados
   ```

## El PDF tiene contraseña

**Problema**: El PDF está protegido

**Solución**:
1. Abre el PDF en Adobe Reader
2. Guárdalo sin contraseña
3. Procesa el nuevo archivo

## Los archivos se guardan en una ubicación extraña

**Windows**: Busca en `C:\Users\TuUsuario\AppData\...`
**macOS**: Busca en `/opt/homebrew/...` o `~/Library/...`
**Linux**: Busca en `~/.local/...`

**Solución**: Especifica siempre la carpeta de destino en el comando

---

# 💡 CONSEJOS AVANZADOS

## Crear carpetas organizadas

**Windows**:
```bash
mkdir %USERPROFILE%\Documents\Extracciones-PDF\proyecto1
marker_single archivo.pdf %USERPROFILE%\Documents\Extracciones-PDF\proyecto1
```

**macOS/Linux**:
```bash
mkdir -p ~/Documents/Extracciones-PDF/proyecto1
marker_single archivo.pdf ~/Documents/Extracciones-PDF/proyecto1
```

## Ver archivos procesados

**Windows**: Explorador de archivos → Documentos → resultados-marker
**macOS**: Finder → Documentos → resultados-marker
**Linux**: Nautilus/Dolphin → Documentos → resultados-marker

## Procesar PDFs grandes

Para PDFs muy grandes (200+ páginas):
1. Cierra otros programas para liberar memoria
2. Deja el ordenador trabajando (puedes irte a tomar un café)
3. No uses el ordenador para otras tareas pesadas mientras procesa

---

# 📖 ABRIR LOS ARCHIVOS .MD

## Opción 1: Editor de texto simple

**Windows**: Bloc de notas, Notepad++
**macOS**: TextEdit
**Linux**: gedit, Kate, nano

## Opción 2: Editores Markdown (RECOMENDADO)

- **Typora** (https://typora.io) - Visualización bonita
- **Visual Studio Code** (https://code.visualstudio.com) - Gratuito y potente
- **Obsidian** (https://obsidian.md) - Para organizar documentos

---

# ❓ PREGUNTAS FRECUENTES

**P: ¿Funciona con PDFs escaneados?**
R: Sí, pero la calidad puede variar. Funciona mejor con PDFs que tienen texto real.

**P: ¿Puedo procesar varios PDFs a la vez?**
R: No automáticamente. Debes ejecutar el comando una vez por cada PDF.

**P: ¿Las imágenes mantienen la calidad original?**
R: Sí, marker extrae las imágenes en alta calidad (formato JPEG).

**P: ¿Es gratis?**
R: Sí, marker es completamente gratuito y de código abierto.

**P: ¿Necesito internet?**
R: Solo para la instalación inicial. Luego funciona sin internet.

---

**Última actualización**: Octubre 2024
**Versión**: 2.0
**Compatible con**: Windows 10/11, macOS 10.14+, Linux (Ubuntu 18.04+)
