
import tkinter as tk
from tkinter import messagebox
import mysql.connector

connector = mysql.connector.connect(
    host="localhost",
    user="root", 
    password="", 
    database="petshop"  
)

cursor= connector.cursor()

estilo_botao = {#dicionário com configurações do estilo dos botões
        "width": 20,#largura do botão
        "height": 2,#altura do botão
        "font": ("Arial", 18, "bold"),#fonte do texto no botão
        "bg": "#4CAF50",#cor verde no botão
        "fg": "white",#cor branca no texto
        "relief": "flat",#botão sem borda
        "bd": 2,#espessura da borda (inativa)
        "highlightthickness": 0,#desativa o realce ao redor
        "activebackground": "#45a049",#cor verde mais clara quando o botão é clicado
        "activeforeground": "white",#mantém o texto branco ao clicar
    }

def cadastrar_cliente():

    esconder_menu_cliente()


    lbl_nome = tk.Label(root, text="Nome:")
    lbl_nome.pack(pady=5)
    entry_nome = tk.Entry(root)
    entry_nome.pack(pady=5)


    lbl_id = tk.Label(root, text="ID:")
    lbl_id.pack(pady=5)
    entry_id = tk.Entry(root)
    entry_id.pack(pady=5)


    lbl_cpf = tk.Label(root, text="CPF:")
    lbl_cpf.pack(pady=5)
    entry_cpf = tk.Entry(root)
    entry_cpf.pack(pady=5)


    lbl_endereco = tk.Label(root, text="Endereço:")
    lbl_endereco.pack(pady=5)
    entry_endereco = tk.Entry(root)
    entry_endereco.pack(pady=5)


    btn_salvar = tk.Button(root, text="Mandar", command=lambda:cadastrando_cliente(entry_nome,entry_id,entry_cpf,entry_endereco), **estilo_botao)
    btn_salvar.pack(pady=10)


    btn_voltar = tk.Button(root, text="Voltar", command=voltar_menu, **estilo_botao)
    btn_voltar.pack(pady=10)

def cadastrando_cliente(entry_nome,entry_id,entry_cpf,entry_endereco):
    id= entry_id.get()
    nome= entry_nome.get()
    cpf= entry_cpf.get()
    endereco= entry_endereco.get()
    try:
        mandar= f'INSERT INTO cliente(id,nome,cpf,endereco) VALUES ({id},"{nome}",{cpf},"{endereco}")'
        cursor.execute(mandar)
        connector.commit()
        messagebox.showinfo("Sucesso",f"sucessor ao cadastrar cliente!")
    except Exception as e:
        messagebox.showerror("Erro",f"erro ao cadastrar cliente{e}")
    
def excluicao_cliente():
    esconder_menu_cliente()
    
    lbl_id = tk.Label(root, text="ID:")
    lbl_id.pack(pady=5)
    entry_id = tk.Entry(root)
    entry_id.pack(pady=5)


    btn_salvar = tk.Button(root, text="Excluir", command=lambda: excluindo_cliente(entry_id), **estilo_botao)
    btn_salvar.pack(pady=10)
    

    btn_voltar = tk.Button(root, text="Voltar", command=voltar_menu, **estilo_botao)
    btn_voltar.pack(pady=10)

def excluindo_cliente(entry_id):
    id= entry_id.get()
    try:
        tirar= f'DELETE FROM cliente WHERE id={id}'
        cursor.execute(tirar)
        connector.commit()
        messagebox.showinfo("Sucesso",f"sucesso ao excluir cliente!")
    except Exception as e:
        messagebox.showerror("Erro",f"erro ao excluir cliente{e}")
    
