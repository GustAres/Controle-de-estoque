import sqlite3

def conectar_banco():
    """Conectar ao banco de dados SQLite."""
    conn = sqlite3.connect('estoque.db')
    cursor = conn.cursor()
    return conn, cursor

def criar_tabela():
    """Criar a tabela de produtos, caso não exista."""
    conn, cursor = conectar_banco()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco_compra REAL NOT NULL,
        preco_venda REAL NOT NULL,
        quantidade INTEGER NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

def inserir_produto(nome, preco_compra, preco_venda, quantidade):
    """Inserir um novo produto na tabela."""
    conn, cursor = conectar_banco()
    cursor.execute('''
    INSERT INTO produtos (nome, preco_compra, preco_venda, quantidade)
    VALUES (?, ?, ?, ?)
    ''', (nome, preco_compra, preco_venda, quantidade))
    conn.commit()
    conn.close()

def editar_produto(id_produto, nome, preco_compra, preco_venda, quantidade):
    """Editar os detalhes de um produto existente."""
    conn, cursor = conectar_banco()
    cursor.execute('''
    UPDATE produtos
    SET nome = ?, preco_compra = ?, preco_venda = ?, quantidade = ?
    WHERE id = ?
    ''', (nome, preco_compra, preco_venda, quantidade, id_produto))
    conn.commit()
    conn.close()

def visualizar_produtos():
    """Visualizar todos os produtos na tabela."""
    conn, cursor = conectar_banco()
    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()
    conn.close()
    return produtos
