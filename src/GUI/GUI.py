from src.controllers.gestao import *



def alternar_barra_lateral(estado_barra, quadro_barra, criar_widgets_barra):
    estado_barra["expandido"] = not estado_barra["expandido"]
    if estado_barra["expandido"]:
        quadro_barra.config(width=200)
    else:
        quadro_barra.config(width=60)
    criar_widgets_barra()

def mostrar_conteudo_principal():
    for widget in quadro_conteudo.winfo_children():
        widget.destroy()
    label_conteudo = ttk.Label(quadro_conteudo, text="BEM VINDO A NUESTOQUE!")
    label_conteudo.pack(pady=25)

def mostrar_formulario_cadastro():
    for widget in quadro_conteudo.winfo_children():
        widget.destroy()
    label_cadastro = ttk.Label(quadro_conteudo, text="CADASTRO DE UM NOVO PRODUTO!")
    label_cadastro.pack(pady=25)
    label_editar_produto = ttk.Label(quadro_conteudo, text="Por favor insira as informações do produto")
    label_editar_produto.pack(pady=0)
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
            nome_entry.delete(0, 'end')
            preco_compra_entry.delete(0, 'end')
            preco_venda_entry.delete(0, 'end')
            quantidade_entry.delete(0, 'end')
        except ValueError as e:
            mostrar_pop_up("Erro", f"Erro no valor inserido: {str(e)}", "danger", aplicativo)
        except Exception as e:
            mostrar_pop_up("Erro", f"Um erro inesperado ocorreu: {str(e)}", "danger", aplicativo)
    botao_inserir = ttk.Button(quadro_conteudo, text="Salvar", bootstyle="INFO", command=inserir_produto)
    botao_inserir.pack(pady=10)
    botao_voltar = ttk.Button(quadro_conteudo, text="Voltar", bootstyle="DANGER", command=mostrar_conteudo_principal)
    botao_voltar.pack(pady=0)

def mostrar_formulario_editar_produto():
    for widget in quadro_conteudo.winfo_children():
        widget.destroy()
    label_editar_produto = ttk.Label(quadro_conteudo, text="EDITAR UM PRODUTO!")
    label_editar_produto.pack(pady=25)
    label_editar_produto = ttk.Label(quadro_conteudo, text="Por favor insira o nome do produto")
    label_editar_produto.pack(pady=0)
    nome_label = ttk.Label(quadro_conteudo, text="Nome do Produto")
    nome_label.pack(pady=15)
    nome_entry = ttk.Entry(quadro_conteudo, width=30, bootstyle="INFO")
    nome_entry.pack(pady=0)
    def selecionar_produto():
        try:
            nome = nome_entry.get()
            produto = pesquisa(pesquisa_nome=nome, aplicativo=aplicativo)
            nome_entry.delete(0, 'end')
            if produto:
                mostrar_opcoes_editar_produto(produto)
            else:
                mostrar_pop_up("Erro", "Produto não encontrado.", "danger", aplicativo)
        except ValueError as e:
            mostrar_pop_up("Erro", f"Erro no valor inserido: {str(e)}", "danger", aplicativo)
        except Exception as e:
            mostrar_pop_up("Erro", f"Um erro inesperado ocorreu: {str(e)}", "danger", aplicativo)
    botao_selecionar = ttk.Button(quadro_conteudo, text="Procurar", bootstyle="INFO", command=selecionar_produto)
    botao_selecionar.pack(pady=10)
    botao_voltar = ttk.Button(quadro_conteudo, text="Voltar", bootstyle="DANGER", command=mostrar_conteudo_principal)
    botao_voltar.pack(pady=0)