def atualizacao_cliente():
    esconder_menu_cliente()

    lbl_id = tk.Label(root, text="ID:")
    lbl_id.pack(pady=5)
    entry_id = tk.Entry(root)
    entry_id.pack(pady=5)


    lbl_nome = tk.Label(root, text="Nome:")
    lbl_nome.pack(pady=5)
    entry_nome = tk.Entry(root)
    entry_nome.pack(pady=5)


    lbl_cpf = tk.Label(root, text="CPF:")
    lbl_cpf.pack(pady=5)
    entry_cpf = tk.Entry(root)
    entry_cpf.pack(pady=5)


    lbl_endereco = tk.Label(root, text="Endereço:")
    lbl_endereco.pack(pady=5)
    entry_endereco = tk.Entry(root)
    entry_endereco.pack(pady=5)


    btn_atualizar = tk.Button(root, text="Atualizar", command=lambda: atualizando_cliente(entry_id,entry_nome,entry_cpf,entry_endereco), **estilo_botao)
    btn_atualizar.pack(pady=10)

    btn_voltar = tk.Button(root, text="Voltar", command=voltar_menu, **estilo_botao)
    btn_voltar.pack(pady=10)


def atualizando_cliente(entry_id,entry_nome,entry_cpf,entry_endereco):
    id= entry_id.get()
    nome= entry_nome.get()
    cpf= entry_cpf.get()
    endereco= entry_endereco.get()
    try:
        trocar= f'UPDATE cliente SET nome="{nome}",cpf={cpf}, endereco="{endereco}" WHERE id={id}'
        cursor.execute(trocar)
        connector.commit()
        messagebox.showinfo("Sucesso", "Cliente atualizado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao atualizar cliente: {e}")
    

def pesquisa_cliente():
    esconder_menu_cliente()
    lbl_id = tk.Label(root, text="ID de pesquisa:")
    lbl_id.pack(pady=5)
    entry_id = tk.Entry(root)
    entry_id.pack(pady=5)


    btn_pesquisar = tk.Button(root, text="Pesquisa", command=lambda: pesquisando_cliente(entry_id), **estilo_botao)
    btn_pesquisar.pack(pady=10)

    btn_voltar = tk.Button(root, text="Voltar", command=voltar_menu, **estilo_botao)
    btn_voltar.pack(pady=10)

def pesquisando_cliente(entry_id):  
        id= entry_id.get()
        try:
            cursor.execute(f"SELECT * FROM cliente WHERE id = '{id}'")
            cliente = cursor.fetchone()
            if cliente:
                messagebox.showinfo("Resultado", f"Cliente encontrado:\nID: {cliente[0]}\nNome: {cliente[1]}\nCPF: {cliente[2]}")
            else:
                messagebox.showinfo("Resultado", "Nenhum cliente encontrado com esse ID.")
            voltar_menu()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao pesquisar cliente: {e}")

def esconder_menu_cliente():

    for widget in root.winfo_children():
        widget.pack_forget()


def cadastrar_pet():

    esconder_menu_cliente()


    lbl_nome = tk.Label(root, text="Nome:")
    lbl_nome.pack(pady=5)
    entry_nome = tk.Entry(root)
    entry_nome.pack(pady=5)


    lbl_id = tk.Label(root, text="ID:")
    lbl_id.pack(pady=5)
    entry_id = tk.Entry(root)
    entry_id.pack(pady=5)


    lbl_raca = tk.Label(root, text="Raça:")
    lbl_raca.pack(pady=5)
    entry_raca = tk.Entry(root)
    entry_raca.pack(pady=5)

    lbl_especie = tk.Label(root, text="Especie:")
    lbl_especie.pack(pady=5)
    entry_especie = tk.Entry(root)
    entry_especie.pack(pady=5)


    btn_salvar = tk.Button(root, text="Mandar", command=lambda: cadastrando_pet(entry_id,entry_nome,entry_raca,entry_especie), **estilo_botao)
    btn_salvar.pack(pady=10)


    btn_voltar = tk.Button(root, text="Voltar", command=voltar_menu, **estilo_botao)
    btn_voltar.pack(pady=10)


