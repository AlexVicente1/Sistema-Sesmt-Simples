import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime

# Função para salvar o cadastro no banco de dados
def save_data():
    nome = entry_nome.get()
    endereco = entry_endereco.get()
    empresa = entry_empresa.get()
    tipo_sanguineo = entry_tipo_sanguineo.get()
    data_exame = entry_data_exame.get()
    telefone = entry_telefone.get()
    email = entry_email.get()
    rg = entry_rg.get()
    cpf = entry_cpf.get()
    funcao = entry_funcao.get()
    dependentes = entry_dependentes.get()

    # Validação simples para garantir que todos os campos foram preenchidos
    if not all([nome, endereco, empresa, tipo_sanguineo, data_exame, telefone, email, rg, cpf, funcao, dependentes]):
        messagebox.showwarning("Aviso", "Todos os campos devem ser preenchidos!")
        return

    # Conectar ao banco de dados e salvar as informações
    conn = sqlite3.connect('cadastros_sesmt.db')
    cursor = conn.cursor()

    # Inserir dados no banco de dados
    cursor.execute('''
    INSERT INTO cadastros (nome, endereco, empresa, tipo_sanguineo, data_exame, telefone, email, rg, cpf, funcao, dependentes)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (nome, endereco, empresa, tipo_sanguineo, data_exame, telefone, email, rg, cpf, funcao, dependentes))

    conn.commit()  # Salvar alterações
    conn.close()  # Fechar a conexão

    # Exibir mensagem de sucesso
    messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")

    # Limpar os campos
    clear_fields()

# Função para limpar os campos de entrada
def clear_fields():
    entry_nome.delete(0, tk.END)
    entry_endereco.delete(0, tk.END)
    entry_empresa.delete(0, tk.END)
    entry_tipo_sanguineo.delete(0, tk.END)
    entry_data_exame.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_rg.delete(0, tk.END)
    entry_cpf.delete(0, tk.END)
    entry_funcao.delete(0, tk.END)
    entry_dependentes.delete(0, tk.END)

# Configuração da janela principal
root = tk.Tk()
root.title("Cadastro SESMT")
root.geometry("500x600")

# Labels e campos de entrada
label_nome = tk.Label(root, text="Nome:")
label_nome.grid(row=0, column=0, padx=10, pady=5)
entry_nome = tk.Entry(root, width=40)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

label_endereco = tk.Label(root, text="Endereço:")
label_endereco.grid(row=1, column=0, padx=10, pady=5)
entry_endereco = tk.Entry(root, width=40)
entry_endereco.grid(row=1, column=1, padx=10, pady=5)

label_empresa = tk.Label(root, text="Empresa:")
label_empresa.grid(row=2, column=0, padx=10, pady=5)
entry_empresa = tk.Entry(root, width=40)
entry_empresa.grid(row=2, column=1, padx=10, pady=5)

label_tipo_sanguineo = tk.Label(root, text="Tipo Sanguíneo:")
label_tipo_sanguineo.grid(row=3, column=0, padx=10, pady=5)
entry_tipo_sanguineo = tk.Entry(root, width=40)
entry_tipo_sanguineo.grid(row=3, column=1, padx=10, pady=5)

label_data_exame = tk.Label(root, text="Data do Exame (dd/mm/yyyy):")
label_data_exame.grid(row=4, column=0, padx=10, pady=5)
entry_data_exame = tk.Entry(root, width=40)
entry_data_exame.grid(row=4, column=1, padx=10, pady=5)

label_telefone = tk.Label(root, text="Telefone:")
label_telefone.grid(row=5, column=0, padx=10, pady=5)
entry_telefone = tk.Entry(root, width=40)
entry_telefone.grid(row=5, column=1, padx=10, pady=5)

label_email = tk.Label(root, text="Email:")
label_email.grid(row=6, column=0, padx=10, pady=5)
entry_email = tk.Entry(root, width=40)
entry_email.grid(row=6, column=1, padx=10, pady=5)

label_rg = tk.Label(root, text="RG:")
label_rg.grid(row=7, column=0, padx=10, pady=5)
entry_rg = tk.Entry(root, width=40)
entry_rg.grid(row=7, column=1, padx=10, pady=5)

label_cpf = tk.Label(root, text="CPF:")
label_cpf.grid(row=8, column=0, padx=10, pady=5)
entry_cpf = tk.Entry(root, width=40)
entry_cpf.grid(row=8, column=1, padx=10, pady=5)

label_funcao = tk.Label(root, text="Função:")
label_funcao.grid(row=9, column=0, padx=10, pady=5)
entry_funcao = tk.Entry(root, width=40)
entry_funcao.grid(row=9, column=1, padx=10, pady=5)

label_dependentes = tk.Label(root, text="Dependentes:")
label_dependentes.grid(row=10, column=0, padx=10, pady=5)
entry_dependentes = tk.Entry(root, width=40)
entry_dependentes.grid(row=10, column=1, padx=10, pady=5)

# Botão para salvar os dados
button_save = tk.Button(root, text="Salvar Cadastro", command=save_data, bg="#4CAF50", fg="white", font=("Arial", 14))
button_save.grid(row=11, column=0, columnspan=2, pady=20)

# Iniciar a interface gráfica
root.mainloop()
