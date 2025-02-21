-- criando banco de dados e tabela
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
