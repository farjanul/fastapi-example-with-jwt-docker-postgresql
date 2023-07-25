# main.py
import os
from dotenv import load_dotenv
from urllib.request import Request

from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination

import app.models as models
from app.db.database import engine, SessionLocal
from app.routers import posts, users
from app.settings import Settings

models.user.Base.metadata.create_all(bind=engine)
models.post.Base.metadata.create_all(bind=engine)

load_dotenv()

settings = Settings()
app = FastAPI(title=settings.app_name)

app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv('ALLOW_HOST'),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


app.include_router(posts.router, prefix=settings.api_prefix)
app.include_router(users.router, prefix=settings.api_prefix)
add_pagination(app)  # important! add pagination to app