def cadastrando_pet(entry_id,entry_nome,entry_raca,entry_especie):
    id= entry_id.get()
    nome= entry_nome.get()
    raca=entry_raca.get()
    especie= entry_especie.get()
    try:
        mandar= f'INSERT INTO pet(id,nome,raca,especie) VALUES ({id},"{nome}","{raca}","{especie}")'
        cursor.execute(mandar)
        connector.commit()
        messagebox.showinfo("Sucesso", "pet cadastrado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao cadastrar pet: {e}")

def excluir_pet():
    esconder_menu_cliente()
    
    lbl_id = tk.Label(root, text="ID:")
    lbl_id.pack(pady=5)
    entry_id = tk.Entry(root)
    entry_id.pack(pady=5)


    btn_salvar = tk.Button(root, text="Excluir", command=lambda: excluindo_pet(entry_id), **estilo_botao)
    btn_salvar.pack(pady=10)
    
    btn_voltar = tk.Button(root, text="Voltar", command=voltar_menu, **estilo_botao)
    btn_voltar.pack(pady=10)

def excluindo_pet(entry_id):
    id= entry_id.get()
    try:
        tirar= f'DELETE FROM pet WHERE id={id}'
        cursor.execute(tirar)
        connector.commit()
        messagebox.showinfo("Sucesso", "pet excluido com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao excluir pet: {e}")
def atualizar_pet():
    esconder_menu_cliente()
    lbl_id = tk.Label(root, text="ID:")
    lbl_id.pack(pady=5)
    entry_id = tk.Entry(root)
    entry_id.pack(pady=5)


    lbl_nome = tk.Label(root, text="Nome:")
    lbl_nome.pack(pady=5)
    entry_nome = tk.Entry(root)
    entry_nome.pack(pady=5)


    lbl_raca = tk.Label(root, text="Raça:")
    lbl_raca.pack(pady=5)
    entry_raca = tk.Entry(root)
    entry_raca.pack(pady=5)

    lbl_especie = tk.Label(root, text="Especie:")
    lbl_especie.pack(pady=5)
    entry_especie = tk.Entry(root)
    entry_especie.pack(pady=5)


    btn_atualizar = tk.Button(root, text="Atualizar", command=lambda: atualizando_pet(entry_id,entry_nome,entry_raca,entry_especie), **estilo_botao)
    btn_atualizar.pack(pady=10)

    btn_voltar = tk.Button(root, text="Voltar", command=voltar_menu, **estilo_botao)
    btn_voltar.pack(pady=10)
def atualizando_pet(entry_id,entry_nome,entry_raca,entry_especie):
    id= entry_id.get()
    nome= entry_nome.get()
    raca= entry_raca.get()
    especie= entry_especie.get()
    try:
        trocar= f'UPDATE pet SET nome="{nome}",raca="{raca}",especie="{especie}" WHERE id={id}'
        cursor.execute(trocar)
        connector.commit()
        messagebox.showinfo("Sucesso", "pet atualizado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao atualizar pet: {e}")
def pesquisar_pet():
    esconder_menu_cliente()
    lbl_id = tk.Label(root, text="ID de pesquisa:")
    lbl_id.pack(pady=5)
    entry_id = tk.Entry(root)
    entry_id.pack(pady=5)


    btn_pesquisar = tk.Button(root, text="Pesquisa", command=lambda: pesquisando_pet(entry_id), **estilo_botao)
    btn_pesquisar.pack(pady=10)

    btn_voltar = tk.Button(root, text="Voltar", command=voltar_menu, **estilo_botao)
    btn_voltar.pack(pady=10)
def pesquisando_pet(entry_id):
        id=entry_id.get()
        try:
            cursor.execute(f"SELECT * FROM pet WHERE id = '{id}'")
            pet = cursor.fetchone()
            if pet:
                messagebox.showinfo("Resultado", f"Pet encontrado:\nID: {pet[0]}\nNome: {pet[1]}\nRaça: {pet[2]}\nEspecie: {pet[3]}")
            else:
                messagebox.showinfo("Resultado", "Nenhum pet encontrado com esse ID.")
            voltar_menu()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao pesquisar pet: {e}")

