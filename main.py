import customtkinter as tk
from tkcalendar import Calendar
from tkinter import ttk
import sqlite3
import tkinter
from tkinter import messagebox
import requests

banco = sqlite3.connect('banco.db')
cursor = banco.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS banco (id INTEGER PRIMARY KEY AUTOINCREMENT, nome_cliente TEXT, contato TEXT, endereco TEXT, pedido TEXT, data_pedido TEXT, data_prev_entrega TEXT, status TEXT)")

janela = tk.CTk()
janela.geometry("625x588+311+21")
janela.title('Gerenciamento')

janela.resizable(False, False)

tk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
tk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

# tk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
# tk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

frame = tk.CTkFrame(janela)
frame.pack(padx=5,pady=5)

label_logo = tk.CTkLabel(frame, text='Sua Logo', font=('', 70))
label_logo.pack()

gerenciamento_pedido = tk.CTkTabview(frame)
gerenciamento_pedido.pack(padx=10, pady=10)

# Tabela de Criar Pedido
tab_gerenciar_pedidos = gerenciamento_pedido.add('Criar Pedido')

label_nome_cliente = tk.CTkLabel(tab_gerenciar_pedidos, text='Nome do Cliente:')
label_nome_cliente.grid(row=0, column=0, padx=5, pady=5)

entry_nome_cliente = tk.CTkEntry(tab_gerenciar_pedidos, placeholder_text='Nome do Cliente')
entry_nome_cliente.grid(row=0, column=1, padx=5, pady=5)

label_contato_cliente = tk.CTkLabel(tab_gerenciar_pedidos, text='Contato | Whatsapp:')
label_contato_cliente.grid(row=1, column=0, padx=5, pady=5)

entry_contato_cliente = tk.CTkEntry(tab_gerenciar_pedidos, placeholder_text='Contato do Cliente')
entry_contato_cliente.grid(row=1, column=1, padx=5, pady=5)

label_contato_cliente = tk.CTkLabel(tab_gerenciar_pedidos, text='Endereço:')
label_contato_cliente.grid(row=2, column=0, padx=5, pady=5)

entry_endereco = tk.CTkEntry(tab_gerenciar_pedidos, placeholder_text='Endereço')
entry_endereco.grid(row=2, column=1, padx=5, pady=5)

