# uvicorn main:app --reload para rodar o nosso codigo
from fastapi import FastAPI

app = FastAPI()

from auth_routes import auth_router
from orders_routes import order_router

# Incluir todas as endpoints/rotas que vem desses outros arquivos
app.include_router(auth_router)
app.include_router(order_router)