def cadastrar_produto():

    esconder_menu_cliente()

    lbl_nome = tk.Label(root, text="Nome:")
    lbl_nome.pack(pady=5)
    entry_nome = tk.Entry(root)
    entry_nome.pack(pady=5)


    lbl_id = tk.Label(root, text="ID:")
    lbl_id.pack(pady=5)
    entry_id = tk.Entry(root)
    entry_id.pack(pady=5)


    lbl_custo = tk.Label(root, text="Custo:")
    lbl_custo.pack(pady=5)
    entry_custo = tk.Entry(root)
    entry_custo.pack(pady=5)

    lbl_estoque = tk.Label(root, text="Em estoque:")
    lbl_estoque.pack(pady=5)
    entry_estoque = tk.Entry(root)
    entry_estoque.pack(pady=5)


    btn_salvar = tk.Button(root, text="Mandar", command=lambda: cadastrando_produto(entry_id,entry_nome,entry_custo,entry_estoque), **estilo_botao)
    btn_salvar.pack(pady=10)

    btn_voltar = tk.Button(root, text="Voltar", command=voltar_menu, **estilo_botao)
    btn_voltar.pack(pady=10)

def cadastrando_produto(entry_id,entry_nome,entry_custo,entry_estoque):
    id= entry_id.get()
    nome= entry_nome.get()
    custo= entry_custo.get()
    estoque= entry_estoque.get()
    try:
        mandar= f'INSERT INTO produto(id,nome,custo,estoque) VALUES ({id},"{nome}",{custo},{estoque})'
        cursor.execute(mandar)
        connector.commit()
        messagebox.showinfo("Sucesso", "produto cadastrado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao cadastrar produto: {e}")
def excluir_produto():
    esconder_menu_cliente()
    
    lbl_id = tk.Label(root, text="ID:")
    lbl_id.pack(pady=5)
    entry_id = tk.Entry(root)
    entry_id.pack(pady=5)


    btn_salvar = tk.Button(root, text="Excluir", command=lambda: excluindo_produto(entry_id), **estilo_botao)
    btn_salvar.pack(pady=10)
    
    btn_voltar = tk.Button(root, text="Voltar", command=voltar_menu, **estilo_botao)
    btn_voltar.pack(pady=10)

def excluindo_produto(entry_id):
    id= entry_id.get()
    try:
        tirar= f'DELETE FROM produto WHERE id={id}'
        cursor.execute(tirar)
        connector.commit()
        messagebox.showinfo("Sucesso", "produto excluido com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao excluir produto: {e}")
def atualizar_produto():
    esconder_menu_cliente()


    lbl_nome = tk.Label(root, text="Nome:")
    lbl_nome.pack(pady=5)
    entry_nome = tk.Entry(root)
    entry_nome.pack(pady=5)


    lbl_id = tk.Label(root, text="ID:")
    lbl_id.pack(pady=5)
    entry_id = tk.Entry(root)
    entry_id.pack(pady=5)


    lbl_custo = tk.Label(root, text="Custo:")
    lbl_custo.pack(pady=5)
    entry_custo = tk.Entry(root)
    entry_custo.pack(pady=5)


    lbl_estoque = tk.Label(root, text="Em estoque:")
    lbl_estoque.pack(pady=5)
    entry_estoque = tk.Entry(root)
    entry_estoque.pack(pady=5)


    btn_salvar = tk.Button(root, text="Mandar", command=lambda: atualizando_produto(entry_id,entry_nome,entry_custo,entry_estoque), **estilo_botao)
    btn_salvar.pack(pady=10)


    btn_voltar = tk.Button(root, text="Voltar", command=voltar_menu, **estilo_botao)
    btn_voltar.pack(pady=10)