def janela_endereco():
    janela_edicao_endereco = tk.CTkToplevel(janela)
    janela_edicao_endereco.geometry('400+120')
    janela_edicao_endereco.grab_set()
    janela_edicao_endereco.title('Endereço')
    janela_edicao_endereco.resizable(False, False)
    # Criar os rótulos e campos de entrada
    frame_edicao = tk.CTkFrame(janela_edicao_endereco)
    frame_edicao.pack(padx=10, pady=10)
    label_cep = tk.CTkLabel(frame_edicao, text="CEP:")
    entry_cep = tk.CTkEntry(frame_edicao, placeholder_text="Digite o CEP")

    label_endereco = tk.CTkLabel(frame_edicao, text="Endereço:")
    entry_endereco_top = tk.CTkEntry(frame_edicao, placeholder_text="Digite o endereço")

    label_numero = tk.CTkLabel(frame_edicao, text="Número:")
    entry_numero = tk.CTkEntry(frame_edicao, placeholder_text="Digite o número")

    label_cidade = tk.CTkLabel(frame_edicao, text="Cidade:")
    entry_cidade = tk.CTkEntry(frame_edicao, placeholder_text="Digite a cidade")

    label_estado = tk.CTkLabel(frame_edicao, text="Estado:")
    entry_estado = tk.CTkEntry(frame_edicao, placeholder_text="Digite o estado")

    label_complemento = tk.CTkLabel(frame_edicao, text="Complemento:")
    entry_complemento = tk.CTkEntry(frame_edicao, placeholder_text="Digite o complemento")

    def puxar_endereco():
        cep = entry_cep.get()
        cep = cep.replace("-", "").replace(".", "").replace(" ", "")
        if len(cep) == 8:
            link = f'https://viacep.com.br/ws/{cep}/json/'
            requisicao = requests.get(link)
            dic_requisicao = requisicao.json()
            uf = dic_requisicao['uf']
            cidade = dic_requisicao['localidade']
            endereco = dic_requisicao['bairro']
            entry_estado.insert(0, uf)
            entry_cidade.insert(0, cidade)
            entry_endereco_top.insert(0, endereco)
        else:
            # Exiba uma caixa de mensagem de erro
            messagebox.showerror("Erro", "Ocorreu um erro! Verifique o CEP ou a conexão com a internet!")

    # Criar o botão "Buscar Cep"
    
    button_buscar = tk.CTkButton(frame_edicao, text="Buscar CEP", width=10, command=puxar_endereco)
    
    def salvar():
        cep = entry_cep.get()
        endereco = entry_endereco_top.get()
        numero = entry_numero.get()
        cidade = entry_cidade.get()
        estado = entry_estado.get()
        complemento = entry_complemento.get()
        endereco_completo = f"CEP: {cep}\nEndereço: {endereco}\nNúmero: {numero}\nCidade: {cidade}\nEstado: {estado}\nComplemento: {complemento}"
        entry_endereco.insert(0, endereco_completo)
        janela_edicao_endereco.destroy()
        
    # Criar o botão "Salvar"
    button_salvar = tk.CTkButton(frame_edicao, text="Salvar", command=salvar)

    # Posicionar os elementos usando o grid
    label_cep.grid(row=0, column=0, sticky="e", padx=5, pady=5)
    entry_cep.grid(row=0, column=1, padx=5, pady=5)
    button_buscar.grid(row=0, column=2, padx=5, pady=5)
    label_endereco.grid(row=1, column=0, columnspan=1, sticky="e", padx=5, pady=5)
    entry_endereco_top.grid(row=1, column=0, columnspan=3, padx=5, pady=5)
    label_numero.grid(row=2, column=0, sticky="e", padx=5, pady=5)
    entry_numero.grid(row=2, column=0, columnspan=3, padx=5, pady=5)
    label_cidade.grid(row=3, column=0, sticky="e", padx=5, pady=5)
    entry_cidade.grid(row=3, column=0, columnspan=3, padx=5, pady=5)
    label_estado.grid(row=4, column=0, sticky="e", padx=5, pady=5)
    entry_estado.grid(row=4, column=0, columnspan=3, padx=5, pady=5)
    label_complemento.grid(row=5, column=0, sticky="e", padx=5, pady=5)
    entry_complemento.grid(row=5, column=0, columnspan=3, padx=5, pady=5)
    button_salvar.grid(row=6, column=0, columnspan=3, padx=5, pady=5)
    
button_endereco = tk.CTkButton(tab_gerenciar_pedidos, text=". . .", width=50, font=("", 13), command=janela_endereco)
button_endereco.grid(row=2, column=2)

label_produto = tk.CTkLabel(tab_gerenciar_pedidos, text='Produto | Pedido:')
label_produto.grid(row=3, column=0,padx=5, pady=5)

entry_produto = tk.CTkEntry(tab_gerenciar_pedidos, placeholder_text='Descreva o pedido')
entry_produto.grid(row=3, column=1, padx=5, pady=5)

