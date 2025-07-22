@echo off
echo 📁 Creando estructura de modelos…

rem crea las carpetas si no existen
if not exist app\models (
    mkdir app\models
)

rem crea los archivos vacíos
type nul > app\models\__init__.py
type nul > app\models\usuario.py
type nul > app\models\categoria.py
type nul > app\models\transaccion.py

echo ✅ Archivos creados:
dir /b app\models

echo 🧹 Escribiendo __init__.py…

(
echo from .usuario import Usuario
echo from .categoria import Categoria
echo from .transaccion import Transaccion
) > app\models\__init__.py

echo 🎉 ¡Estructura de modelos lista!
pause

:: ===============================================
:: setup_modelos.bat
::
:: Este script crea la estructura de carpetas y archivos
:: para los modelos de la app Finansmarrt.
::
:: Crea:
::   app\models\__init__.py
::   app\models\usuario.py
::   app\models\categoria.py
::   app\models\transaccion.py
::
:: Uso:
::   Ejecuta este archivo haciendo doble clic
::   o desde la consola: setup_modelos.bat
::
:: Autor: Reinaldo + ChatGPT
:: ===============================================
