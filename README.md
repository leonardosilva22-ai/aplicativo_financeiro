# 💰 Planejador Financeiro - Aplicativo de Controle Financeiro

Um aplicativo moderno e intuitivo para gerenciar receitas, despesas e investimentos pessoais, desenvolvido com Streamlit e Python.

## 🎯 Funcionalidades

### 📊 Dashboard
- Visualização clara de receitas, despesas e investimentos do mês
- Gráficos comparativos de receita vs despesa (últimos 6 meses)
- Análise patrimonial (Ativo/Passivo)
- Distribuição de gastos e receitas por categoria
- Seleção de mês e ano para análise

### 💳 Gerenciamento de Transações
- Registrar receitas, despesas e investimentos
- Categorização automática de transações
- Associação de transações a diferentes bancos
- Histórico completo de lançamentos
- **Editar e deletar transações existentes**

### 🏷️ Categorias
- Categorias pré-cadastradas (Moradia, Alimentação, Transporte, etc.)
- Adicionar categorias personalizadas
- Categorizar por tipo: Receita, Despesa ou Investimento
- Gerenciar categorias (editar e deletar)

### 🏦 Bancos
- Cadastrar múltiplos bancos/instituições financeiras
- Definir saldo inicial para cada banco
- Associar transações a bancos específicos
- Gerenciar bancos (editar e deletar)

### 📈 Relatórios Detalhados
- Resumo mensal de receitas, despesas e investimentos
- Saldo líquido mensal
- Visualização completa de todas as transações do período
- Filtros por mês e ano

### 🗑️ Editar/Deletar
- Interface dedicada para editar transações existentes
- Deletar transações com confirmação
- Visualização prévia antes de alterar

## 🚀 Como Executar

### 1. Requisitos
- Python 3.10 ou superior
- pip (gerenciador de pacotes Python)

### 2. Instalação

```bash
# Navegar até a pasta do projeto
cd path/to/aplicativo_financeiro

# Instalar dependências
pip install -r requirements.txt
```

### 3. Executar o Aplicativo

```bash
streamlit run main.py
```

O aplicativo abrirá em seu navegador padrão (geralmente em `http://localhost:8501`)

## 📁 Estrutura do Projeto

```
aplicativo_financeiro/
├── main.py              # Arquivo principal (interface Streamlit)
├── database.py          # Gerenciamento do banco de dados SQLite
├── utils.py             # Funções utilitárias
├── requirements.txt     # Dependências do projeto
├── financeiro.db        # Banco de dados (criado automaticamente)
└── README.md           # Este arquivo
```

## 💾 Banco de Dados

O aplicativo utiliza SQLite para armazenar dados de forma segura e local. O arquivo `financeiro.db` é criado automaticamente na primeira execução e armazena:

- **Categorias**: Tipos de receita, despesa e investimento
- **Bancos**: Instituições e contas financeiras
- **Transações**: Registro completo de todas as operações financeiras

## 🎨 Interface

A interface é intuitiva e organizada em abas:

1. **Dashboard** - Visão geral do mês selecionado
2. **Lançamentos** - Registrar novas transações
3. **Categorias** - Gerenciar categorias
4. **Bancos** - Gerenciar bancos/instituições
5. **Relatórios** - Análise detalhada do período
6. **Editar/Deletar** - Modificar ou remover transações

## 📱 Responsive Design

O aplicativo é otimizado para funcionar em diferentes tamanhos de tela, facilitando o uso em desktop, tablet e celular.

## 🔐 Segurança

- Dados armazenados localmente em banco de dados SQLite
- Nenhum dado é enviado para servidores externos
- Controle total sobre suas informações financeiras

## 🛠️ Tecnologias Utilizadas

- **Streamlit** - Framework para criar aplicações web em Python
- **SQLite** - Banco de dados relacional leve
- **Pandas** - Manipulação e análise de dados
- **Plotly** - Gráficos e visualizações interativas

## 📝 Licença

Este projeto é fornecido como está para uso pessoal.

## ❓ Dúvidas ou Sugestões?

Sinta-se livre para expandir o projeto com novas funcionalidades conforme sua necessidade!

---

**Desenvolvido com ❤️ para facilitar o controle financeiro pessoal**
