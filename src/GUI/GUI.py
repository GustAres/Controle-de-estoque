
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from src.controllers.gestao import *

def alternar_barra_lateral(estado_barra, quadro_barra, criar_widgets_barra):
    """Alterna a barra lateral entre os estados expandido e recolhido."""
    estado_barra["expandido"] = not estado_barra["expandido"]

    # Atualiza a largura da barra
    if estado_barra["expandido"]:
        quadro_barra.config(width=200)
    else:
        quadro_barra.config(width=60)

    # Atualiza os widgets da barra
    criar_widgets_barra()

def mostrar_conteudo_principal():
    for widget in quadro_conteudo.winfo_children():
        widget.destroy()
    label_conteudo = ttk.Label(quadro_conteudo, text="Bem Vindo A NuEstoque!")
    label_conteudo.pack(pady=15)

    botao_cadastrar = ttk.Label(quadro_conteudo, text="Cadastrar Produto", bootstyle=INFO, commmand=mostrar_formulario_cadastro)
    botao_cadastrar.pack(pady=10)

def mostrar_formulario_cadastro():
    for widget in  quadro_conteudo.winfo_children():
        widget.destroy()
    label_cadastro = ttk.Label(quadro_conteudo, text="Cadastro De Um Novo Produto!")
    label_cadastro.pack(pady=15)


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
        #if nome_conteudo == "Editar Quantidade":
            #mostrar_formulario_editar_quantidade
        #if nome_conteudo == "Pesquisar":
            #mostrar_formulario_pesquisar
        #if nome_conteudo == "Editar Valores":
            #mostrar_formulario_editar_valores
        #if nome_conteudo == "Remover Produto"
            #mostrar_formulario_remover_produto

    itens_menu = [
        ("Início", "🏠", "Início"),
        ("Cadastrar Produto", "📦", "Cadastrar Produto"),
        ("Editar Quantidade", "📝", "Editar Quantidade"),
        ("Pesquisar", "🔍", "Pesquisar"),
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
    global quadro_conteudo

    aplicativo = ttk.Window(themename="cyborg")
    aplicativo.title("NuEstoque")
    aplicativo.geometry("900x500")

    #Configura a fonte padrão para o aplicativo
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