def mostrar_opcoes_editar_produto(produto):
    for widget in quadro_conteudo.winfo_children():
        widget.destroy()
    label_opcoes = ttk.Label(quadro_conteudo, text=f"EDITAR PRODUTO: {produto[0]}")
    label_opcoes.pack(pady=25)
    botao_mudar_nome = ttk.Button(quadro_conteudo, text="Mudar Nome", bootstyle="INFO", command=lambda: mostrar_formulario_mudar_nome(produto[0]))
    botao_mudar_nome.pack(pady=10)
    botao_adicionar = ttk.Button(quadro_conteudo, text="Adicionar Quantidade", bootstyle="INFO", command=lambda: mostrar_formulario_adicionar_quantidade(produto[0]))
    botao_adicionar.pack(pady=10)
    botao_subtrair = ttk.Button(quadro_conteudo, text="Subtrair Quantidade", bootstyle="INFO", command=lambda: mostrar_formulario_subtrair_quantidade(produto[0]))
    botao_subtrair.pack(pady=10)
    botao_mudar_preco_compra = ttk.Button(quadro_conteudo, text="Mudar Preço de Compra", bootstyle="INFO", command=lambda: mostrar_formulario_mudar_preco_compra(produto[0]))
    botao_mudar_preco_compra.pack(pady=10)
    botao_mudar_preco_venda = ttk.Button(quadro_conteudo, text="Mudar Preço de Venda", bootstyle="INFO", command=lambda: mostrar_formulario_mudar_preco_venda(produto[0]))
    botao_mudar_preco_venda.pack(pady=10)
    botao_voltar = ttk.Button(quadro_conteudo, text="Voltar", bootstyle="DANGER", command=mostrar_formulario_editar_produto)
    botao_voltar.pack(pady=10)

def mostrar_formulario_adicionar_quantidade(produto_nome):
    for widget in quadro_conteudo.winfo_children():
        widget.destroy()
    label_adicionar_quantidade = ttk.Label(quadro_conteudo, text=f"Adicionar Quantidade Ao Produto: {produto_nome}")
    label_adicionar_quantidade.pack(pady=30)
    quantidade_label = ttk.Label(quadro_conteudo, text="Quantidade a Adicionar")
    quantidade_label.pack(pady=10)
    quantidade_entry = ttk.Entry(quadro_conteudo, width=30, bootstyle="INFO")
    quantidade_entry.pack(pady=5)
    def adicionar_quantidade():
        try:
            quantidade = int(quantidade_entry.get())
            aumentar_qtde(aumentar_nome=produto_nome, aumentar_qtde=quantidade, aplicativo=aplicativo)
            quantidade_entry.delete(0, 'end')
        except ValueError as e:
            mostrar_pop_up("Erro", f"Erro no valor inserido: {str(e)}", "danger", aplicativo)
        except Exception as e:
            mostrar_pop_up("Erro", f"Um erro inesperado ocorreu: {str(e)}", "danger", aplicativo)
    botao_confirmar = ttk.Button(quadro_conteudo, text="Confirmar", bootstyle="INFO", command=adicionar_quantidade)
    botao_confirmar.pack(pady=10)
    botao_voltar = ttk.Button(quadro_conteudo, text="Voltar", bootstyle="DANGER", command=lambda: mostrar_opcoes_editar_produto((produto_nome,)))
    botao_voltar.pack(pady=10)

def mostrar_formulario_subtrair_quantidade(produto_nome):
    for widget in quadro_conteudo.winfo_children():
        widget.destroy()
    label_subtrair_quantidade = ttk.Label(quadro_conteudo, text=f"Subtrair Quantidade do Produto: {produto_nome}")
    label_subtrair_quantidade.pack(pady=30)
    quantidade_label = ttk.Label(quadro_conteudo, text="Quantidade a Subtrair")
    quantidade_label.pack(pady=10)
    quantidade_entry = ttk.Entry(quadro_conteudo, width=30, bootstyle="INFO")
    quantidade_entry.pack(pady=5)
    def subtrair_quantidade():
        try:
            quantidade = int(quantidade_entry.get())
            diminuir_qtde(diminuir_nome=produto_nome, diminuir_qtde=quantidade, aplicativo=aplicativo)
            quantidade_entry.delete(0, 'end')
        except ValueError as e:
            mostrar_pop_up("Erro", f"Erro no valor inserido: {str(e)}", "danger", aplicativo)
        except Exception as e:
            mostrar_pop_up("Erro", f"Um erro inesperado ocorreu: {str(e)}", "danger", aplicativo)
    botao_confirmar = ttk.Button(quadro_conteudo, text="Confirmar", bootstyle="INFO", command=subtrair_quantidade)
    botao_confirmar.pack(pady=10)
    botao_voltar = ttk.Button(quadro_conteudo, text="Voltar", bootstyle="DANGER", command=lambda: mostrar_opcoes_editar_produto((produto_nome,)))
    botao_voltar.pack(pady=10)

