import sqlite3
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from Teste_2 import inserir_produto, criar_tabela, editar_produto, visualizar_produtos

def alternar_barra_lateral(estado_barra, quadro_barra, criar_widgets_barra):
    estado_barra["expandido"] = not estado_barra["expandido"]
    if estado_barra["expandido"]:
        quadro_barra.config(width=200)
    else:
        quadro_barra.config(width=50)
    criar_widgets_barra()

def mostrar_conteudo_principal():
    for widget in quadro_conteudo.winfo_children():
        widget.destroy()
    label_conteudo = ttk.Label(quadro_conteudo, text="Conteúdo Principal", font=("Arial", 16))
    label_conteudo.pack(pady=20)

    botao_inserir = ttk.Button(quadro_conteudo, text="Inserir Produto", bootstyle=PRIMARY, command=mostrar_formulario_insercao)
    botao_inserir.pack(pady=10)

    botao_visualizar = ttk.Button(quadro_conteudo, text="Visualizar Produtos", bootstyle=INFO, command=mostrar_lista_produtos)
    botao_visualizar.pack(pady=10)

def mostrar_formulario_insercao():
    for widget in quadro_conteudo.winfo_children():
        widget.destroy()
    label_inserir = ttk.Label(quadro_conteudo, text="Inserir Novo Produto", font=("Arial", 16))
    label_inserir.pack(pady=20)

    nome_label = ttk.Label(quadro_conteudo, text="Nome do Produto:")
    nome_label.pack(pady=5, anchor=W)
    nome_entry = ttk.Entry(quadro_conteudo, width=30)
    nome_entry.pack(pady=10)

    preco_compra_label = ttk.Label(quadro_conteudo, text="Preço de Compra:")
    preco_compra_label.pack(pady=5, anchor=W)
    preco_compra_entry = ttk.Entry(quadro_conteudo, width=30)
    preco_compra_entry.pack(pady=10)

    preco_venda_label = ttk.Label(quadro_conteudo, text="Preço de Venda:")
    preco_venda_label.pack(pady=5, anchor=W)
    preco_venda_entry = ttk.Entry(quadro_conteudo, width=30)
    preco_venda_entry.pack(pady=10)

    quantidade_label = ttk.Label(quadro_conteudo, text="Quantidade:")
    quantidade_label.pack(pady=5, anchor=W)
    quantidade_entry = ttk.Entry(quadro_conteudo, width=30)
    quantidade_entry.pack(pady=10)

    def inserir():
        nome = nome_entry.get()
        preco_compra = float(preco_compra_entry.get())
        preco_venda = float(preco_venda_entry.get())
        quantidade = int(quantidade_entry.get())
        try:
            inserir_produto(nome, preco_compra, preco_venda, quantidade)
            mostrar_conteudo_principal()
        except ValueError as e:
            print(f"Erro ao inserir produto: {e}")

    botao_inserir = ttk.Button(quadro_conteudo, text="Salvar", bootstyle=PRIMARY, command=inserir)
    botao_inserir.pack(pady=10)

    botao_voltar = ttk.Button(quadro_conteudo, text="Voltar", bootstyle=SECONDARY, command=mostrar_conteudo_principal)
    botao_voltar.pack(pady=10)

def mostrar_lista_produtos():
    for widget in quadro_conteudo.winfo_children():
        widget.destroy()

    label_lista = ttk.Label(quadro_conteudo, text="Lista de Produtos", font=("Arial", 16))
    label_lista.pack(pady=20)

    produtos = visualizar_produtos()
    for produto in produtos:
        label_produto = ttk.Label(quadro_conteudo, text=f"{produto[1]} - Preço Compra: {produto[2]} - Preço Venda: {produto[3]} - Quantidade: {produto[4]}", font=("Arial", 12))
        label_produto.pack(pady=5)

    botao_editar = ttk.Button(quadro_conteudo, text="Editar Produto", bootstyle=PRIMARY, command=mostrar_formulario_edicao)
    botao_editar.pack(pady=10)

    botao_voltar = ttk.Button(quadro_conteudo, text="Voltar", bootstyle=SECONDARY, command=mostrar_conteudo_principal)
    botao_voltar.pack(pady=10)