def pedido_detalhado():
    janela_pedido_detalhado = tk.CTkToplevel(janela)
    janela_pedido_detalhado.geometry('280+100')
    janela_pedido_detalhado.title('Pedido Detalhado')
    janela_pedido_detalhado.grab_set()
    janela_pedido_detalhado.resizable(False, False)


    frame_adulto = tk.CTkFrame(janela_pedido_detalhado)
    frame_adulto.grid(row=1, column=0, padx=5, pady=5)

    gerenciamento_pedido = tk.CTkTabview(frame_adulto)
    gerenciamento_pedido.pack(padx=10, pady=10)

    # Tabela de Criar Pedido
    tab_pedido_adulto = gerenciamento_pedido.add('Tamanho Adulto')
    tab_pedido_infantil = gerenciamento_pedido.add('Tamanho Infantil')

    # Grupo 1 - Informações da Camiseta
    label_info_camiseta = tk.CTkLabel(tab_pedido_adulto, text='Informações da Camiseta:')
    label_info_camiseta.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky='w')

    label_tamanho_adulto = tk.CTkLabel(tab_pedido_adulto, text='Tamanho:')
    label_tamanho_adulto.grid(row=1, column=0, padx=5, pady=5)

    opcoes_tamanho_adulto = ["PP", "P", "M", "G", "GG", "XG", "XXG"]
    combo_tamanho_adulto = tk.CTkComboBox(tab_pedido_adulto, values=opcoes_tamanho_adulto)
    combo_tamanho_adulto.grid(row=1, column=1, padx=5, pady=5)

    label_modelo_adulto = tk.CTkLabel(tab_pedido_adulto, text='Modelo:')
    label_modelo_adulto.grid(row=2, column=0, padx=5, pady=5)

    opcoes_modelo_adulto = ["Básica", "Baby Look", "Polo", "Regata", "3/4", "Manga Longa"]
    combo_modelo_adulto = tk.CTkComboBox(tab_pedido_adulto, values=opcoes_modelo_adulto)
    combo_modelo_adulto.grid(row=2, column=1, padx=5, pady=5)

    label_gola_adulto = tk.CTkLabel(tab_pedido_adulto, text='Gola:')
    label_gola_adulto.grid(row=3, column=0, padx=5, pady=5)

    opcoes_gola_adulto = ["Careca", "V", "Polo"]
    combo_gola_adulto = tk.CTkComboBox(tab_pedido_adulto, values=opcoes_gola_adulto)
    combo_gola_adulto.grid(row=3, column=1, padx=5, pady=5)

    # Grupo 2 - Informações de Quantidade e Preço
    label_info_preco = tk.CTkLabel(tab_pedido_adulto, text='Informações de Quantidade e Preço:')
    label_info_preco.grid(row=4, column=0, columnspan=3, padx=5, pady=5, sticky='w')

    label_nome_tecido_adulto = tk.CTkLabel(tab_pedido_adulto, text='Nome do Tecido:')
    label_nome_tecido_adulto.grid(row=5, column=0, padx=5, pady=5)

    entry_nome_tecido_adulto = tk.CTkEntry(tab_pedido_adulto, placeholder_text='Nome do tecido')
    entry_nome_tecido_adulto.grid(row=5, column=1, padx=5, pady=5)

    label_quantidade_adulto = tk.CTkLabel(tab_pedido_adulto, text='Quantidade Total:')
    label_quantidade_adulto.grid(row=6, column=0, padx=5, pady=5)

    entry_quantidade_adulto = tk.CTkEntry(tab_pedido_adulto, placeholder_text='Quantidade')
    entry_quantidade_adulto.grid(row=6, column=1, padx=5, pady=5)

    label_preco_adulto = tk.CTkLabel(tab_pedido_adulto, text='Preço Unitário:')
    label_preco_adulto.grid(row=7, column=0, padx=5, pady=5)

    entry_preco_adulto = tk.CTkEntry(tab_pedido_adulto, placeholder_text='Preço')
    entry_preco_adulto.grid(row=7, column=1, padx=5, pady=5)

    # Grupo 3 - Outras Informações
    label_info_outras = tk.CTkLabel(tab_pedido_adulto, text='Outras Informações:')
    label_info_outras.grid(row=0, column=2, padx=5, pady=5, sticky='w')

    label_observacao_adulto = tk.CTkLabel(tab_pedido_adulto, text='Observação:')
    label_observacao_adulto.grid(row=1, column=2, padx=5, pady=5)

    text_obs_adulto = tk.CTkTextbox(tab_pedido_adulto, wrap="word")
    text_obs_adulto.grid(row=1, column=3, rowspan=6, padx=5, pady=5, sticky="nsew")

    label_valor_adulto = tk.CTkLabel(tab_pedido_adulto, text='Valor Total:')
    label_valor_adulto.grid(row=7, column=2, padx=5, pady=5)

    entry_valor_adulto = tk.CTkEntry(tab_pedido_adulto, placeholder_text='Valor')
    entry_valor_adulto.grid(row=7, column=3, padx=5, pady=5)

    def calcular_valor_total_adulto():
        quantidade = entry_quantidade_adulto.get().replace(',', '.')
        preco_unidade = entry_preco_adulto.get().replace(',', '.')
        if quantidade and preco_unidade:
            valor = float(quantidade) * float(preco_unidade)
            valor_formatado = "{:.2f}".format(valor)
            entry_valor_adulto.delete(0, tk.END)
            entry_valor_adulto.insert(0, valor_formatado)
        else:
            messagebox.showerror("Erro", "Verifique os campos de quantidade e preço!")

    button_calcular = tk.CTkButton(tab_pedido_adulto, text='Calcular Valor Total', command=calcular_valor_total_adulto)
    button_calcular.grid(row=12, column=0, columnspan=4, padx=5, pady=5)

    def salvar_pedido_adulto():
        tamanho = combo_tamanho_adulto.get()
        modelo = combo_modelo_adulto.get()
        gola = combo_gola_adulto.get()
        tecido = entry_nome_tecido_adulto.get()
        observacao = text_obs_adulto.get('1.0', tk.END)
        observacao = observacao.replace('\n', '')
        quantidade = entry_quantidade_adulto.get()
        preco = entry_preco_adulto.get()
        valor = entry_valor_adulto.get()
        pedido = f'Pedido Adulto no Tamanho: {tamanho}\nModelo: {modelo}\nGola: {gola}\nTecido: {tecido}\nObservação: {observacao}\nQuantidade: {quantidade}\nPreço unitário: {preco}\nValor: {valor}'
        entry_produto.insert(0, pedido)
        janela_pedido_detalhado.destroy()

    button_salvar_adulto = tk.CTkButton(tab_pedido_adulto, text='Salvar', command=salvar_pedido_adulto)
    button_salvar_adulto.grid(row=13, column=0, columnspan=4, padx=5, pady=5)

    #infantil
    label_info_camiseta = tk.CTkLabel(tab_pedido_infantil, text='Informações da Camiseta:')
    label_info_camiseta.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky='w')

    label_tamanho_infantil = tk.CTkLabel(tab_pedido_infantil, text='Tamanho:')
    label_tamanho_infantil.grid(row=1, column=0, padx=5, pady=5)

    opcoes_tamanho_infantil = ["1", "2", "4", "6", "8", "10"]
    combo_tamanho_infantil = tk.CTkComboBox(tab_pedido_infantil, values=opcoes_tamanho_infantil)
    combo_tamanho_infantil.grid(row=1, column=1, padx=5, pady=5)

    label_modelo_infantil = tk.CTkLabel(tab_pedido_infantil, text='Modelo:')
    label_modelo_infantil.grid(row=2, column=0, padx=5, pady=5)

    opcoes_tamanho_infantil = ["Básica Baby Look", "Polo", "Regata"]
    combo_modelo_infantil = tk.CTkComboBox(tab_pedido_infantil, values=opcoes_tamanho_infantil)
    combo_modelo_infantil.grid(row=2, column=1, padx=5, pady=5)

    label_gola_infantil = tk.CTkLabel(tab_pedido_infantil, text='Gola:')
    label_gola_infantil.grid(row=3, column=0, padx=5, pady=5)

    opcoes_gola_infantil = ["Careca", "V", "Polo"]
    combo_gola_infantil = tk.CTkComboBox(tab_pedido_infantil, values=opcoes_gola_infantil)
    combo_gola_infantil.grid(row=3, column=1, padx=5, pady=5)  

    # Grupo 2 - Informações de Quantidade e Preço
    label_info_preco = tk.CTkLabel(tab_pedido_infantil, text='Informações de Quantidade e Preço:')
    label_info_preco.grid(row=4, column=0, columnspan=3, padx=5, pady=5, sticky='w')

    label_nome_tecido_infantil = tk.CTkLabel(tab_pedido_infantil, text='Nome do Tecido:')
    label_nome_tecido_infantil.grid(row=5, column=0, padx=5, pady=5)

    entry_nome_tecido_infantil = tk.CTkEntry(tab_pedido_infantil, placeholder_text='Nome do tecido')
    entry_nome_tecido_infantil.grid(row=5, column=1, padx=5, pady=5)

    label_quantidade_infantil = tk.CTkLabel(tab_pedido_infantil, text='Quantidade Total:')
    label_quantidade_infantil.grid(row=6, column=0, padx=5, pady=5)

    entry_quantidade_infantil = tk.CTkEntry(tab_pedido_infantil, placeholder_text='Quantidade')
    entry_quantidade_infantil.grid(row=6, column=1, padx=5, pady=5)

    label_preco_infantil = tk.CTkLabel(tab_pedido_infantil, text='Preço Unitário:')
    label_preco_infantil.grid(row=7, column=0, padx=5, pady=5)

    entry_preco_infantil = tk.CTkEntry(tab_pedido_infantil, placeholder_text='Preço')
    entry_preco_infantil.grid(row=7, column=1, padx=5, pady=5)

    # Grupo 3 - Outras Informações
    label_info_outras = tk.CTkLabel(tab_pedido_infantil, text='Outras Informações:')
    label_info_outras.grid(row=0, column=2, padx=5, pady=5, sticky='w')

    label_observacao_infantil = tk.CTkLabel(tab_pedido_infantil, text='Observação:')
    label_observacao_infantil.grid(row=1, column=2, padx=5, pady=5)

    text_obs_infantil = tk.CTkTextbox(tab_pedido_infantil, wrap="word")
    text_obs_infantil.grid(row=1, column=3, rowspan=6, padx=5, pady=5, sticky="nsew")

    label_valor_infantil = tk.CTkLabel(tab_pedido_infantil, text='Valor Total:')
    label_valor_infantil.grid(row=7, column=2, padx=5, pady=5)

    entry_valor_infantil = tk.CTkEntry(tab_pedido_infantil, placeholder_text='Valor')
    entry_valor_infantil.grid(row=7, column=3, padx=5, pady=5)


    def calcular_valor_total_infantil():
        quantidade = entry_quantidade_infantil.get().replace(',', '.')
        preco_unidade = entry_preco_infantil.get().replace(',', '.')
        if quantidade and preco_unidade:
            valor = float(quantidade) * float(preco_unidade)
            valor_formatado = "{:.2f}".format(valor)
            entry_valor_infantil.delete(0, tk.END)
            entry_valor_infantil.insert(0, valor_formatado)
        else:
            messagebox.showerror("Erro", "Preencha os campos de quantidade e preço!")

    button_calcular = tk.CTkButton(tab_pedido_infantil, text='Calcular Valor Total', command=calcular_valor_total_infantil)
    button_calcular.grid(row=12, column=0, columnspan=4, padx=5, pady=5)
    
    def salvar_pedido_infantil():
        tamanho = combo_tamanho_infantil.get()
        modelo = combo_modelo_infantil.get()
        gola = combo_gola_infantil.get()
        tecido = entry_nome_tecido_infantil.get()
        observacao = text_obs_infantil.get('1.0', tk.END)
        observacao = observacao.replace('\n', '')
        quantidade = entry_quantidade_infantil.get()
        preco = entry_preco_infantil.get()
        valor = entry_valor_infantil.get()
        pedido = f'Pedido no Infantil no Tamanho: {tamanho}\nModelo: {modelo}\nGola: {gola}\nTecido: {tecido}\nObservação: {observacao}\nQuantidade: {quantidade}\nPreço unitário: {preco}\nValor: {valor}'
        entry_produto.insert(0, pedido)
        janela_pedido_detalhado.destroy()

    button_salvar_infantil = tk.CTkButton(tab_pedido_infantil, text='Salvar', command=salvar_pedido_infantil)
    button_salvar_infantil.grid(row=13, column=0, columnspan=4, padx=5, pady=5)


