from dataclasses import dataclass
import sqlite3
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import Toplevel
from tkinter import *



@dataclass
class RegistroItem:
    nome: str = ""
    qtde: int = 0
    valor_compra: float = 0.0
    valor_venda: float = 0.0
    total_brutoC: float = 0.0
    total_brutoV: float = 0.0
    total_liquido: float = 0.0



####################### Função para criar produto e inserir no estoque #######################
def inserir(cadastro_nome, cadastro_qtde, cadastro_valorC, cadastro_valorV, aplicativo):
    item = []
    try:
        banco = sqlite3.connect('Estoque.db')
        tabela = banco.cursor()
        nome = cadastro_nome.lower()

        tabela.execute(" CREATE TABLE IF NOT EXISTS Estoque (nome VARCHAR, qtde INT NOT NULL,valor_compra DOUBLE NOT NULL,valor_venda DOUBLE NOT NULL,total_brutoC DOUBLE GENERATED ALWAYS AS (qtde * valor_compra) STORED,total_brutoV DOUBLE GENERATED ALWAYS AS (qtde * valor_venda) STORED,total_liquido DOUBLE GENERATED ALWAYS AS (total_brutoV - total_brutoC) STORED )")


        # Verificando se já existe
        tabela.execute("SELECT nome FROM Estoque WHERE nome = ?", (nome,))
        if tabela.fetchone():
            mostrar_pop_up("Erro", "Produto já cadastrado no estoque", "danger", aplicativo)
            return

        qtde = cadastro_qtde
        valor_compra = cadastro_valorC
        valor_venda = cadastro_valorV


        novo_item = RegistroItem(nome, qtde, valor_compra, valor_venda)
        item.append((novo_item.nome, novo_item.qtde, novo_item.valor_compra, novo_item.valor_venda))
        tabela.executemany("INSERT INTO Estoque VALUES(?,?,?,?)", item)
        banco.commit()
        mostrar_pop_up("Sucesso", "Produto inserido com sucesso!", "info", aplicativo)
    except Exception as e:
        mostrar_pop_up("Erro", f"Um erro ocorreu: {str(e)}", "danger", aplicativo)
    finally:
        banco.close()


####################### Função de Pop-Up #######################
def mostrar_pop_up(titulo, mensagem, estilo, aplicativo):
    pop_up = Toplevel(aplicativo)
    pop_up.title(titulo)
    pop_up.geometry("300x150")
    pop_up.grab_set()  # Faz o pop-up modal

    mensagem_label = ttk.Label(pop_up, text=mensagem, bootstyle=estilo)
    mensagem_label.pack(pady=30, padx=10)

    botao_ok = ttk.Button(pop_up, text="OK", bootstyle=estilo, command=pop_up.destroy)
    botao_ok.pack(pady=10)


####################### Função para aumentar produto #######################
def aumentar_qtde(aumentar_nome, aumentar_qtde, aplicativo):
    try:
        banco = sqlite3.connect('Estoque.db')
        tabela = banco.cursor()
        nome = aumentar_nome.lower()

        # Verificar se tem na tabela
        tabela.execute("SELECT nome FROM Estoque WHERE nome = ?", (nome,))
        if tabela.fetchone() is None:
            mostrar_pop_up("Erro", "Este produto não está no estoque. Tente novamente.", "danger", aplicativo)
            return

        # Adicionar quantidade
        tabela.execute("SELECT qtde FROM Estoque WHERE nome = ?", (nome,))
        itemA = tabela.fetchone()
        adicionar = aumentar_qtde
        nova_qtde = itemA[0] + adicionar
        tabela.execute("UPDATE Estoque SET qtde =? WHERE nome =?", (nova_qtde, nome))
        banco.commit()
        mostrar_pop_up("Sucesso", "Quantidade aumentada com sucesso!", "info", aplicativo)
    except Exception as e:
        mostrar_pop_up("Erro", f"Erro ao aumentar quantidade: {str(e)}", "danger", aplicativo)
    finally:
        banco.close()


####################### Função para diminuir produto #######################
def diminuir_qtde(diminuir_nome, diminuir_qtde, aplicativo):
    try:
        banco = sqlite3.connect('Estoque.db')
        tabela = banco.cursor()
        nome = diminuir_nome.lower()

        # Verificar se tem na tabela
        tabela.execute("SELECT nome FROM Estoque WHERE nome = ?", (nome,))
        if tabela.fetchone() is None:
            mostrar_pop_up("Erro", "Este produto não está no estoque. Tente novamente.", "danger", aplicativo)
            return

        # Remover quantidade
        tabela.execute("SELECT qtde FROM Estoque WHERE nome =?", (nome,))
        itemR = tabela.fetchone()
        remover = diminuir_qtde
        if remover > itemR[0]:
            mostrar_pop_up("Erro", "Quantidade a remover é maior que a quantidade existente no estoque.", "danger", aplicativo)
            return
        nova_qtdeR = itemR[0] - remover
        tabela.execute("UPDATE Estoque SET qtde =? WHERE nome =?", (nova_qtdeR, nome))
        banco.commit()
        mostrar_pop_up("Sucesso", "Quantidade diminuída com sucesso!", "info", aplicativo)
    except Exception as e:
        mostrar_pop_up("Erro", f"Erro ao diminuir quantidade: {str(e)}", "danger", aplicativo)
    finally:
        banco.close()


