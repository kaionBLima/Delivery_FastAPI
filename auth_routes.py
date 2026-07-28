from fastapi import APIRouter, Depends
from models import Usuario
from dependencies import pegar_sessao

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def autenticar():
    """
    Essa é a rota padrão de autenticação do sistema
    """
    return {"Mensagem": "Você acessou a rota padrão de autenticação", "Autenticado" : False}

@auth_router.post("/criar_conta")
async def criar_conta(email: str, senha:str, nome: str, session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email==email).first()
    if usuario:
       # ja existe um usuario com esse e-mail
       return {"mensagem" : "ja existe um usuario com esse e-mail"}
    else:
        novo_usuario = Usuario(nome, email, senha)
        session.add(novo_usuario)
        session.commit()
        return {"Mensagem" : "Usuário cadastrado com sucesso"}