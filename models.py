from sqlalchemy import createengine, Column, String, Integer, Boolean, Float, ForeignKey, PrimaryKeyConstraint
from sqlalchemy import declative_base
from sqlalchemy_utils.types import ChoiceType

# Criando table e o banco com sqlalchemy -----------------

#Conexão com banco de dados, como não temos nenhum externo, usamos o que criamos
db = createengine("sqlite:///banco.db")

#Base do banco de dados
Base = declative_base()

#Classe/Tabelas do banco de dados
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String, nullable=False)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)
    admin = Column("admin", Boolean, default=False)

    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin

class Pedido(Base):
    __tablename__ = "pedido"

    STATUS_PEDIDOS = (
        ("PENDENTE", "PENDENTE")
        ("CANCELADO", "CANCELADO")
        ("FINALIZADO", "FINALIZADO")
    )

    id = Column("id", primary_key=True, autoincrement=True)
    status = Column("status", String, ChoiceType(choices=STATUS_PEDIDOS))
    usuario = Column("usuario", ForeignKey("usuarios.id"))
    preco = Column("preco", Float)

    def __init__(self, usuario, status="PENDENTE", preco=0):
        self.usuario = usuario
        self.preco = preco
        self.status = status
#Executa a criação dos metadados do banco (cria efetivamente o banco de dados)