####################### Função para remover produto #######################
def remover(remover_nome, aplicativo):
    try:
        banco = sqlite3.connect('Estoque.db')
        tabela = banco.cursor()
        nome_remove = remover_nome.lower()

        # Verificar se tem na tabela
        tabela.execute("SELECT nome FROM Estoque WHERE nome =?", (nome_remove,))
        if tabela.fetchone() is None:
            mostrar_pop_up("Erro", "Este produto não está no estoque. Tente novamente.", "danger", aplicativo)
            return

        # Exclusão
        tabela.execute("DELETE FROM Estoque WHERE nome =?", (nome_remove,))
        banco.commit()
        mostrar_pop_up("Sucesso", "Produto removido com sucesso!", "info", aplicativo)
    except Exception as e:
        mostrar_pop_up("Erro", f"Erro ao remover produto: {str(e)}", "danger", aplicativo)
    finally:
        banco.close()


####################### Função para alterar valor de compra do produto #######################
def editar_valor_compra(editar_valor_nome, alterar_valorC, aplicativo):
    try:
        banco = sqlite3.connect('Estoque.db')
        tabela = banco.cursor()
        nome = editar_valor_nome.lower()


    # Verificar se tem na tabela
        tabela.execute("SELECT nome FROM Estoque WHERE nome =?", (nome,))
        if tabela.fetchone() is None:
            mostrar_pop_up("Erro", "Este produto não está no estoque. Tente novamente.", "danger", aplicativo)
            return

    # Editar valor
        tabela.execute("UPDATE Estoque SET valor_compra = ? WHERE nome = ?", (alterar_valorC, nome))
        banco.commit()
        mostrar_pop_up("Sucesso", "Valores alterados com sucesso!", "info", aplicativo)
    except Exception as e:
        mostrar_pop_up("Erro", f"Erro ao editar valores: {str(e)}", "danger", aplicativo)
    finally:
        banco.close()


####################### Função para alterar valor de venda do produto #######################
def editar_valor_venda(editar_valor_nome,alterar_valorV, aplicativo):
    try:
        banco = sqlite3.connect('Estoque.db')
        tabela = banco.cursor()
        nome = editar_valor_nome.lower()
        valor_novo = alterar_valorV
        # Verificar se tem na tabela
        tabela.execute("SELECT nome FROM Estoque WHERE nome =?", (nome,))
        if tabela.fetchone() is None:
            mostrar_pop_up("Erro", "Este produto não está no estoque. Tente novamente.", "danger", aplicativo)
            return

    # Editar valor
        tabela.execute("UPDATE Estoque SET valor_venda = ? WHERE nome = ?",(valor_novo, nome))
        banco.commit()
        mostrar_pop_up("Sucesso", "Valores alterados com sucesso!", "info", aplicativo)
    except Exception as e:
        mostrar_pop_up("Erro", f"Erro ao editar valores: {str(e)}", "danger", aplicativo)
    finally:
        banco.close()


####################### Função para alterar o nome do produto #######################
def editar_nome(nome,editar_nome, aplicativo):
    try:
        banco = sqlite3.connect('Estoque.db')
        tabela = banco.cursor()
        nome_selecionado = nome.lower()
        nome_editado = editar_nome.lower()

        # Verificar se tem na tabela
        tabela.execute("SELECT nome FROM Estoque WHERE nome =?", (nome_selecionado,))
        if tabela.fetchone() is None:
            mostrar_pop_up("Erro", "Este produto não está no estoque. Tente novamente.", "danger", aplicativo)
            return
        # Verificar se o novo nome já existe na tabela
        tabela.execute("SELECT nome FROM Estoque WHERE nome =?", (nome_editado,))
        if tabela.fetchone() is not None:
            mostrar_pop_up("Erro", "O novo nome já está em uso. Tente novamente.", "danger", aplicativo)
            return

        # Editar valor
        tabela.execute("UPDATE Estoque SET nome = ? WHERE nome = ?", (nome_editado, nome_selecionado))
        banco.commit()
        mostrar_pop_up("Sucesso", "Valores alterados com sucesso!", "info", aplicativo)

        # Atualizar a interface com o novo nome
        aplicativo.event_generate("<<NomeProdutoAtualizado>>", when="tail")
    except Exception as e:
        mostrar_pop_up("Erro", f"Erro ao editar valores: {str(e)}", "danger", aplicativo)
    finally:
        banco.close()        



####################### Função para para pesquisar o produto #######################
def pesquisa(pesquisa_nome, aplicativo):
    try:
        banco = sqlite3.connect('Estoque.db')
        tabela = banco.cursor()
        nome = pesquisa_nome.lower()
        tabela.execute("SELECT * FROM Estoque WHERE nome = ?", (nome,))
        produto = tabela.fetchone()

        # Verificar se tem na tabela
        if produto is None:
            return
        return produto
    except Exception as e:
        mostrar_pop_up("Erro", f"Erro na pesquisa: {str(e)}", "danger", aplicativo)
    finally:
        banco.close()

####################### Função para verificar total de compra e total de venda #######################
def ver_valor(aplicativo):
    try:
        banco = sqlite3.connect('Estoque.db')
        tabela = banco.cursor()
        tabela.execute("SELECT SUM(total_brutoC), SUM(total_liquido) FROM Estoque")
        produto = tabela.fetchone()
        total_compra = produto[0]
        total_liquido = produto[1]
        return total_compra, total_liquido
    except Exception as e:
        mostrar_pop_up("Erro", f"Erro ao obter valores: {str(e)}", "danger", aplicativo)
    finally:
        banco.close()