def atualizando_produto(entry_id,entry_nome,entry_custo,entry_estoque):
    id= entry_id.get()
    nome= entry_nome.get()
    custo= entry_custo.get()
    estoque= entry_estoque.get()
    try:
        trocar= f'UPDATE produto SET nome="{nome}",custo={custo},estoque={estoque} WHERE id={id}'
        cursor.execute(trocar)
        connector.commit()
        messagebox.showinfo("Sucesso", "produto atualizado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao atualizar produto: {e}")
def pesquisar_produto():
    esconder_menu_cliente()
    lbl_id = tk.Label(root, text="ID de pesquisa:")
    lbl_id.pack(pady=5)
    entry_id = tk.Entry(root)
    entry_id.pack(pady=5)


    btn_pesquisar = tk.Button(root, text="Pesquisa", command=lambda: pesquisando_produto(entry_id), **estilo_botao)
    btn_pesquisar.pack(pady=10)

    btn_voltar = tk.Button(root, text="Voltar", command=voltar_menu, **estilo_botao)
    btn_voltar.pack(pady=10)

def pesquisando_produto(entry_id):
        id= entry_id.get()
        try:
            cursor.execute(f"SELECT * FROM produto WHERE id = '{id}'")
            produto = cursor.fetchone()
            if produto:
                messagebox.showinfo("Resultado", f"produto encontrado:\nID: {produto[0]}\nNome: {produto[1]}\nCusto: {produto[2]}\nEm estoque: {produto[3]}")
            else:
                messagebox.showinfo("Resultado", "Nenhum produto encontrado com esse ID.")
            voltar_menu()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao pesquisar produto: {e}")

def cadastrar_servico():
    
    esconder_menu_cliente()


    lbl_nome = tk.Label(root, text="Nome:")
    lbl_nome.pack(pady=5)
    entry_nome = tk.Entry(root)
    entry_nome.pack(pady=5)


    lbl_id = tk.Label(root, text="ID:")
    lbl_id.pack(pady=5)
    entry_id = tk.Entry(root)
    entry_id.pack(pady=5)

    lbl_cpf = tk.Label(root, text="Custo:")
    lbl_cpf.pack(pady=5)
    entry_custo = tk.Entry(root)
    entry_custo.pack(pady=5)


    btn_salvar = tk.Button(root, text="Mandar", command=lambda: cadastrando_servico(entry_id,entry_nome,entry_custo), **estilo_botao)
    btn_salvar.pack(pady=10)


    btn_voltar = tk.Button(root, text="Voltar", command=voltar_menu, **estilo_botao)
    btn_voltar.pack(pady=10)

def cadastrando_servico(entry_id,entry_nome,entry_custo):
    id= entry_id.get()
    nome= entry_nome.get()
    custo= entry_custo.get()
    try:
        mandar= f'INSERT INTO servico(id,nome,custo) VALUES ({id},"{nome}",{custo})'
        cursor.execute(mandar)
        connector.commit()
        messagebox.showinfo("Sucesso", "serviço cadastrado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao cadastrar serviço: {e}")
def excluir_servico():
    esconder_menu_cliente()
    
    lbl_id = tk.Label(root, text="ID:")
    lbl_id.pack(pady=5)
    entry_id = tk.Entry(root)
    entry_id.pack(pady=5)


    btn_salvar = tk.Button(root, text="Excluir", command=lambda: excluindo_servico(entry_id), **estilo_botao)
    btn_salvar.pack(pady=10)
    
    btn_voltar = tk.Button(root, text="Voltar", command=voltar_menu, **estilo_botao)
    btn_voltar.pack(pady=10)
def excluindo_servico(entry_id):
    id= entry_id.get()
    try:
        tirar= f'DELETE FROM servico WHERE id={id}'
        cursor.execute(tirar)
        connector.commit()
        messagebox.showinfo("Sucesso", "serviço excluido com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao excluir serviço: {e}")