def mostrar_formulario_edicao():
    for widget in quadro_conteudo.winfo_children():
        widget.destroy()
    label_editar = ttk.Label(quadro_conteudo, text="Editar Produto", font=("Arial", 16))
    label_editar.pack(pady=20)

    id_label = ttk.Label(quadro_conteudo, text="ID do Produto:")
    id_label.pack(pady=5, anchor=W)
    id_entry = ttk.Entry(quadro_conteudo, width=30)
    id_entry.pack(pady=10)

    nome_label = ttk.Label(quadro_conteudo, text="Nome do Produto:")
    nome_label.pack(pady=5, anchor=W)
    nome_entry = ttk.Entry(quadro_conteudo, width=30)
    nome_entry.pack(pady=10)

    preco_compra_label = ttk.Label(quadro_conteudo, text="Preço de Compra:")
    preco_compra_label.pack(pady=5, anchor=W)
    preco_compra_entry = ttk.Entry(quadro_conteudo, width=30)
    preco_compra_entry.pack(pady=10)

    preco_venda_label = ttk.Label(quadro_conteudo, text="Preço de Venda:")
    preco_venda_label.pack(pady=5, anchor=W)
    preco_venda_entry = ttk.Entry(quadro_conteudo, width=30)
    preco_venda_entry.pack(pady=10)

    quantidade_label = ttk.Label(quadro_conteudo, text="Quantidade:")
    quantidade_label.pack(pady=5, anchor=W)
    quantidade_entry = ttk.Entry(quadro_conteudo, width=30)
    quantidade_entry.pack(pady=10)

    def editar():
        id_produto = int(id_entry.get())
        nome = nome_entry.get()
        preco_compra = float(preco_compra_entry.get())
        preco_venda = float(preco_venda_entry.get())
        quantidade = int(quantidade_entry.get())
        try:
            editar_produto(id_produto, nome, preco_compra, preco_venda, quantidade)
            mostrar_conteudo_principal()
        except ValueError as e:
            print(f"Erro ao editar produto: {e}")

    botao_editar = ttk.Button(quadro_conteudo, text="Salvar Alterações", bootstyle=PRIMARY, command=editar)
    botao_editar.pack(pady=10)

    botao_voltar = ttk.Button(quadro_conteudo, text="Voltar", bootstyle=SECONDARY, command=mostrar_conteudo_principal)
    botao_voltar.pack(pady=10)

def criar_widgets_barra(quadro_barra, estado_barra, comando_alternar):
    for widget in quadro_barra.winfo_children():
        widget.destroy()
    botao_alternar = ttk.Button(quadro_barra, text="☰", bootstyle=SECONDARY, command=comando_alternar)
    botao_alternar.pack(anchor=NW, pady=10, padx=10)

    def mostrar_conteudo(nome_conteudo):
        for widget in quadro_conteudo.winfo_children():
            widget.destroy()
        if nome_conteudo == "Início":
            mostrar_conteudo_principal()
        elif nome_conteudo == "Inserir Produto":
            mostrar_formulario_insercao()
        elif nome_conteudo == "Visualizar Produtos":
            mostrar_lista_produtos()

    itens_menu = [
        ("Início", "🏠", "Início"),
        ("Inserir Produto", "➕", "Inserir Produto"),
        ("Visualizar Produtos", "🔍", "Visualizar Produtos")
    ]

    if estado_barra["expandido"]:
        for texto, icone, nome_conteudo in itens_menu:
            botao = ttk.Button(quadro_barra, text=f"{icone} {texto}", bootstyle=LINK, compound=LEFT, command=lambda nome=nome_conteudo: mostrar_conteudo(nome))
            botao.pack(anchor=W, fill=X, padx=10, pady=5)
    else:
        for texto, icone, nome_conteudo in itens_menu:
            botao = ttk.Button(quadro_barra, text=icone, bootstyle=LINK, compound=LEFT, width=4, command=lambda nome=nome_conteudo: mostrar_conteudo(nome))
            botao.pack(anchor=W, padx=10, pady=5)

def principal():
    global quadro_conteudo

    aplicativo = ttk.Window(themename="darkly")
    aplicativo.title("Menu de Barra Lateral")
    aplicativo.geometry("600x400")

    estado_barra = {"expandido": True}

    quadro_principal = ttk.Frame(aplicativo)
    quadro_principal.pack(fill=BOTH, expand=YES)

    quadro_barra = ttk.Frame(quadro_principal, width=200, bootstyle=PRIMARY)
    quadro_barra.pack(side=LEFT, fill=Y)
    quadro_barra.pack_propagate(False)

    quadro_conteudo = ttk.Frame(quadro_principal)
    quadro_conteudo.pack(side=RIGHT, fill=BOTH, expand=YES)

    comando_alternar = lambda: alternar_barra_lateral(estado_barra, quadro_barra, lambda: criar_widgets_barra(quadro_barra, estado_barra, comando_alternar))

    criar_widgets_barra(quadro_barra, estado_barra, comando_alternar)

    criar_tabela()  # Criação da tabela antes de iniciar o aplicativo

    mostrar_conteudo_principal()

    aplicativo.mainloop()

if __name__ == "__main__":
    principal()