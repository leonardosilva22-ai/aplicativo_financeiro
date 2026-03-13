@echo off
REM Script para iniciar o Planejador Financeiro

cls
echo.
echo ====================================
echo    PLANEJADOR FINANCEIRO
echo    Iniciando aplicativo...
echo ====================================
echo.

REM Ativar ambiente virtual se existir (opcional)
REM call venv\Scripts\activate.bat

REM Iniciar o aplicativo Streamlit
python -m streamlit run main.py

pause
