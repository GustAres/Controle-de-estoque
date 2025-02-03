
from dataclasses import dataclass
import sqlite3


banco = sqlite3.connect('Estoque.db')
tabela = banco.cursor()
tabela.execute('''
    CREATE TABLE IF NOT EXISTS Estoque (
        nome TEXT PRIMARY KEY,
        qtde INTEGER,
        valor_compra REAL,
        valor_venda REAL,
        total_brutoC REAL,
        total_brutoV REAL,
        total_liquido REAL
    )
''')

@dataclass
class registroitem:
    def __init__(self, nome, qtde, valor_compra, valor_venda, total_brutoC, total_brutoV, total_liquido  ):
        self.nome = nome
        self.qtde = qtde
        self.valor_compra = valor_compra
        self.valor_venda = valor_venda
        self.total_brutoC = total_brutoC
        self.total_brutoV = total_brutoV
        self.total_liquido = total_liquido





item = []

def inserir():
    banco = sqlite3.connect('Estoque.db')
    tabela = banco.cursor()

    while True:
        nome = input('Nome do produto: ')
        if nome.lower() == 'fim':
            break
        #Verificando se ja existe
        tabela.execute("SELECT nome FROM Estoque WHERE nome = ?", (nome,))
        if tabela.fetchone():
            print('Este produto já está no estoque. Tente novamente.')
            continue

        qtde = int(input('Quantidade de produto: '))
        valor_compra = float(input('Valor que comprou: R$ '))
        valor_venda = float(input('Valor que ira vender: R$ '))
        total_brutoC = qtde * valor_compra
        total_brutoV = qtde * valor_venda
        total_liquido = total_brutoC - total_brutoV

        novo_item = registroitem(nome, qtde, valor_compra, valor_venda, total_brutoC, total_brutoV, total_liquido)
        item.append((novo_item.nome, novo_item.qtde,novo_item.valor_compra, novo_item.valor_venda, novo_item.total_brutoC, novo_item.total_brutoV, novo_item.total_liquido))

        tabela.executemany("INSERT INTO Estoque VALUES(?,?,?,?,?,?,?)",item )
        banco.commit()
        tabela.execute('SELECT * FROM Estoque')


    print(tabela.fetchall())
    banco.close()


def adicionar():
    banco = sqlite3.connect('Estoque.db')
    tabela = banco.cursor()

    while True:
        nome = input('Qual produto você quer adicionar: ')
        if nome.lower() == 'fim':
            break

        tabela.execute("SELECT qtde FROM Estoque WHERE nome = ?", (nome,))
        item = tabela.fetchone()
        tabela.execute("SELECT valor_venda FROM Estoque WHERE nome = ?", (nome,))
        item2 = tabela.fetchone()

        if item:
            qtde = int(input("Qual a quantidade que deseja adicionar: "))


            #arrumar isso
            ##nova_qtde = item[0] + qtde
            ###novo_valor = float(input("Novo valor: "))

            tabela.execute("UPDATE Estoque SET qtde = ? WHERE nome = ?", (nova_qtde, nome))
            banco.commit()
            print(f"A quantidade do item '{nome}' foi atualizada para {nova_qtde}.")
        else:
            print(f"O item '{nome}' não foi encontrado no estoque.")
    banco.close()
















banco.close()

