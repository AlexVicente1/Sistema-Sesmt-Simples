import sqlite3

# Função para criar o banco de dados e a tabela
def create_db():
    # Conecta ou cria o banco de dados
    conn = sqlite3.connect('cadastros_sesmt.db')
    cursor = conn.cursor()

    # Criação da tabela se ela não existir mas exitirá ok? 
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cadastros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        endereco TEXT,
        empresa TEXT,
        tipo_sanguineo TEXT,
        data_exame TEXT,
        telefone TEXT,
        email TEXT,
        rg TEXT,
        cpf TEXT,
        funcao TEXT,
        dependentes INTEGER
    );
    ''')

    conn.commit()  # Salva as alterações
    conn.close()  # Fecha a conexão

create_db()  # Chama a função para criar o banco
