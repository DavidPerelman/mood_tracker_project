from fastapi import FastAPI
from api.routers.mood import router as mood_router

app = FastAPI()

app.include_router(mood_router)