button_pedido_detalhado = tk.CTkButton(tab_gerenciar_pedidos, text=". . .", width=50, font=("", 13), command=pedido_detalhado)
button_pedido_detalhado.grid(row=3, column=2)

data_calendario1 = None
data_calendario2 = None

def criar_pedido():
    global data_calendario1, data_calendario2
    
    data_selecionada_calendario1 = calendario1.get_date()
    if data_selecionada_calendario1 is not None:
        data_calendario1 = data_selecionada_calendario1
    
    data_selecionada_calendario2 = calendario2.get_date()
    if data_selecionada_calendario2 is not None:
        data_calendario2 = data_selecionada_calendario2

    nome_cliente = entry_nome_cliente.get()
    contato_cliente = entry_contato_cliente.get()
    produto = entry_produto.get()
    endereco = entry_endereco.get()
    
    # Inserindo dados
    cursor.execute('''INSERT INTO banco
                  (nome_cliente, contato, endereco, pedido, data_pedido, data_prev_entrega, status)
                  VALUES (?, ?, ?, ?, ?, ?, ?)''',
               (nome_cliente, contato_cliente, endereco, produto, data_calendario1, data_calendario2, 'Para Produção'))

    # Salvando as alterações
    banco.commit()
    atualizar_treeview_todos_pedidos()
    # Exibir janela de "pedido criado"
    messagebox.showinfo("Pedido Criado", "O pedido foi criado com sucesso!")

