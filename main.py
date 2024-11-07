# .txt
#banco de dados
# SQLit

#SQL
#linguagem de consulta de estrutura

#select * from clientes
#nome, sobrenome, idade
#ORM

import os
from sqlalchemy import create_engine, column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

#criando bando de dados.
MEU_BANCO =  create_engine("sqlite:///meubanco.db")

#criando conexão com o banco de dados
Session = sessionmaker(bind=MEU_BANCO)
session = Session()

#I/O
#I = input(entrada)
#O = output(saída)

#criando tabela.
Base = declarative_base()
class usuario(Base):
    _tablename_ = "usuarios"

    # Criando campos da tabela
    id = column("id", Integer, primary_key = True, autoincrement =True)
    nome = column("nome", String)
    email = column("email", String)
    senha = column("senha", String)

    #Definindo atributos da classe.
    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha
    
#criando tabela no banco de dados.
Base.metadata.create_all(bind=MEU_BANCO)

#Salvar no banco de dados.
usuario = Usuario("Marta", "marta@gmail.com", "123")
session.add(usuario)
session.commit()

#listando todos os usuarios do banco de dados.
print("\nExibindo todos os usuarios do banco de dados. ")
lista_usuarios = session.query(usuario).all()

for usuario in lista_usuarios:
    print(f"{usuario.id} - {usuario.nome} - {usuario.senha}")

#fechando conexão.
session.close()