def mostrar_formulario_mudar_nome(produto_nome):
    for widget in quadro_conteudo.winfo_children():
        widget.destroy()
    label_mudar_nome = ttk.Label(quadro_conteudo, text=f"Mudar Nome do Produto: {produto_nome}")
    label_mudar_nome.pack(pady=30)
    novo_nome_label = ttk.Label(quadro_conteudo, text="Novo Nome")
    novo_nome_label.pack(pady=10)
    novo_nome_entry = ttk.Entry(quadro_conteudo, width=30, bootstyle="INFO")
    novo_nome_entry.pack(pady=5)
    def mudar_nome():
        try:
            novo_nome = novo_nome_entry.get()
            editar_nome(produto_nome, novo_nome, aplicativo=aplicativo)
            novo_nome_entry.delete(0, 'end')
        except ValueError as e:
            mostrar_pop_up("Erro", f"Erro no valor inserido: {str(e)}", "danger", aplicativo)
        except Exception as e:
            mostrar_pop_up("Erro", f"Um erro inesperado ocorreu: {str(e)}", "danger", aplicativo)
    botao_confirmar = ttk.Button(quadro_conteudo, text="Confirmar", bootstyle="INFO", command=mudar_nome)
    botao_confirmar.pack(pady=10)
    botao_voltar = ttk.Button(quadro_conteudo, text="Voltar", bootstyle="DANGER", command=lambda: mostrar_opcoes_editar_produto((produto_nome,)))
    botao_voltar.pack(pady=10)

def mostrar_formulario_mudar_preco_compra(produto_nome):
    for widget in quadro_conteudo.winfo_children():
        widget.destroy()
    label_mudar_preco = ttk.Label(quadro_conteudo, text=f"Mudar Preço de compra do Produto: {produto_nome}")
    label_mudar_preco.pack(pady=30)
    novo_preco_label = ttk.Label(quadro_conteudo, text=f"Novo Preço de compra do Produto")
    novo_preco_label.pack(pady=10)
    novo_preco_entry = ttk.Entry(quadro_conteudo, width=30, bootstyle="INFO")
    novo_preco_entry.pack(pady=5)
    def mudar_preco_compra():
        try:
            novo_preco = float(novo_preco_entry.get())
            editar_valor_compra(editar_valor_nome=produto_nome, alterar_valorC=novo_preco, aplicativo=aplicativo)
            novo_preco_entry.delete(0, 'end')
        except ValueError as e:
            mostrar_pop_up("Erro", f"Erro no valor inserido: {str(e)}", "danger", aplicativo)
        except Exception as e:
            mostrar_pop_up("Erro", f"Um erro inesperado ocorreu: {str(e)}", "danger", aplicativo)
    botao_confirmar = ttk.Button(quadro_conteudo, text="Confirmar", bootstyle="INFO", command=mudar_preco_compra)
    botao_confirmar.pack(pady=10)
    botao_voltar = ttk.Button(quadro_conteudo, text="Voltar", bootstyle="DANGER", command=lambda: mostrar_opcoes_editar_produto((produto_nome,)))
    botao_voltar.pack(pady=10)

def mostrar_formulario_mudar_preco_venda(produto_nome):
    for widget in quadro_conteudo.winfo_children():
        widget.destroy()
    label_mudar_preco = ttk.Label(quadro_conteudo, text=f"Mudar Preço de venda do Produto: {produto_nome}")
    label_mudar_preco.pack(pady=30)
    novo_preco_label = ttk.Label(quadro_conteudo, text=f"Novo Preço de venda do Produto")
    novo_preco_label.pack(pady=10)
    novo_preco_entry = ttk.Entry(quadro_conteudo, width=30, bootstyle="INFO")
    novo_preco_entry.pack(pady=5)
    def mudar_preco_venda():
        try:
            novo_preco = float(novo_preco_entry.get())
            editar_valor_venda(editar_valor_nome=produto_nome, alterar_valorV=novo_preco, aplicativo=aplicativo)
            novo_preco_entry.delete(0, 'end')
        except ValueError as e:
            mostrar_pop_up("Erro", f"Erro no valor inserido: {str(e)}", "danger", aplicativo)
        except Exception as e:
            mostrar_pop_up("Erro", f"Um erro inesperado ocorreu: {str(e)}", "danger", aplicativo)
    botao_confirmar = ttk.Button(quadro_conteudo, text="Confirmar", bootstyle="INFO", command=mudar_preco_venda)
    botao_confirmar.pack(pady=10)
    botao_voltar = ttk.Button(quadro_conteudo, text="Voltar", bootstyle="DANGER", command=lambda: mostrar_opcoes_editar_produto((produto_nome,)))
    botao_voltar.pack(pady=10)

