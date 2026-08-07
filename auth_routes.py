from fastapi import APIRouter, Depends, HTTPException
from models import Usuario
from dependencies import pegar_sessao
from main import bcrypt_context
from schemas import UsuarioSchema
from sqlalchemy.orm import Session

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def autenticar():
    """
    Essa é a rota padrão de autenticação do sistema
    """
    return {"Mensagem": "Você acessou a rota padrão de autenticação", "Autenticado" : False}

@auth_router.post("/criar_conta")
async def criar_conta(usuario_schema: UsuarioSchema, session : Session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email==usuario_schema.email).first()
    if usuario:
       # ja existe um usuario com esse e-mail
       raise HTTPException(status_code=400, detail="E-mail do usuário já cadastrado")
    else:
        senha_criptografada = bcrypt_context.hash(usuario_schema.senha)
        novo_usuario = Usuario(usuario_schema.nome, usuario_schema.email, senha_criptografada, usuario_schema.ativo, usuario_schema.admin)
        session.add(novo_usuario)
        session.commit()
        return {"Mensagem" : f"Usuário cadastrado com sucesso {email}"}