label_calendario1 = tk.CTkLabel(tab_gerenciar_pedidos, text='Data do pedido:', font=("", 20))
label_calendario1.grid(row=4, column=0, padx=5, pady=5)

calendario1 = Calendar(tab_gerenciar_pedidos, variable=data_calendario1, showweeknumbers=False, date_pattern= 'dd-mm-yyyy', cursor="hand2")
calendario1.grid(row=5, column=0, padx=5, pady=5)

label_calendario2 = tk.CTkLabel(tab_gerenciar_pedidos, text='Previsão de entrega:', font=("", 20))
label_calendario2.grid(row=4, column=1, padx=5, pady=5, columnspan=2)

calendario2 = Calendar(tab_gerenciar_pedidos, variable=data_calendario2, showweeknumbers=False, date_pattern= 'dd-mm-yyyy', cursor="hand2")
calendario2.grid(row=5, column=1, padx=5, pady=5, columnspan=2)

button_criar_pedido = tk.CTkButton(tab_gerenciar_pedidos, text='Criar Pedido', command=criar_pedido)
button_criar_pedido.grid(row=6, column=0, columnspan=3, padx=10, pady=10)

# Tab "Verificar Pedidos"
tab_gerenciar_todos = gerenciamento_pedido.add('Verificar Pedidos')