def atualizar_servico():
    esconder_menu_cliente()


    lbl_nome = tk.Label(root, text="Nome:")
    lbl_nome.pack(pady=5)
    entry_nome = tk.Entry(root)
    entry_nome.pack(pady=5)


    lbl_id = tk.Label(root, text="ID:")
    lbl_id.pack(pady=5)
    entry_id = tk.Entry(root)
    entry_id.pack(pady=5)


    lbl_cpf = tk.Label(root, text="Custo:")
    lbl_cpf.pack(pady=5)
    entry_custo = tk.Entry(root)
    entry_custo.pack(pady=5)


    btn_salvar = tk.Button(root, text="Mandar", command=lambda: atualizando_servico(entry_id,entry_nome,entry_custo), **estilo_botao)
    btn_salvar.pack(pady=10)


    btn_voltar = tk.Button(root, text="Voltar", command=voltar_menu, **estilo_botao)
    btn_voltar.pack(pady=10)
def atualizando_servico(entry_id,entry_nome,entry_custo):
    id= entry_id.get()
    nome= entry_nome.get()
    custo= entry_custo.get()
    try:
        trocar= f'UPDATE servico SET nome="{nome}",custo={custo} WHERE id={id}'
        cursor.execute(trocar)
        connector.commit()
        messagebox.showinfo("Sucesso", "serviço atualizado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao atualizar serviço: {e}")
def pesquisar_servico():
    esconder_menu_cliente()
    lbl_id = tk.Label(root, text="ID de pesquisa:")
    lbl_id.pack(pady=5)
    entry_id = tk.Entry(root)
    entry_id.pack(pady=5)


    btn_pesquisar = tk.Button(root, text="Pesquisa", command=lambda: pesquisando_servico(entry_id), **estilo_botao)
    btn_pesquisar.pack(pady=10)

    btn_voltar = tk.Button(root, text="Voltar", command=voltar_menu, **estilo_botao)
    btn_voltar.pack(pady=10)
def pesquisando_servico(entry_id):
        id=entry_id.get()
        try:
            cursor.execute(f"SELECT * FROM servico WHERE id = '{id}'")
            servico = cursor.fetchone()
            if servico:
                messagebox.showinfo("Resultado", f"Serviço encontrado:\nID: {servico[0]}\nNome: {servico[1]}\nCusto: {servico[2]}")
            else:
                messagebox.showinfo("Resultado", "Nenhum serviço encontrado com esse ID.")
            voltar_menu()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao pesquisar serviço: {e}")
    
def voltar_menu():

    for widget in root.winfo_children():
        widget.pack_forget()


    btn_cliente.pack(pady=5)
    btn_pets.pack(pady=5)
    btn_produtos.pack(pady=5)
    btn_servicos.pack(pady=5)

def menu_cliente():
    # Esconde os botões principais
    esconder_menu_cliente()

    # Criar os botões do menu de clientes
    btn_cadastrar = tk.Button(root, text="Cadastrar Cliente", command=cadastrar_cliente, **estilo_botao)
    btn_cadastrar.pack(pady=5)

    btn_atualizar = tk.Button(root, text="Atualizar Cliente", command=atualizar_cliente, **estilo_botao)
    btn_atualizar.pack(pady=5)

    btn_excluir = tk.Button(root, text="Excluir Cliente", command=excluir_cliente, **estilo_botao)
    btn_excluir.pack(pady=5)

    btn_pesquisar = tk.Button(root, text="Pesquisar Cliente", command=pesquisar_cliente, **estilo_botao)
    btn_pesquisar.pack(pady=5)

    # Criar o botão Voltar
    btn_voltar = tk.Button(root, text="Voltar", command=voltar_menu, **estilo_botao)
    btn_voltar.pack(pady=10)

