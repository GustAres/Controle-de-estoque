
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
class RegistroItem:
    nome: str = ""
    qtde: int = 0
    valor_compra: float = 0.0
    valor_venda: float = 0.0
    total_brutoC: float = 0.0
    total_brutoV: float = 0.0
    total_liquido: float = 0.0

item = []

#######################Função para criar produto e inserir no estoque#######################
def inserir():
    banco = sqlite3.connect('Estoque.db')
    tabela = banco.cursor()

    while True:
        nome = input("Digite o nome do produto ou 'fim' para encerrar: ").lower()
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
        total_liquido = total_brutoV - total_brutoC

        #confirmaçao para adicinor no eastoque
        print(f"CONFIRMAÇÃO \n Produto : {nome} \n Quantidade : {qtde} \n Valor de Compra: {valor_compra} \n Valor de venda {valor_venda}")
        confirma = input("DIGITE 'S' OU 'N' : ").lower()
        if confirma == "n":
            print('VOLTANDO...\n')
            continue

        novo_item = RegistroItem(nome, qtde, valor_compra, valor_venda, total_brutoC, total_brutoV, total_liquido)
        item.append((novo_item.nome, novo_item.qtde, novo_item.valor_compra, novo_item.valor_venda, novo_item.total_brutoC, novo_item.total_brutoV, novo_item.total_liquido))
        tabela.executemany("INSERT INTO Estoque VALUES(?,?,?,?,?,?,?)",item )
        banco.commit()

    banco.close()



#######################Função para adicionar ou remover produto que ja existe ao estoque#######################
def alterar():
    banco = sqlite3.connect('Estoque.db')
    tabela = banco.cursor()

    while True:
        opcao = int(input('1- ad   2- remv  ou 0 pra ence'))
        if opcao == 0:
            break
        elif opcao == 1 :
            nome = input('Qual produto você quer adicionar: ').lower()
            tabela.execute("SELECT nome FROM Estoque WHERE nome = ?", (nome,))
            if tabela.fetchone() == None:
                print('Este produto não está no estoque. Tente novamente.')
                continue
            tabela.execute("SELECT qtde FROM Estoque WHERE nome = ?", (nome,))
            itemA = tabela.fetchone()
            adicionar = int(input("Quantidade que ira adicionar: "))
            nova_qtde = itemA[0] + adicionar
            print("Quantidade atualizado")
            tabela.execute("UPDATE Estoque SET qtde =? WHERE nome =?", (nova_qtde, nome))
            banco.commit()

        elif opcao == 2:
            nome = input('Qual produto você quer remover: ').lower()
            tabela.execute("SELECT nome FROM Estoque WHERE nome = ?", (nome,))
            if tabela.fetchone() == None:
                print('Este produto não está no estoque. Tente novamente.')
                continue
            tabela.execute("SELECT qtde FROM Estoque WHERE nome =?", (nome,))
            itemR = tabela.fetchone()
            remover = int(input("Quantidade que ira remover: "))
            if remover > itemR[0]:
                print('Quantidade a remover é maior que a quantidade existente no estoque.')
                continue
            nova_qtdeR = itemR[0] - remover
            print("Quantidade atualizado")
            tabela.execute("UPDATE Estoque SET qtde =? WHERE nome =?", (nova_qtdeR, nome))
            banco.commit()
        else:
            print('Opção invalida. Tente novamente.')
            continue

def remover():
    banco = sqlite3.connect('Estoque.db')
    tabela = banco.cursor()
    while True:
        nome = input('Qual produto você quer remover: ').lower()
        tabela.execute("SELECT nome FROM Estoque WHERE nome =?", (nome,))
        if tabela.fetchone() == None:
            print('Este produto não está no estoque. Tente novamente.')
            continue
        print(f"CONFIRMAÇÃO \n Produto : {nome}")
        confirma = input("DIGITE 'S' OU 'N' : ").lower()
        if confirma == "n":
            print('VOLTANDO...\n')
            continue
        tabela.execute("DELETE FROM Estoque WHERE nome =?", (nome,))
        banco.commit()
        print("Produto removido")
        break


def pesquisa():
    banco = sqlite3.connect('Estoque.db')
    tabela = banco.cursor()

    while True:
        nome = input('Qual produto você quer pesquisar: ').lower()
        tabela.execute("SELECT nome, qtde, total_brutoV FROM Estoque WHERE nome = ?", (nome,))
        produto = tabela.fetchone()

        if produto is None:
            print('Este produto não está no estoque.')
            continue

        print(f"Produto: {produto[0]}")
        print(f'Quantidade: {produto[1]} unidades')
        print(f'Valor total bruto: R$ {produto[2]:.2f}')

        opcao = input("Quer ver outro produto? 'S' ou 'N' ").lower()
        if opcao == "n":
            break
        elif opcao != "s":
            print('Opção inválida. Tente novamente.')

    banco.close()
















banco.close()