def mostrar_formulario_remover_produto():
    for widget in quadro_conteudo.winfo_children():
        widget.destroy()
    label_editar_produto = ttk.Label(quadro_conteudo, text="REMOVER PRODUTO!")
    label_editar_produto.pack(pady=25)
    label_editar_produto = ttk.Label(quadro_conteudo, text="Por favor insira o nome do produto")
    label_editar_produto.pack(pady=0)
    nome_label = ttk.Label(quadro_conteudo, text="Nome do Produto")
    nome_label.pack(pady=15)
    nome_entry = ttk.Entry(quadro_conteudo, width=30, bootstyle="INFO")
    nome_entry.pack(pady=0)
    def remover_produto():
        try:
            nome = nome_entry.get()
            remover(remover_nome=nome, aplicativo=aplicativo)
            nome_entry.delete(0, 'end')
        except ValueError as e:
            mostrar_pop_up("Erro", "Produto não encontrado.", "danger", aplicativo)
        except Exception as e:
            mostrar_pop_up("Erro", f"Um erro inesperado ocorreu: {str(e)}", "danger", aplicativo)
    botao_selecionar = ttk.Button(quadro_conteudo, text="Remover", bootstyle="INFO", command=remover_produto)
    botao_selecionar.pack(pady=10)
    botao_voltar = ttk.Button(quadro_conteudo, text="Voltar", bootstyle="DANGER", command=mostrar_conteudo_principal)
    botao_voltar.pack(pady=0)

def mostrar_formulario_lista():
    for widget in quadro_conteudo.winfo_children():
        widget.destroy()
    label_editar_produto = ttk.Label(quadro_conteudo, text="LISTA DE PRODUTOS")
    label_editar_produto.pack(pady=25)
    frame_tabela = ttk.Frame(quadro_conteudo)
    frame_tabela.pack(pady=5, padx=10, fill="both", expand=True)
    colunas = ("Nome", "Preço Compra", "Preço Venda", "Quantidade")
    tabela = ttk.Treeview(frame_tabela, columns=colunas, show="headings", height=10, bootstyle="INFO")
    for coluna in colunas:
        tabela.heading(coluna, text=coluna)
        tabela.column(coluna, anchor="center", width=100)
    scrollbar_y = ttk.Scrollbar(frame_tabela, orient="vertical", command=tabela.yview)
    scrollbar_x = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tabela.xview)
    tabela.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
    tabela.grid(row=0, column=0, sticky="nsew")
    scrollbar_y.grid(row=0, column=1, sticky="ns")
    scrollbar_x.grid(row=1, column=0, sticky="ew")
    frame_tabela.columnconfigure(0, weight=1)
    frame_tabela.rowconfigure(0, weight=1)
    try:
        banco = sqlite3.connect("Estoque.db")  # Alterar para 'gestao.db' se necessário
        tabela_bd = banco.cursor()
        tabela_bd.execute("SELECT nome, valor_compra, valor_venda, qtde FROM Estoque")
        produtos = tabela_bd.fetchall()
        for produto in produtos:
            tabela.insert("", "end", values=produto)
    except Exception as e:
        mostrar_pop_up("Erro", f"Erro ao carregar produtos: {str(e)}", "danger", aplicativo)
    finally:
        banco.close()
    frame_botoes = ttk.Frame(quadro_conteudo)
    frame_botoes.pack(pady=10, padx=10, fill="x")
    botao_voltar = ttk.Button(frame_botoes, text="Voltar", bootstyle="DANGER", command=mostrar_conteudo_principal)
    botao_voltar.pack(side="left", padx=5)
    entrada_pesquisa = ttk.Entry(frame_botoes, width=30, bootstyle="INFO")
    entrada_pesquisa.pack(side="right", padx=5)
    def pesquisar_produto():
        termo = entrada_pesquisa.get().lower()
        for item in tabela.get_children():
            valores = tabela.item(item, "values")
            nome_produto = valores[0].lower()
            if termo in nome_produto:
                tabela.selection_set(item)
                tabela.focus(item)
                tabela.see(item)
    botao_pesquisa = ttk.Button(frame_botoes, text="Pesquisar", bootstyle="INFO", command=pesquisar_produto)
    botao_pesquisa.pack(side="right")

