from fastapi import FastAPI
from app.routes.events import router

app = FastAPI()
app.add_api_route(router)