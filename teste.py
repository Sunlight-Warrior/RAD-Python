import sqlite3

class CriacaoTabelas:
    def __init__(self, nome_banco):
        self.nome_banco = nome_banco
        self.conexao = None

    def conectar(self):
        
        self.conexao = sqlite3.connect(self.nome_banco)

    def desconectar(self):
        
        if self.conexao:
            self.conexao.close()
            self.conexao = None

    def criar_tabelas(self):
    
        if not self.conexao:
            raise Exception("Você precisa se conectar ao banco primeiro usando o método 'conectar()'.")

        cursor = self.conexao.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Enderecos(
                id_endereco INTEGER PRIMARY KEY AUTOINCREMENT,
                complemento VARCHAR(50) NOT NULL,
                estado CHAR(2) NOT NULL,
                cep CHAR(8) NOT NULL
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Alunos(
                id_aluno INTEGER PRIMARY KEY AUTOINCREMENT, 
                cpf CHAR(11) UNIQUE NOT NULL,
                nome VARCHAR(100) NOT NULL,
                rg VARCHAR(20) NOT NULL,
                data_nascimento DATE NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                telefone VARCHAR(20) NOT NULL,
                unidade VARCHAR(50) NOT NULL,
                id_endereco INTEGER NOT NULL,
                FOREIGN KEY (id_endereco) REFERENCES Enderecos(id_endereco)
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Professores(
                id_professor INTEGER PRIMARY KEY AUTOINCREMENT,
                cpf CHAR(11) UNIQUE NOT NULL,
                nome VARCHAR(100) NOT NULL,
                rg VARCHAR(20) NOT NULL,
                data_nascimento DATE NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                telefone VARCHAR(20) NOT NULL,
                unidade VARCHAR(50) NOT NULL,
                id_endereco INTEGER NOT NULL,
                senha VARCHAR(25) NOT NULL,
                FOREIGN KEY (id_endereco) REFERENCES Enderecos(id_endereco)
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Funcionarios(
                id_funcionarios INTEGER PRIMARY KEY AUTOINCREMENT,
                cpf CHAR(11) UNIQUE NOT NULL,
                nome VARCHAR(100) NOT NULL,
                rg VARCHAR(20) NOT NULL,
                data_nascimento DATE NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                telefone VARCHAR(20) NOT NULL,
                unidade VARCHAR(50) NOT NULL,
                id_endereco INTEGER NOT NULL,
                senha VARCHAR(25) NOT NULL,
                FOREIGN KEY (id_endereco) REFERENCES Enderecos(id_endereco)
            );
        """)

        self.conexao.commit()
        cursor.close()