label_pesquisa = tk.CTkLabel(tab_gerenciar_todos, text="Pesquisar Cliente")
label_pesquisa.grid(row=0, column=0)

entry_pesquisa = tk.CTkEntry(tab_gerenciar_todos, placeholder_text='Nº Pedido ou Contato')
entry_pesquisa.grid(row=1, column=0, pady=5)

def pesquisar_cliente():
    # ID do cliente a ser buscado
    id_cliente = entry_pesquisa.get()
    contato = entry_pesquisa.get()
    # Executar a instrução SELECT
    cursor.execute("SELECT * FROM banco WHERE id = ?", (id_cliente,))
    dados_cliente = cursor.fetchone()

    # Exibir os dados do cliente
    if not dados_cliente:
        cursor.execute("SELECT * FROM banco WHERE contato = ?", (contato,))
        dados_cliente = cursor.fetchone()

    if dados_cliente:
        id_cliente = dados_cliente[0]
        nome = dados_cliente[1]
        contato = dados_cliente[2] 
        endereco = dados_cliente[3]
        pedido = dados_cliente[4]
        data_pedido = dados_cliente[5]
        data_entrega = dados_cliente[6]
        status = dados_cliente[7]
        tree.delete(*tree.get_children())
        tree.insert("", "end", values=(id_cliente, nome, contato, endereco, pedido, data_pedido, data_entrega, status))
        
    else:
        messagebox.showwarning("Aviso", "Cliente não encontrado!")

button_pesquisar = tk.CTkButton(tab_gerenciar_todos, text='Pesquisar', command=pesquisar_cliente)
button_pesquisar.grid(row=2, column=0)

label_filtrar = tk.CTkLabel(tab_gerenciar_todos, text="Filtrar:")
label_filtrar.grid(row=0, column=1)

filtros = ['Todos', 'Para produção', 'Em produção', 'Falta Pagamento', 'Falta Material', 'Concluído']
combo_filtro = tk.CTkComboBox(tab_gerenciar_todos, values=filtros)
combo_filtro.grid(row=1, column=1, pady=5)

def filtrar():
    # Obter o status selecionado no ComboBox
    status_selecionado = combo_filtro.get()

    if status_selecionado == 'Todos':
        cursor.execute("SELECT * FROM banco")
        registros = cursor.fetchall()
        
        # Limpar a Treeview
        tree.delete(*tree.get_children())

        # Adicionar os registros ao Treeview
        for registro in registros:
            tree.insert("", tk.END, values=registro)
    else:
        # Filtrar os dados da tabela "banco" com base no status selecionado
        cursor.execute("SELECT * FROM banco WHERE status = ?", (status_selecionado,))
        dados_filtrados = cursor.fetchall()

        # Limpar a Treeview
        tree.delete(*tree.get_children())

        # Atualizar a Treeview com os dados filtrados
        for dados in dados_filtrados:
            tree.insert("", "end", values=dados)


