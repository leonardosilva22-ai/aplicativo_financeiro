# 📊 Planejador Financeiro - Guia de Distribuição

## ✅ Executável Criado com Sucesso!

Seu aplicativo Planejador Financeiro foi convertido em um executável **standalone** com o ícone do aplicativo.

---

## 📂 Arquivo Gerado

**Localização:** `dist/Planejador_Financeiro.exe`

**Tamanho:** ~300-400 MB (inclui Python, bibliotecas e todos os arquivos necessários)

**Ícone:** finance.ico (exibido na taskbar e desktop)

---

## 🚀 Como Usar

### Para Você:
1. Abra a pasta `dist/`
2. Execute `Planejador_Financeiro.exe`
3. O aplicativo será aberto automaticamente em http://localhost:8501

### Para Compartilhar com Outros:
1. Localize a pasta `dist/`
2. Copie **APENAS** o arquivo `Planejador_Financeiro.exe`
3. Compartilhe o arquivo com qualquer pessoa
4. Qualquer um pode executar o arquivo **SEM necessidade de instalar Python**

---

## ⚠️ Informações Importantes

### ✅ O que Incluir:
- `Planejador_Financeiro.exe` - **OBRIGATÓRIO**

### ❌ O que NÃO Incluir:
- Python (já está integrado no .exe)
- Bibliotecas pip (já estão integradas)
- Arquivo `financeiro.db` (é criado automaticamente)

### 📝 Dados Persistentes:
- **Banco de Dados:** Um arquivo `financeiro.db` será criado automaticamente na pasta de execução
- **Localização:** Será salvo no mesmo diretório onde o `.exe` está
- **Backup:** Copie o arquivo `financeiro.db` para fazer backup dos dados

---

## 🔧 Se Ocorrer Algum Problema:

### Problema: "Não consegui abrir o aplicativo"
**Solução:**
- Verifique se o arquivo não está corrompido
- Recrie o executável usando: `build_exe.ps1`
- Certifique-se de que a porta 8501 não está em uso

### Problema: "Erro ao acessar http://localhost:8501"
**Solução:**
- Aguarde 5-10 segundos após clicar no .exe
- Verifique se há algum firewall bloqueando a porta 8501
- Reinicie o computador e tente novamente

### Problema: "Arquivo muito grande para compartilhar"
**Solução:**
- Use ferramentas de compressão (WinRAR, 7-Zip) para reduzir o tamanho
- Compartilhe via Google Drive, OneDrive ou similar
- O arquivo .exe tem ~300-400 MB

---

## 📋 Processo de Compilação Usado

```powershell
PyInstaller --onefile `
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
    run_app.py
```

**Parâmetros Explicados:**
- `--onefile` - Cria um único arquivo executável
- `--windowed` - Oculta o console (interface mais limpa)
- `--icon` - Define o ícone do aplicativo
- `--add-data` - Inclui os arquivos Python necessários
- `--hidden-import` - Inclui bibliotecas que o PyInstaller possa perder

---

## 🔄 Recriar o Executável (Se Necessário)

1. Delete as pastas `build/` e `dist/`
2. Execute novamente: `build_exe.ps1`
3. Novo executável será gerado em `dist/`

---

## 📞 Suporte

Se você fizer atualizações no código:
1. Modifique os arquivos `.py` normalmente
2. Execute `build_exe.ps1` novamente
3. Novo executável será criado com as mudanças

---

**Criado em:** 11/03/2026  
**Versão:** 1.0.0  
**Status:** ✅ Pronto para Produção