def menu_pets():
    # Esconde os botões principais
    esconder_menu_cliente()

    # Criar os botões do menu de clientes
    btn_cadastrar = tk.Button(root, text="Cadastrar pet", command=cadastrar_pet, **estilo_botao)
    btn_cadastrar.pack(pady=5)

    btn_atualizar = tk.Button(root, text="Atualizar pet", command=atualizar_pet, **estilo_botao)
    btn_atualizar.pack(pady=5)

    btn_excluir = tk.Button(root, text="Excluir pet", command=excluir_pet, **estilo_botao)
    btn_excluir.pack(pady=5)

    btn_pesquisar = tk.Button(root, text="Pesquisar pet", command=pesquisar_pet, **estilo_botao)
    btn_pesquisar.pack(pady=5)

    # Criar o botão Voltar
    btn_voltar = tk.Button(root, text="Voltar", command=voltar_menu, **estilo_botao)
    btn_voltar.pack(pady=10)

def menu_produtos():
    # Esconde os botões principais
    esconder_menu_cliente()

    # Criar os botões do menu de clientes
    btn_cadastrar = tk.Button(root, text="Cadastrar produto", command=cadastrar_produto, **estilo_botao)
    btn_cadastrar.pack(pady=5)

    btn_atualizar = tk.Button(root, text="Atualizar produto", command=atualizar_produto, **estilo_botao)
    btn_atualizar.pack(pady=5)

    btn_excluir = tk.Button(root, text="Excluir produto", command=excluir_produto, **estilo_botao)
    btn_excluir.pack(pady=5)

    btn_pesquisar = tk.Button(root, text="Pesquisar produto", command=pesquisar_produto, **estilo_botao)
    btn_pesquisar.pack(pady=5)

    # Criar o botão Voltar
    btn_voltar = tk.Button(root, text="Voltar", command=voltar_menu, **estilo_botao)
    btn_voltar.pack(pady=10)

def menu_servicos():
    # Esconde os botões principais
    esconder_menu_cliente()

    # Criar os botões do menu de clientes
    btn_cadastrar = tk.Button(root, text="Cadastrar serviço", command=cadastrar_servico, **estilo_botao)
    btn_cadastrar.pack(pady=5)

    btn_atualizar = tk.Button(root, text="Atualizar serviço", command=atualizar_servico, **estilo_botao)
    btn_atualizar.pack(pady=5)

    btn_excluir = tk.Button(root, text="Excluir serviço", command=excluir_servico, **estilo_botao)
    btn_excluir.pack(pady=5)

    btn_pesquisar = tk.Button(root, text="Pesquisar serviço", command=pesquisar_servico, **estilo_botao)
    btn_pesquisar.pack(pady=5)

    # Criar o botão Voltar
    btn_voltar = tk.Button(root, text="Voltar", command=voltar_menu, **estilo_botao)
    btn_voltar.pack(pady=10)



def atualizar_cliente():
    atualizacao_cliente()

def excluir_cliente():
    excluicao_cliente()

def pesquisar_cliente():
    pesquisa_cliente()

# Configuração da janela principal
root = tk.Tk()
root.title("Página Inicial")
root.geometry("400x300")  # Definindo o tamanho da janela

# Título
titulo = tk.Label(root, text="Bem-vindo ao Sistema de Gerenciamento do seu Petshop!", font=("Arial", 16))
titulo.pack(pady=20)

# Botões principais
btn_cliente = tk.Button(root, text="Clientes", command=menu_cliente, **estilo_botao)
btn_cliente.pack(pady=5)

btn_pets = tk.Button(root, text="Pets", command=menu_pets, **estilo_botao)
btn_pets.pack(pady=5)

btn_produtos = tk.Button(root, text="Produtos", command=menu_produtos, **estilo_botao)
btn_produtos.pack(pady=5)

btn_servicos = tk.Button(root, text="Serviços", command=menu_servicos, **estilo_botao)
btn_servicos.pack(pady=5)

# Inicia a interface
root.mainloop()

#Link slides: https://www.canva.com/design/DAGXiJVKuwM/b0ECXlvyEtu5iCa-JNzlGw/edit
