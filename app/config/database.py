#banco de dados
from sqlalchemy import create_engine
from sqlalchemy import sessionmaker
from contextlib import contextmanager

#definindo parametros para acesso ao banco de dados.
db_user = "aluno"
db_password = ""aluno_senha"
db_name = "meu_banco_senai"
db_host = "localhost"
db_port = "3306"

#Endereço (URL) para conexão com banco de dados.
DATABASE_URL = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

#criando banco de dados.
db = create_engine(DATABASE_URL)

#criando conexão com banco de dados.
Session = sessionmaker(bind = db)
session = Session()

#Gerenciando conexão com banco de dados
@contextmanager
def get_db():
    db = Session()
    try:
        yield db #realiza operação no BD.
        db.commit()#salvando no BD.
    except Exception as erro