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


    btn_salvar = tk.Button(root, text="Mandar", width=20, height=2, command=lambda:cadastrando_cliente(entry_nome,entry_id,entry_cpf,entry_endereco))
    btn_salvar.pack(pady=10)


    btn_voltar = tk.Button(root, text="Voltar", width=20, height=2, command=voltar_menu)
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


    btn_salvar = tk.Button(root, text="excluir", width=20, height=2, command=lambda: excluindo_cliente(entry_id))
    btn_salvar.pack(pady=10)
    

    btn_voltar = tk.Button(root, text="Voltar", width=20, height=2, command=voltar_menu)
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


    btn_atualizar = tk.Button(root, text="atualizar", width=20, height=2, command=lambda: atualizando_cliente(entry_id,entry_nome,entry_cpf,entry_endereco))
    btn_atualizar.pack(pady=10)

    btn_voltar = tk.Button(root, text="Voltar", width=20, height=2, command=voltar_menu)
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


    btn_pesquisar = tk.Button(root, text="pesquisa", width=20, height=2, command=lambda: pesquisando_cliente(entry_id))
    btn_pesquisar.pack(pady=10)

    btn_voltar = tk.Button(root, text="Voltar", width=20, height=2, command=voltar_menu)
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


    btn_salvar = tk.Button(root, text="Mandar", width=20, height=2, command=lambda: cadastrando_pet(entry_id,entry_nome,entry_raca))
    btn_salvar.pack(pady=10)


    btn_voltar = tk.Button(root, text="Voltar", width=20, height=2, command=voltar_menu)
    btn_voltar.pack(pady=10)


def cadastrando_pet(entry_id,entry_nome,entry_raca):
    id= entry_id.get()
    nome= entry_nome.get()
    raca=entry_raca.get()
    try:
        mandar= f'INSERT INTO pet(id,nome,raca) VALUES ({id},"{nome}","{raca}")'
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


    btn_salvar = tk.Button(root, text="excluir", width=20, height=2, command=lambda: excluindo_pet(entry_id))
    btn_salvar.pack(pady=10)
    
    btn_voltar = tk.Button(root, text="Voltar", width=20, height=2, command=voltar_menu)
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


    lbl_cpf = tk.Label(root, text="Raça:")
    lbl_cpf.pack(pady=5)
    entry_raca = tk.Entry(root)
    entry_raca.pack(pady=5)


    btn_atualizar = tk.Button(root, text="atualizar", width=20, height=2, command=lambda: atualizando_pet(entry_id,entry_nome,entry_raca))
    btn_atualizar.pack(pady=10)

    btn_voltar = tk.Button(root, text="Voltar", width=20, height=2, command=voltar_menu)
    btn_voltar.pack(pady=10)
def atualizando_pet(entry_id,entry_nome,entry_raca):
    id= entry_id.get()
    nome= entry_nome.get()
    raca= entry_raca.get()
    try:
        trocar= f'UPDATE pet SET nome="{nome}",raca={raca} WHERE id={id}'
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


    btn_pesquisar = tk.Button(root, text="pesquisa", width=20, height=2, command=lambda: pesquisando_pet(entry_id))
    btn_pesquisar.pack(pady=10)

    btn_voltar = tk.Button(root, text="Voltar", width=20, height=2, command=voltar_menu)
    btn_voltar.pack(pady=10)
def pesquisando_pet(entry_id):
        id=entry_id.get()
        try:
            cursor.execute(f"SELECT * FROM pet WHERE id = '{id}'")
            pet = cursor.fetchone()
            if pet:
                messagebox.showinfo("Resultado", f"Pet encontrado:\nID: {pet[0]}\nNome: {pet[1]}\nRaça: {pet[2]}")
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


    lbl_cpf = tk.Label(root, text="custo:")
    lbl_cpf.pack(pady=5)
    entry_custo = tk.Entry(root)
    entry_custo.pack(pady=5)


    btn_salvar = tk.Button(root, text="Mandar", width=20, height=2, command=lambda: cadastrando_produto(entry_id,entry_nome,entry_custo))
    btn_salvar.pack(pady=10)

    btn_voltar = tk.Button(root, text="Voltar", width=20, height=2, command=voltar_menu)
    btn_voltar.pack(pady=10)

