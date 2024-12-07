from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import settings
from .api import greetings


# origins = [settings.FRONTEND_URL]
origins = ["*"]

app = FastAPI(title=settings.PROJECT_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
)

app.include_router(greetings.router, prefix="/v0/api/greetings", tags=["Greetings"])


@app.get("/")
async def root():
    return {"message": "Hello World"}
