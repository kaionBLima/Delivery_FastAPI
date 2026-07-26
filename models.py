from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types import ChoiceType
#migration que iremos usar


# Criando table e o banco com sqlalchemy -----------------

#Conexão com banco de dados, como não temos nenhum externo, usamos o que criamos
db = create_engine("sqlite:///banco.db")

#Base do banco de dados
Base = declarative_base()

#Classe/Tabelas do banco de dados
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
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

    # STATUS_PEDIDOS = (
    #     ("PENDENTE", "PENDENTE"),
    #     ("CANCELADO", "CANCELADO"),
    #     ("FINALIZADO", "FINALIZADO")
    # )

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", String)
    usuario = Column("usuario", ForeignKey("usuarios.id"))
    preco = Column("preco", Float)

    def __init__(self, usuario, status="PENDENTE", preco=0):
        self.usuario = usuario
        self.preco = preco
        self.status = status

class ItemPedido(Base):
    __tablename__= "itens_pedido"

    # TAMANHO = (
    #     ("P", 'PEQUENO'),
    #     ("M", "MEDIO"),
    #     ("G", "GRANDE"),
    #     ("GG", "GIGANTE")
    # )

    # BEBIDA = (
    #     ("REFRIGERANTE", "REFRIGERANTE"),
    #     ("SUCO", "SUCO"),
    #     ("CERVEJA", "CERVEJA")
    # )

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    quantidade = Column("quantidade", Integer)
    sabor = Column("sabor", String)
    tamanho = Column("tamanho", String)
    preco_unitario = Column("preco", Float)
    pedido = Column("pedido", ForeignKey("pedido.id"))
    bebida = Column("bebida", String)

    def __init__(self, quantidade, sabor, tamanho, preco_unitario, pedido, bebida):
        self.quantidade = quantidade
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco = preco_unitario
        self.pedido = pedido
        self.bebida = bebida
#Executa a criação dos metadados do banco (cria efetivamente o banco de dados)