button_filtrar = tk.CTkButton(tab_gerenciar_todos, text='Filtrar Status', command=filtrar)
button_filtrar.grid(row=2, column=1)

tree = ttk.Treeview(tab_gerenciar_todos, show="headings", height=15)

# Defina as colunas e os cabeçalhos
colunas = ("Nº", "Nome", "Contato", "Endereço", "Pedido", "Data", "Entrega", "Status")
tree["columns"] = colunas

column_widths = [40, 70, 70, 70, 70, 70, 70, 100]
column_anchor = tk.CENTER

for i, coluna in enumerate(colunas):
    tree.column(coluna, width=column_widths[i], anchor=column_anchor)
    tree.heading(coluna, text=coluna)

# Atualizar o Treeview inicialmente
def atualizar_treeview_todos_pedidos():
    # Limpar todas as linhas existentes no Treeview
    tree.delete(*tree.get_children())
    
    # Recuperar os registros do banco de dados
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM banco")
    registros = cursor.fetchall()
    
    # Adicionar os registros ao Treeview
    for registro in registros:
        tree.insert("", tk.END, values=registro)


atualizar_treeview_todos_pedidos()
tree.grid(row=4, column=0, columnspan=2, padx=5, pady=5)


# Crie o menu de contexto
def tela_edicao():
    item_selecionado = tree.selection()
    if item_selecionado:
        
        nome = tree.item(item_selecionado)['values'][1]
        contato = tree.item(item_selecionado)['values'][2]
        endereco = tree.item(item_selecionado)['values'][3]
        pedido = tree.item(item_selecionado)['values'][4]
        data_pedido = tree.item(item_selecionado)['values'][5]
        data_entrega = tree.item(item_selecionado)['values'][6]
        status = tree.item(item_selecionado)['values'][7]

        # Criar a janela de edição
        janela_edicao = tk.CTkToplevel(janela)
        janela_edicao.geometry('280+7')
        janela_edicao.grab_set()
        janela_edicao.title('Editar')
        janela_edicao.resizable(False, False)
        datevar1 = tk.StringVar(janela_edicao, data_pedido)
        datevar2 = tk.StringVar(janela_edicao, data_entrega)
        
        label_edicao = tk.CTkLabel(janela_edicao, text='Editar', font=("", 25))
        label_edicao.pack(padx=5, pady=5)

        # Criar o frame dentro da janela de edição
        frame = tk.CTkFrame(janela_edicao)
        frame.pack(padx=20, pady=20)

        label_nome_cliente = tk.CTkLabel(frame, text='Nome do Cliente:')
        label_nome_cliente.grid(row=0, column=0, padx=5, pady=5)

        entry_nome = tk.CTkEntry(frame, placeholder_text='Nome do Cliente')
        entry_nome.insert(0, nome)
        entry_nome.grid(row=0, column=1, padx=5, pady=5)

        label_contato_cliente = tk.CTkLabel(frame, text='Contato | Whatsapp:')
        label_contato_cliente.grid(row=1, column=0, padx=5, pady=5)

        entry_contato = tk.CTkEntry(frame, placeholder_text='Contato do Cliente')
        entry_contato.insert(0, contato)
        entry_contato.grid(row=1, column=1, padx=5, pady=5)

        label_status_cliente = tk.CTkLabel(frame, text='Status do pedido:')
        label_status_cliente.grid(row=2, column=0, padx=5, pady=5)

        statuses = ['Para produção', 'Em produção', 'Falta Pagamento', 'Falta Material', 'Concluído']
        combo_status = tk.CTkComboBox(frame, values=statuses)
        combo_status.set(status)
        combo_status.grid(row=2, column=1, padx=5, pady=5)

        label_endereco = tk.CTkLabel(frame, text='Endereço:')
        label_endereco.grid(row=4, column=1, columnspan=1, padx=5, pady=5)

        text_endereco = tk.CTkTextbox(frame, height=130, wrap="word")
        text_endereco.insert(tk.END, endereco)
        text_endereco.grid(row=5, column=1, columnspan=1, padx=5, pady=5)

        label_produto = tk.CTkLabel(frame, text='Produto | Pedido:')
        label_produto.grid(row=4, column=0, columnspan=1, padx=5, pady=5)

        # Criar o campo de texto
        texto_pedido = tk.CTkTextbox(frame, height=130, wrap="word")
        texto_pedido.insert(tk.END, pedido)
        texto_pedido.grid(row=5, column=0, columnspan=1)

        # Criar os calendários
        label_calendario1 = tk.CTkLabel(frame, text='Data do pedido:', font=("", 20))
        label_calendario1.grid(row=6, column=0, padx=10, pady=5)

        calendario_pedido = Calendar(frame, showweeknumbers=False, date_pattern= 'dd-mm-yyyy', cursor="hand2", textvariable=datevar1)
        calendario_pedido.grid(row=7, column=0, padx=10, pady=5)

        label_calendario2 = tk.CTkLabel(frame, text='Previsão de entrega:', font=("", 20))
        label_calendario2.grid(row=6, column=1, padx=10, pady=5)

        calendario_entrega = Calendar(frame, showweeknumbers=False, date_pattern= 'dd-mm-yyyy', cursor="hand2", textvariable=datevar2)
        calendario_entrega.grid(row=7, column=1, padx=10, pady=5)

        # Função para salvar as alterações
        def salvar_edicao():
            indice = int(tree.index(item_selecionado))
            novo_nome = entry_nome.get()
            novo_contato = entry_contato.get()
            novo_endereco = text_endereco.get("0.0", tk.END).rstrip('\n')
            novo_pedido = texto_pedido.get("0.0", tk.END).rstrip('\n')
            data_pedido = calendario_pedido.get_date()
            data_entrega = calendario_entrega.get_date()
            status = combo_status.get()
            
            indice += 1
            if indice:
                # Fazendo atualização de dados
                # Atualizar os dados no banco de dados usando o índice como parâmetro
                cursor.execute("UPDATE banco SET nome_cliente = ?, contato = ?, endereco = ?, pedido = ?, data_pedido = ?, data_prev_entrega = ?, status = ? WHERE id = ?",
                (novo_nome, novo_contato, novo_endereco, novo_pedido, data_pedido, data_entrega, status, indice))

                banco.commit()
                atualizar_treeview_todos_pedidos()
                messagebox.showinfo("Pedido Atualizado", "As alterações foram salvas com sucesso!")
                janela_edicao.destroy()

        # Criar o botão de salvar
        botao_salvar = tk.CTkButton(frame, text="Salvar", command=salvar_edicao)
        botao_salvar.grid(row=8, column=0, columnspan=2, pady=5)
        
