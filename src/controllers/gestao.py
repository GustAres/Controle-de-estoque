
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
def inserir(cadastro_nome, cadastro_qtde, cadastro_valorC, cadastro_valorV):
    banco = sqlite3.connect('Estoque.db')
    tabela = banco.cursor()
    nome = cadastro_nome.lower()

    #Verificando se ja existe
    tabela.execute("SELECT nome FROM Estoque WHERE nome = ?", (nome,))
    if tabela.fetchone():
        return  print("ERRO")

    qtde = cadastro_qtde
    valor_compra = cadastro_valorC
    valor_venda = cadastro_valorV
    total_brutoC = qtde * valor_compra
    total_brutoV = qtde * valor_venda
    total_liquido = total_brutoV - total_brutoC

    ###############confirmaçao para adicinor no eastoque#####################
    print(f"CONFIRMAÇÃO \n Produto : {nome} \n Quantidade : {qtde} \n Valor de Compra: {valor_compra} \n Valor de venda {valor_venda}")
    confirma = input("DIGITE 'S' OU 'N' : ").lower()
    if confirma == "n":
      return print('VOLTANDO...\n')

        ######################################################################

    novo_item = RegistroItem(nome, qtde, valor_compra, valor_venda, total_brutoC, total_brutoV, total_liquido)
    item.append((novo_item.nome, novo_item.qtde, novo_item.valor_compra, novo_item.valor_venda, novo_item.total_brutoC, novo_item.total_brutoV, novo_item.total_liquido))
    tabela.executemany("INSERT INTO Estoque VALUES(?,?,?,?,?,?,?)",item )
    banco.commit()
    banco.close()


#######################Função para aumentar produto#######################
def aumentar_qtde(aumentar_nome, aumentar_qtde):
    banco = sqlite3.connect('Estoque.db')
    tabela = banco.cursor()
    nome = aumentar_nome.lower()

    #verificar se tem na tabela
    tabela.execute("SELECT nome FROM Estoque WHERE nome = ?", (nome,))
    if tabela.fetchone() == None:
        return print('Este produto não está no estoque. Tente novamente.')

    ### Adicionar quantidade
    tabela.execute("SELECT qtde FROM Estoque WHERE nome = ?", (nome,))
    itemA = tabela.fetchone()
    adicionar = aumentar_qtde
    nova_qtde = itemA[0] + adicionar
    tabela.execute("UPDATE Estoque SET qtde =? WHERE nome =?", (nova_qtde, nome))
    banco.commit()

#######################Função para diminuir produto#######################
def diminuir_qtde(diminuir_nome, diminuir_qtde ):
    banco = sqlite3.connect('Estoque.db')
    tabela = banco.cursor()
    nome = diminuir_nome.lower()

    # verificar se tem na tabela
    tabela.execute("SELECT nome FROM Estoque WHERE nome = ?", (nome,))
    if tabela.fetchone() == None:
        return print('Este produto não está no estoque. Tente novamente.')

    #### Remover quantidade
    tabela.execute("SELECT qtde FROM Estoque WHERE nome =?", (nome,))
    itemR = tabela.fetchone()
    remover = diminuir_qtde
    if remover > itemR[0]:
        return print('Quantidade a remover é maior que a quantidade existente no estoque.')
    nova_qtdeR = itemR[0] - remover

    tabela.execute("UPDATE Estoque SET qtde =? WHERE nome =?", (nova_qtdeR, nome))
    banco.commit()

#######################Função para remover produto#######################
def remover(remover_nome):
    banco = sqlite3.connect('Estoque.db')
    tabela = banco.cursor()
    nome = remover_nome.lower()
    # verificar se tem na tabela
    tabela.execute("SELECT nome FROM Estoque WHERE nome =?", (nome,))
    if tabela.fetchone() == None:
        return print('Este produto não está no estoque. Tente novamente.')

    #confirmar se quer excluir
    print(f"CONFIRMAÇÃO \n Produto : {nome}")
    confirma = input("DIGITE 'S' OU 'N' : ").lower()
    if confirma == "n":
           return print('VOLTANDO...\n')

    #exlusao
    tabela.execute("DELETE FROM Estoque WHERE nome =?", (nome,))
    banco.commit()
    print("Produto removido")

#######################Função para alterar valor do produto#######################
def editar_valor(editar_valor_nome, alterar_valorC, alterar_valorV):
    banco = sqlite3.connect('Estoque.db')
    tabela = banco.cursor()
    nome = editar_valor_nome.lower()

    # verificar se tem na tabela
    tabela.execute("SELECT nome FROM Estoque WHERE nome =?", (nome,))
    if tabela.fetchone() == None:
        return print('Este produto não está no estoque. Tente novamente.')

    #editar valor
    tabela.execute("UPDATE Estoque SET valor_compra, valor_venda =? WHERE nome =?", (alterar_valorC, alterar_valorV, nome))
    banco.commit()

#######################Função para pesquisar produto#######################
def pesquisa(pesquisa_nome):
    banco = sqlite3.connect('Estoque.db')
    tabela = banco.cursor()
    nome = pesquisa_nome.lower()
    tabela.execute("SELECT nome, qtde, total_brutoV FROM Estoque WHERE nome = ?", (nome,))
    produto = tabela.fetchone()

    # verificar se tem na tabela
    if produto is None:
        return print('Este produto não está no estoque.')

    print(f"Produto: {produto[0]}")
    print(f'Quantidade: {produto[1]} unidades')
    print(f'Valor total bruto: R$ {produto[2]:.2f}')

    #opcao se quer continuar
    opcao = input("Quer ver outro produto? 'S' ou 'N' ").lower()
    if opcao == "n":
            return
    elif opcao != "s":
            print('Opção inválida. Tente novamente.')

    banco.close()

#######################Função para verificar total de compra e total de venda#######################
def ver_valor():
    banco = sqlite3.connect('Estoque.db')
    tabela = banco.cursor()
    tabela.execute("SELECT SUM(total_brutoC), SUM(total_liquido) FROM Estoque")
    produto = tabela.fetchone()
    total_compra = produto[0]
    total_liquido = produto[1]
    banco.close()
    return total_compra, total_liquido

banco.close()
