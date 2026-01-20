from fastapi import FastAPI
from app.routes.events import router

app = FastAPI()
app.include_router(router)