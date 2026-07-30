from models import db
from sqlalchemy.orm import sessionmaker


def pegar_sessao():
    try:    #tentar executar a função
        Session = sessionmaker(bind=db)
        session = Session() #instância de sessão
        yield session #Retorna ou pausa a sessão/instância 

    finally: #dando certo ou errado, eu finalizo a sessão
        session.close()