def excluir():
    item_selecionado = tree.selection()
    if item_selecionado:
        indice = tree.item(item_selecionado)['values'][0]
        # Exibir uma janela de confirmação
        resposta = messagebox.askyesno("Excluir Dados", "Deseja excluir os dados selecionados?")
        
        if resposta:
            
            # Lógica para excluir os dados no banco de dados
            # ...
            cursor.execute("DELETE FROM banco WHERE id = ?", (indice,))
            # Excluir o item da Treeview
            tree.delete(item_selecionado)
            banco.commit()
            messagebox.showinfo("Pedido Atualizado", "Dados excluidos com sucesso!")
        else:
            print("Exclusão cancelada pelo usuário")

def opcao3():
    item_selecionado = tree.selection()
    if item_selecionado:
        indice = tree.index(item_selecionado)  # Obter o índice numérico do item
        print("Concluir item:", indice)

def exibir_menu(event):
    # Obter o item selecionado no Treeview
    item_selecionado = tree.identify('item', event.x, event.y)
    if item_selecionado:
        tree.selection_set(item_selecionado)  # Definir o item como selecionado
        menu_contexto.post(event.x_root, event.y_root)

menu_contexto = tkinter.Menu(janela, tearoff=0)
menu_contexto.add_command(label="Editar e Exibir Detalhes", command=tela_edicao)
menu_contexto.add_command(label="Excluir", command=excluir)
menu_contexto.add_command(label="Atualizar Tabela", command=atualizar_treeview_todos_pedidos)

def executar_opcao1(event):
    tela_edicao()

tree.bind("<Double-Button-1>", executar_opcao1)

# Vincule o menu de contexto ao evento de clique com o botão direito do mouse
tree.bind("<Button-3>", exibir_menu)

janela.mainloop()
