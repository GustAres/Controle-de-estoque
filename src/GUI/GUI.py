import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import Toplevel, messagebox
from src.controllers.gestao import *


def alternar_barra_lateral(estado_barra, quadro_barra, criar_widgets_barra):
    # Alterna a barra lateral entre os estados expandido e recolhido.
    estado_barra["expandido"] = not estado_barra["expandido"]

    # Atualiza a largura da barra
    if (estado_barra["expandido"]):
        quadro_barra.config(width=200)
    else:
        quadro_barra.config(width=60)

    # Atualiza os widgets da barra
    criar_widgets_barra()


def mostrar_conteudo_principal():
    for widget in quadro_conteudo.winfo_children():
        widget.destroy()
    label_conteudo = ttk.Label(quadro_conteudo, text="Bem Vindo A NuEstoque!")
    label_conteudo.pack(pady=30)


def mostrar_formulario_cadastro():
    for widget in quadro_conteudo.winfo_children():
        widget.destroy()
    label_cadastro = ttk.Label(quadro_conteudo, text="Cadastro De Um Novo Produto!")
    label_cadastro.pack(pady=30)

    nome_label = ttk.Label(quadro_conteudo, text="Nome do Produto")
    nome_label.pack(pady=15)
    nome_entry = ttk.Entry(quadro_conteudo, width=30, bootstyle="INFO")
    nome_entry.pack(pady=0)

    preco_compra_label = ttk.Label(quadro_conteudo, text="Preço de Compra")
    preco_compra_label.pack(pady=15)
    preco_compra_entry = ttk.Entry(quadro_conteudo, width=30, bootstyle="INFO")
    preco_compra_entry.pack(pady=0)

    preco_venda_label = ttk.Label(quadro_conteudo, text="Preço de Venda")
    preco_venda_label.pack(pady=15)
    preco_venda_entry = ttk.Entry(quadro_conteudo, width=30, bootstyle="INFO")
    preco_venda_entry.pack(pady=0)

    quantidade_label = ttk.Label(quadro_conteudo, text="Quantidade")
    quantidade_label.pack(pady=15)
    quantidade_entry = ttk.Entry(quadro_conteudo, width=30, bootstyle="INFO")
    quantidade_entry.pack(pady=0)

    def inserir_produto():
        try:
            nome = nome_entry.get()
            preco_compra = float(preco_compra_entry.get())
            preco_venda = float(preco_venda_entry.get())
            quantidade = int(quantidade_entry.get())
            inserir(cadastro_nome=nome, cadastro_valorC=preco_compra, cadastro_valorV=preco_venda, cadastro_qtde=quantidade, aplicativo=aplicativo)
            # Limpa as caixas de texto após inserir o produto
            nome_entry.delete(0, 'end')
            preco_compra_entry.delete(0, 'end')
            preco_venda_entry.delete(0, 'end')
            quantidade_entry.delete(0, 'end')

        except ValueError as e:
            mostrar_pop_up("Erro", f"Erro no valor inserido: {str(e)}", "danger", aplicativo)
        except Exception as e:
            mostrar_pop_up("Erro", f"Um erro inesperado ocorreu: {str(e)}", "danger", aplicativo)

    botao_inserir = ttk.Button(quadro_conteudo, text="Salvar", bootstyle="INFO", command=inserir_produto)
    botao_inserir.pack(pady=20)

    botao_voltar = ttk.Button(quadro_conteudo, text="Voltar", bootstyle="DANGER", command=mostrar_conteudo_principal)
    botao_voltar.pack(pady=20)

def mostrar_formulario_editar_quantidade():
    for widget in quadro_conteudo.winfo_children():
        widget.destroy()
    label_editar_quantidade = ttk.Label(quadro_conteudo, text="Editar Quantidade Produto")
    label_editar_quantidade.pack(pady=30)

def criar_widgets_barra(quadro_barra, estado_barra, comando_alternar):
    # Limpa os widgets existentes
    for widget in quadro_barra.winfo_children():
        widget.destroy()

    # Readiciona o botão de alternância
    botao_alternar = ttk.Button(quadro_barra, text="☰", bootstyle=INFO, command=comando_alternar, width=4)
    botao_alternar.pack(anchor=NW, pady=10, padx=10)

    def mostrar_conteudo(nome_conteudo):
        for widget in quadro_conteudo.winfo_children():
            widget.destroy()
        if nome_conteudo == "Início":
            mostrar_conteudo_principal()
        if nome_conteudo == "Cadastrar Produto":
            mostrar_formulario_cadastro()
        if nome_conteudo == "Editar Quantidade":
            mostrar_formulario_editar_quantidade()
        # if nome_conteudo == "Lista De Produtos":
        # mostrar_formulario_lista
        # if nome_conteudo == "Editar Valores":
        # mostrar_formulario_editar_valores
        # if nome_conteudo == "Remover Produto"
        # mostrar_formulario_remover_produto

    itens_menu = [
        ("Início", "🏠", "Início"),
        ("Cadastrar Produto", "📦", "Cadastrar Produto"),
        ("Editar Quantidade", "📝", "Editar Quantidade"),
        ("Lista De Produtos", "🔍", "Lista De Produtos"),
        ("Editar Valores", "💲", "Editar Valores"),
        ("Remover Produtos", "❌", "Remover Produtos")
    ]

    if estado_barra["expandido"]:
        # Menu expandido com texto e ícones
        for texto, icone, nome_conteudo in itens_menu:
            botao = ttk.Button(quadro_barra, text=f"{icone} {texto}", bootstyle=INFO, compound=LEFT, command=lambda nome=nome_conteudo: mostrar_conteudo(nome))
            botao.pack(anchor=W, fill=X, padx=10, pady=5)
    else:
        # Menu recolhido apenas com ícones e tamanho fixo
        for texto, icone, nome_conteudo in itens_menu:
            botao = ttk.Button(quadro_barra, text=icone, bootstyle=INFO, compound=LEFT, width=8, command=lambda nome=nome_conteudo: mostrar_conteudo(nome))
            botao.pack(anchor=W, padx=10, pady=5)


def principal():
    global quadro_conteudo, aplicativo

    aplicativo = ttk.Window(themename="cyborg")
    aplicativo.title("NuEstoque")
    aplicativo.geometry("900x500")

    # Configura a fonte padrão para o aplicativo
    style = ttk.Style()
    style.configure('.', font=('Graphik', 12))

    # Estado da barra lateral
    estado_barra = {"expandido": True}

    # Quadro Principal
    quadro_principal = ttk.Frame(aplicativo)
    quadro_principal.pack(fill=BOTH, expand=YES)

    # Barra Lateral
    quadro_barra = ttk.Frame(quadro_principal, width=200, bootstyle=DARK)
    quadro_barra.pack(side=LEFT, fill=Y)
    quadro_barra.pack_propagate(False)

    # Quadro de Conteúdo
    quadro_conteudo = ttk.Frame(quadro_principal)
    quadro_conteudo.pack(side=RIGHT, fill=BOTH, expand=YES)

    # Comando do botão de alternância
    comando_alternar = lambda: alternar_barra_lateral(estado_barra, quadro_barra, lambda: criar_widgets_barra(quadro_barra, estado_barra, comando_alternar))

    # Widgets iniciais da barra lateral
    criar_widgets_barra(quadro_barra, estado_barra, comando_alternar)

    mostrar_conteudo_principal()

    aplicativo.mainloop()


if __name__ == "__main__":
    principal()