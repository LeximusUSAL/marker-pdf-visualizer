#!/bin/bash
# Script para procesar por lotes múltiples conversiones de Marker
# Uso: ./procesar_lote.sh

set -e  # Salir si hay error

# Colores para output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # Sin color

echo -e "${BLUE}═══════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}   Procesador por Lotes - Visualizador Marker             ${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════${NC}\n"

# Verificar que el script generador existe
if [ ! -f "generador_visualizacion_marker.py" ]; then
    echo -e "${RED}Error: generador_visualizacion_marker.py no encontrado${NC}"
    echo "Ejecuta este script desde el directorio marker-conversions/"
    exit 1
fi

# Verificar Python y PyMuPDF
if ! python3 -c "import fitz" 2>/dev/null; then
    echo -e "${RED}Error: PyMuPDF no está instalado${NC}"
    echo "Instala con: pip install PyMuPDF"
    exit 1
fi

# Crear directorios si no existen
mkdir -p visualizaciones

# Contador
total=0
exitosos=0
fallidos=0

echo -e "${BLUE}Buscando archivos PDF...${NC}\n"

# Procesar cada PDF que tenga su directorio de conversión
for pdf in *.pdf; do
    # Saltar si no hay PDFs
    [ -e "$pdf" ] || continue

    nombre="${pdf%.pdf}"
    dir_conversion="$nombre"

    # Verificar que existe el directorio de conversión de Marker
    if [ ! -d "$dir_conversion" ]; then
        echo -e "${RED}⊗ Saltando $pdf (no existe directorio $dir_conversion/)${NC}"
        continue
    fi

    # Verificar que existen los archivos necesarios
    if [ ! -f "$dir_conversion/${nombre}.md" ]; then
        echo -e "${RED}⊗ Saltando $pdf (no existe ${nombre}.md)${NC}"
        continue
    fi

    if [ ! -f "$dir_conversion/${nombre}_meta.json" ]; then
        echo -e "${RED}⊗ Saltando $pdf (no existe ${nombre}_meta.json)${NC}"
        continue
    fi

    total=$((total + 1))

    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BLUE}Procesando [$total]: $pdf${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

    # Nombre del archivo de salida
    html_output="visualizaciones/visualizacion_${nombre}.html"

    # Ejecutar generador
    if python3 generador_visualizacion_marker.py \
        "$pdf" \
        "$dir_conversion" \
        "$html_output" 2>&1 | grep -E "(✓|✅|📄|📋|📝|🖼️|Error)"; then

        exitosos=$((exitosos + 1))
        echo -e "\n${GREEN}✓ Generado: $html_output${NC}\n"
    else
        fallidos=$((fallidos + 1))
        echo -e "\n${RED}✗ Error al procesar $pdf${NC}\n"
    fi
done

# Resumen final
echo -e "${BLUE}═══════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}                    RESUMEN FINAL                          ${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════${NC}"
echo -e "  Total procesados:    ${BLUE}$total${NC}"
echo -e "  ${GREEN}✓ Exitosos:          $exitosos${NC}"

if [ $fallidos -gt 0 ]; then
    echo -e "  ${RED}✗ Fallidos:          $fallidos${NC}"
fi

echo -e "${BLUE}═══════════════════════════════════════════════════════════${NC}\n"

if [ $exitosos -gt 0 ]; then
    echo -e "${GREEN}Las visualizaciones se guardaron en: visualizaciones/${NC}"
    echo -e "${GREEN}Abre cualquiera con: open visualizaciones/visualizacion_*.html${NC}\n"
fi

# Listar archivos generados
if [ $exitosos -gt 0 ]; then
    echo -e "${BLUE}Archivos generados:${NC}"
    ls -lh visualizaciones/*.html 2>/dev/null | awk '{print "  • " $9 " (" $5 ")"}'
fi

exit 0
