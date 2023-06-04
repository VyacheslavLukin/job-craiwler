from fastapi import FastAPI
from src.client_api.endpoints import router

app = FastAPI()

app.include_router(router)