def cadastrando_produto(entry_id,entry_nome,entry_custo):
    id= entry_id.get()
    nome= entry_nome.get()
    custo= entry_custo.get()
    try:
        mandar= f'INSERT INTO produto(id,nome,custo) VALUES ({id},"{nome}",{custo})'
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


    btn_salvar = tk.Button(root, text="excluir", width=20, height=2, command=lambda: excluindo_produto(entry_id))
    btn_salvar.pack(pady=10)
    
    btn_voltar = tk.Button(root, text="Voltar", width=20, height=2, command=voltar_menu)
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


    lbl_cpf = tk.Label(root, text="custo:")
    lbl_cpf.pack(pady=5)
    entry_custo = tk.Entry(root)
    entry_custo.pack(pady=5)


    btn_salvar = tk.Button(root, text="Mandar", width=20, height=2, command=lambda: atualizando_produto(entry_id,entry_nome,entry_custo))
    btn_salvar.pack(pady=10)


    btn_voltar = tk.Button(root, text="Voltar", width=20, height=2, command=voltar_menu)
    btn_voltar.pack(pady=10)

def atualizando_produto(entry_id,entry_nome,entry_custo):
    id= entry_id.get()
    nome= entry_nome.get()
    custo= entry_custo.get()
    try:
        trocar= f'UPDATE produto SET nome="{nome}",custo={custo} WHERE id={id}'
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


    btn_pesquisar = tk.Button(root, text="pesquisa", width=20, height=2, command=lambda: pesquisando_produto(entry_id))
    btn_pesquisar.pack(pady=10)

    btn_voltar = tk.Button(root, text="Voltar", width=20, height=2, command=voltar_menu)
    btn_voltar.pack(pady=10)

def pesquisando_produto(entry_id):
        id= entry_id.get()
        try:
            cursor.execute(f"SELECT * FROM produto WHERE id = '{id}'")
            produto = cursor.fetchone()
            if produto:
                messagebox.showinfo("Resultado", f"produto encontrado:\nID: {produto[0]}\nNome: {produto[1]}\nCusto: {produto[2]}")
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

    lbl_cpf = tk.Label(root, text="custo:")
    lbl_cpf.pack(pady=5)
    entry_custo = tk.Entry(root)
    entry_custo.pack(pady=5)


    btn_salvar = tk.Button(root, text="Mandar", width=20, height=2, command=lambda: cadastrando_servico(entry_id,entry_nome,entry_custo))
    btn_salvar.pack(pady=10)


    btn_voltar = tk.Button(root, text="Voltar", width=20, height=2, command=voltar_menu)
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


    btn_salvar = tk.Button(root, text="excluir", width=20, height=2, command=lambda: excluindo_servico(entry_id))
    btn_salvar.pack(pady=10)
    
    btn_voltar = tk.Button(root, text="Voltar", width=20, height=2, command=voltar_menu)
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


    lbl_cpf = tk.Label(root, text="custo:")
    lbl_cpf.pack(pady=5)
    entry_custo = tk.Entry(root)
    entry_custo.pack(pady=5)


    btn_salvar = tk.Button(root, text="Mandar", width=20, height=2, command=lambda: atualizando_servico(entry_id,entry_nome,entry_custo))
    btn_salvar.pack(pady=10)


    btn_voltar = tk.Button(root, text="Voltar", width=20, height=2, command=voltar_menu)
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


    btn_pesquisar = tk.Button(root, text="pesquisa", width=20, height=2, command=lambda: pesquisando_servico(entry_id))
    btn_pesquisar.pack(pady=10)

    btn_voltar = tk.Button(root, text="Voltar", width=20, height=2, command=voltar_menu)
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
    btn_cadastrar = tk.Button(root, text="Cadastrar Cliente", width=20, height=2, command=cadastrar_cliente)
    btn_cadastrar.pack(pady=5)

    btn_atualizar = tk.Button(root, text="Atualizar Cliente", width=20, height=2, command=atualizar_cliente)
    btn_atualizar.pack(pady=5)

    btn_excluir = tk.Button(root, text="Excluir Cliente", width=20, height=2, command=excluir_cliente)
    btn_excluir.pack(pady=5)

    btn_pesquisar = tk.Button(root, text="Pesquisar Cliente", width=20, height=2, command=pesquisar_cliente)
    btn_pesquisar.pack(pady=5)

    # Criar o botão Voltar
    btn_voltar = tk.Button(root, text="Voltar", width=20, height=2, command=voltar_menu)
    btn_voltar.pack(pady=10)

