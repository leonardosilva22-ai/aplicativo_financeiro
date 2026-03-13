import sqlite3
import os
from datetime import datetime
from pathlib import Path

# Caminho do banco de dados
DB_PATH = Path(__file__).parent / "financeiro.db"

def get_connection():
    """Obtém uma conexão com o banco de dados"""
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn

def init_database():
    """Inicializa o banco de dados com as tabelas necessárias"""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Tabela de categorias
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categorias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT UNIQUE NOT NULL,
            tipo TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Tabela de bancos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bancos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT UNIQUE NOT NULL,
            saldo_inicial REAL DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Tabela de transações
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo TEXT NOT NULL,
            categoria_id INTEGER NOT NULL,
            banco_id INTEGER NOT NULL,
            valor REAL NOT NULL,
            descricao TEXT,
            data DATE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (categoria_id) REFERENCES categorias(id),
            FOREIGN KEY (banco_id) REFERENCES bancos(id)
        )
    ''')
    
    # Inserir categorias padrão se não existirem
    try:
        cursor.execute("INSERT INTO categorias (nome, tipo) VALUES (?, ?)", ("Moradia", "Despesa"))
        cursor.execute("INSERT INTO categorias (nome, tipo) VALUES (?, ?)", ("Comunicação", "Despesa"))
        cursor.execute("INSERT INTO categorias (nome, tipo) VALUES (?, ?)", ("Alimentação", "Despesa"))
        cursor.execute("INSERT INTO categorias (nome, tipo) VALUES (?, ?)", ("Transporte", "Despesa"))
        cursor.execute("INSERT INTO categorias (nome, tipo) VALUES (?, ?)", ("Saúde", "Despesa"))
        cursor.execute("INSERT INTO categorias (nome, tipo) VALUES (?, ?)", ("Pessoais", "Despesa"))
        cursor.execute("INSERT INTO categorias (nome, tipo) VALUES (?, ?)", ("Educação", "Despesa"))
        cursor.execute("INSERT INTO categorias (nome, tipo) VALUES (?, ?)", ("Lazer", "Despesa"))
        cursor.execute("INSERT INTO categorias (nome, tipo) VALUES (?, ?)", ("Serv. Financeiros", "Despesa"))
        cursor.execute("INSERT INTO categorias (nome, tipo) VALUES (?, ?)", ("Empresa", "Despesa"))
        cursor.execute("INSERT INTO categorias (nome, tipo) VALUES (?, ?)", ("Dependentes", "Despesa"))
        cursor.execute("INSERT INTO categorias (nome, tipo) VALUES (?, ?)", ("Diversos", "Despesa"))
        cursor.execute("INSERT INTO categorias (nome, tipo) VALUES (?, ?)", ("Salário", "Receita"))
        cursor.execute("INSERT INTO categorias (nome, tipo) VALUES (?, ?)", ("Freelance", "Receita"))
        cursor.execute("INSERT INTO categorias (nome, tipo) VALUES (?, ?)", ("Investimentos", "Receita"))
        cursor.execute("INSERT INTO categorias (nome, tipo) VALUES (?, ?)", ("Ações", "Investimento"))
        cursor.execute("INSERT INTO categorias (nome, tipo) VALUES (?, ?)", ("Criptomoedas", "Investimento"))
        cursor.execute("INSERT INTO categorias (nome, tipo) VALUES (?, ?)", ("Imóveis", "Investimento"))
        cursor.execute("INSERT INTO categorias (nome, tipo) VALUES (?, ?)", ("Renda Fixa", "Investimento"))
    except sqlite3.IntegrityError:
        pass  # Categorias já existem
    
    conn.commit()
    conn.close()

# Funções CRUD para Categorias
def get_categorias(tipo=None):
    """Obtém todas as categorias ou filtrado por tipo"""
    conn = get_connection()
    cursor = conn.cursor()
    
    if tipo:
        cursor.execute("SELECT * FROM categorias WHERE tipo = ? ORDER BY nome", (tipo,))
    else:
        cursor.execute("SELECT * FROM categorias ORDER BY nome")
    
    categorias = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return categorias

def add_categoria(nome, tipo):
    """Adiciona uma nova categoria"""
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO categorias (nome, tipo) VALUES (?, ?)", (nome, tipo))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        conn.close()
        return False

def delete_categoria(categoria_id):
    """Deleta uma categoria"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM categorias WHERE id = ?", (categoria_id,))
    conn.commit()
    conn.close()

# Funções CRUD para Bancos
def get_bancos():
    """Obtém todos os bancos"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bancos ORDER BY nome")
    bancos = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return bancos

def add_banco(nome, saldo_inicial=0):
    """Adiciona um novo banco"""
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO bancos (nome, saldo_inicial) VALUES (?, ?)", (nome, saldo_inicial))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        conn.close()
        return False

def delete_banco(banco_id):
    """Deleta um banco"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM bancos WHERE id = ?", (banco_id,))
    conn.commit()
    conn.close()

# Funções CRUD para Transações
def get_transacoes(tipo=None, mes=None, ano=None):
    """Obtém transações com filtros opcionais"""
    conn = get_connection()
    cursor = conn.cursor()
    
    query = "SELECT t.*, c.nome as categoria_nome, b.nome as banco_nome FROM transacoes t " \
            "JOIN categorias c ON t.categoria_id = c.id " \
            "JOIN bancos b ON t.banco_id = b.id WHERE 1=1 "
    params = []
    
    if tipo:
        query += "AND t.tipo = ? "
        params.append(tipo)
    
    if mes and ano:
        query += "AND strftime('%m', t.data) = ? AND strftime('%Y', t.data) = ? "
        params.append(f"{mes:02d}")
        params.append(str(ano))
    
    query += "ORDER BY t.data DESC"
    
    cursor.execute(query, params)
    transacoes = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return transacoes

def add_transacao(tipo, categoria_id, banco_id, valor, descricao, data):
    """Adiciona uma nova transação"""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        "INSERT INTO transacoes (tipo, categoria_id, banco_id, valor, descricao, data) "
        "VALUES (?, ?, ?, ?, ?, ?)",
        (tipo, categoria_id, banco_id, valor, descricao, data)
    )
    conn.commit()
    transacao_id = cursor.lastrowid
    conn.close()
    return transacao_id

def update_transacao(transacao_id, tipo, categoria_id, banco_id, valor, descricao, data):
    """Atualiza uma transação"""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        "UPDATE transacoes SET tipo = ?, categoria_id = ?, banco_id = ?, valor = ?, descricao = ?, data = ? "
        "WHERE id = ?",
        (tipo, categoria_id, banco_id, valor, descricao, data, transacao_id)
    )
    conn.commit()
    conn.close()

def delete_transacao(transacao_id):
    """Deleta uma transação"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM transacoes WHERE id = ?", (transacao_id,))
    conn.commit()
    conn.close()

def get_transacao_by_id(transacao_id):
    """Obtém uma transação pelo ID com informações de categoria e banco"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT t.*, c.nome as categoria_nome, b.nome as banco_nome 
        FROM transacoes t 
        JOIN categorias c ON t.categoria_id = c.id 
        JOIN bancos b ON t.banco_id = b.id 
        WHERE t.id = ?
    """, (transacao_id,))
    transacao = cursor.fetchone()
    conn.close()
    return dict(transacao) if transacao else None

# Funções para relatórios
def get_saldo_total():
    """Calcula o saldo total de todos os bancos"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT 
            COALESCE(SUM(CASE WHEN t.tipo IN ('Receita', 'Investimento') THEN t.valor ELSE -t.valor END), 0) as saldo
        FROM transacoes t
    """)
    result = cursor.fetchone()
    conn.close()
    return result['saldo'] if result else 0

def get_resumo_mes(mes, ano):
    """Obtém resumo do mês"""
    conn = get_connection()
    cursor = conn.cursor()
    
    query = """
        SELECT 
            t.tipo,
            COALESCE(SUM(t.valor), 0) as total
        FROM transacoes t
        WHERE strftime('%m', t.data) = ? AND strftime('%Y', t.data) = ?
        GROUP BY t.tipo
    """
    
    cursor.execute(query, (f"{mes:02d}", str(ano)))
    resumo = {row['tipo']: row['total'] for row in cursor.fetchall()}
    conn.close()
    return resumo

def get_gastos_por_categoria(mes, ano):
    """Obtém gastos por categoria no mês"""
    conn = get_connection()
    cursor = conn.cursor()
    
    query = """
        SELECT 
            c.nome,
            COALESCE(SUM(t.valor), 0) as total
        FROM transacoes t
        JOIN categorias c ON t.categoria_id = c.id
        WHERE t.tipo = 'Despesa' 
        AND strftime('%m', t.data) = ? 
        AND strftime('%Y', t.data) = ?
        GROUP BY c.nome
        ORDER BY total DESC
    """
    
    cursor.execute(query, (f"{mes:02d}", str(ano)))
    gastos = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return gastos

def get_receitas_por_categoria(mes, ano):
    """Obtém receitas por categoria no mês"""
    conn = get_connection()
    cursor = conn.cursor()
    
    query = """
        SELECT 
            c.nome,
            COALESCE(SUM(t.valor), 0) as total
        FROM transacoes t
        JOIN categorias c ON t.categoria_id = c.id
        WHERE t.tipo = 'Receita' 
        AND strftime('%m', t.data) = ? 
        AND strftime('%Y', t.data) = ?
        GROUP BY c.nome
        ORDER BY total DESC
    """
    
    cursor.execute(query, (f"{mes:02d}", str(ano)))
    receitas = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return receitas
