from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.controllers.user_controller import router as user_router
from app.database import Base, engine
from app.models import user_model  # noqa: F401  (registers the table)


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title="User Service", lifespan=lifespan)
app.include_router(user_router)
