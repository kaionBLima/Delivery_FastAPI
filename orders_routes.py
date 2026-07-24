from fastapi import APIRouter

# crio primeiro a rota que importei dentro do arquivo main com o prefixo da endpoint para organização da rota
order_router = APIRouter(prefix="/pedidos", tags=["pedidos"])

@order_router.get("/")
async def pedidos():
    """
    Região para explicação do para quê cada rota é usada e qual a funcionalidade, caso a API seja pública
    """
    return {"Mensagem: Você acessou a rota de pedidos"}