def criar_widgets_barra(quadro_barra, estado_barra, comando_alternar):
    for widget in quadro_barra.winfo_children():
        widget.destroy()
    botao_alternar = ttk.Button(quadro_barra, text="☰", bootstyle=INFO, command=comando_alternar, width=4)
    botao_alternar.pack(anchor=NW, pady=10, padx=10)
    def mostrar_conteudo(nome_conteudo):
        for widget in quadro_conteudo.winfo_children():
            widget.destroy()
        if nome_conteudo == "Início":
            mostrar_conteudo_principal()
        if nome_conteudo == "Cadastrar Produto":
            mostrar_formulario_cadastro()
        if nome_conteudo == "Editar Produto":
            mostrar_formulario_editar_produto()
        if nome_conteudo == "Remover Produto":
            mostrar_formulario_remover_produto()
        if nome_conteudo == "Lista De Produto":
            mostrar_formulario_lista()
    itens_menu = [
        ("Início", "🏠", "Início"),
        ("Cadastrar Produto", "📦", "Cadastrar Produto"),
        ("Editar Produto", "📝", "Editar Produto"),
        ("Remover Produtos", "🧹", "Remover Produto"),
        ("Lista De Produtos", "🔍", "Lista De Produto")
    ]
    if estado_barra["expandido"]:
        for texto, icone, nome_conteudo in itens_menu:
            botao = ttk.Button(quadro_barra, text=f"{icone} {texto}", bootstyle=INFO, compound=LEFT, command=lambda nome=nome_conteudo: mostrar_conteudo(nome))
            botao.pack(anchor=W, fill=X, padx=10, pady=5)
    else:
        for texto, icone, nome_conteudo in itens_menu:
            botao = ttk.Button(quadro_barra, text=icone, bootstyle=INFO, compound=LEFT, width=8, command=lambda nome=nome_conteudo: mostrar_conteudo(nome))
            botao.pack(anchor=W, padx=10, pady=5)

def principal():
    global quadro_conteudo, aplicativo
    aplicativo = ttk.Window(themename="cyborg")
    aplicativo.title("NuEstoque")
    aplicativo.geometry("900x500")
    style = ttk.Style()
    style.configure('.', font=('Roboto-Regular', 12))
    estado_barra = {"expandido": True}
    quadro_principal = ttk.Frame(aplicativo)
    quadro_principal.pack(fill=BOTH, expand=YES)
    quadro_barra = ttk.Frame(quadro_principal, width=200, bootstyle=DARK)
    quadro_barra.pack(side=LEFT, fill=Y)
    quadro_barra.pack_propagate(False)
    quadro_conteudo = ttk.Frame(quadro_principal)
    quadro_conteudo.pack(side=RIGHT, fill=BOTH, expand=YES)
    comando_alternar = lambda: alternar_barra_lateral(estado_barra, quadro_barra, lambda: criar_widgets_barra(quadro_barra, estado_barra, comando_alternar))
    criar_widgets_barra(quadro_barra, estado_barra, comando_alternar)
    mostrar_conteudo_principal()
    aplicativo.bind("<<NomeProdutoAtualizado>>", lambda event: mostrar_conteudo_principal())
    aplicativo.mainloop()
if __name__ == "__main__":
    principal()



# adicionar cirulo roxo com o total bruto v e c e total liquido no inicio que se auto atualiza
#criar logo