def menu_pets():
    # Esconde os botões principais
    esconder_menu_cliente()

    # Criar os botões do menu de clientes
    btn_cadastrar = tk.Button(root, text="Cadastrar pet", width=20, height=2, command=cadastrar_pet)
    btn_cadastrar.pack(pady=5)

    btn_atualizar = tk.Button(root, text="Atualizar pet", width=20, height=2, command=atualizar_pet)
    btn_atualizar.pack(pady=5)

    btn_excluir = tk.Button(root, text="Excluir pet", width=20, height=2, command=excluir_pet)
    btn_excluir.pack(pady=5)

    btn_pesquisar = tk.Button(root, text="Pesquisar pet", width=20, height=2, command=pesquisar_pet)
    btn_pesquisar.pack(pady=5)

    # Criar o botão Voltar
    btn_voltar = tk.Button(root, text="Voltar", width=20, height=2, command=voltar_menu)
    btn_voltar.pack(pady=10)

def menu_produtos():
    # Esconde os botões principais
    esconder_menu_cliente()

    # Criar os botões do menu de clientes
    btn_cadastrar = tk.Button(root, text="Cadastrar produto", width=20, height=2, command=cadastrar_produto)
    btn_cadastrar.pack(pady=5)

    btn_atualizar = tk.Button(root, text="Atualizar produto", width=20, height=2, command=atualizar_produto)
    btn_atualizar.pack(pady=5)

    btn_excluir = tk.Button(root, text="Excluir produto", width=20, height=2, command=excluir_produto)
    btn_excluir.pack(pady=5)

    btn_pesquisar = tk.Button(root, text="Pesquisar produto", width=20, height=2, command=pesquisar_produto)
    btn_pesquisar.pack(pady=5)

    # Criar o botão Voltar
    btn_voltar = tk.Button(root, text="Voltar", width=20, height=2, command=voltar_menu)
    btn_voltar.pack(pady=10)

def menu_servicos():
    # Esconde os botões principais
    esconder_menu_cliente()

    # Criar os botões do menu de clientes
    btn_cadastrar = tk.Button(root, text="Cadastrar serviço", width=20, height=2, command=cadastrar_servico)
    btn_cadastrar.pack(pady=5)

    btn_atualizar = tk.Button(root, text="Atualizar serviço", width=20, height=2, command=atualizar_servico)
    btn_atualizar.pack(pady=5)

    btn_excluir = tk.Button(root, text="Excluir serviço", width=20, height=2, command=excluir_servico)
    btn_excluir.pack(pady=5)

    btn_pesquisar = tk.Button(root, text="Pesquisar serviço", width=20, height=2, command=pesquisar_servico)
    btn_pesquisar.pack(pady=5)

    # Criar o botão Voltar
    btn_voltar = tk.Button(root, text="Voltar", width=20, height=2, command=voltar_menu)
    btn_voltar.pack(pady=10)

# Funções para as outras opções (Pets, Produtos e Serviços)
def exibir_pets():
    messagebox.showinfo("Pets", "Tela de Pets")

def exibir_produtos():
    messagebox.showinfo("Produtos", "Tela de Produtos")

def exibir_servicos():
    messagebox.showinfo("Serviços", "Tela de Serviços")


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
titulo = tk.Label(root, text="Bem-vindo ao Sistema", font=("Arial", 16))
titulo.pack(pady=20)

# Botões principais
btn_cliente = tk.Button(root, text="Clientes", width=20, height=2, command=menu_cliente)
btn_cliente.pack(pady=5)

btn_pets = tk.Button(root, text="Pets", width=20, height=2, command=menu_pets)
btn_pets.pack(pady=5)

btn_produtos = tk.Button(root, text="Produtos", width=20, height=2, command=menu_produtos)
btn_produtos.pack(pady=5)

btn_servicos = tk.Button(root, text="Serviços", width=20, height=2, command=menu_servicos)
btn_servicos.pack(pady=5)

# Inicia a interface
root.mainloop()
