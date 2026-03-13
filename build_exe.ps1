#!/usr/bin/env ps1
# Script para criar o executável do Planejador Financeiro
# Coloque este arquivo na pasta do projeto e execute-o

$PythonPath = "C:\Users\LeonardodeSouzaSilva\.local\bin\python3.14.exe"
$ProjetoDir = Get-Location

Write-Host "================================" -ForegroundColor Cyan
Write-Host "Construindo Executável" -ForegroundColor Cyan
Write-Host "Planejador Financeiro" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

# Verificar se PyInstaller está instalado
Write-Host "📦 Verificando dependências..." -ForegroundColor Yellow

& $PythonPath -c "import PyInstaller" 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host "⚠️  PyInstaller não encontrado. Instalando..."
    & $PythonPath -m pip install pyinstaller --break-system-packages -q
}

Write-Host "✅ Dependências OK" -ForegroundColor Green
Write-Host ""

# Criar o executável
Write-Host "🔨 Compilando executável..." -ForegroundColor Yellow
Write-Host ""

& $PythonPath -m PyInstaller `
    --onefile `
    --windowed `
    --name "Planejador_Financeiro" `
    --icon "finance.ico" `
    --add-data "main.py;." `
    --add-data "database.py;." `
    --add-data "utils.py;." `
    --hidden-import=streamlit `
    --hidden-import=plotly `
    --hidden-import=pandas `
    --hidden-import=sqlite3 `
    --hidden-import=altair `
    run_app.py

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "================================" -ForegroundColor Green
    Write-Host "✅ Executável criado com sucesso!" -ForegroundColor Green
    Write-Host "================================" -ForegroundColor Green
    Write-Host ""
    Write-Host "📂 Arquivo gerado:" -ForegroundColor Cyan
    Write-Host "   dist\Planejador_Financeiro.exe" -ForegroundColor White
    Write-Host ""
    Write-Host "🚀 Para usar:" -ForegroundColor Cyan
    Write-Host "   1. Abra a pasta 'dist'" -ForegroundColor White
    Write-Host "   2. Copie o arquivo 'Planejador_Financeiro.exe'" -ForegroundColor White
    Write-Host "   3. Cole em qualquer lugar e execute!" -ForegroundColor White
    Write-Host ""
    Write-Host "💡 Dicas:" -ForegroundColor Cyan
    Write-Host "   ✓ Pode compartilhar o .exe com outras pessoas" -ForegroundColor White
    Write-Host "   ✓ Não necessita Python instalado" -ForegroundColor White
    Write-Host "   ✓ Banco de dados (financeiro.db) será criado automaticamente" -ForegroundColor White
    Write-Host ""
} else {
    Write-Host ""
    Write-Host "❌ Erro ao compilar!" -ForegroundColor Red
    Write-Host "Verifique os arquivos e tente novamente." -ForegroundColor Red
    Write-Host ""
}

Read-Host "Pressione ENTER para fechar"
