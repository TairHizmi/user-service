from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.clients.poll_client import PollClient
from app.database import get_db
from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserCreate, UserResponse, UserUpdate
from app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["Users"])


def get_user_service(db: Session = Depends(get_db)) -> UserService:
    return UserService(UserRepository(db), PollClient())


@router.post("", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(data: UserCreate, service: UserService = Depends(get_user_service)):
    return service.create_user(data)


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, service: UserService = Depends(get_user_service)):
    return service.get_user(user_id)


@router.put("/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int, data: UserUpdate, service: UserService = Depends(get_user_service)
):
    return service.update_user(user_id, data)


@router.put("/{user_id}/register", response_model=UserResponse)
def register_user(user_id: int, service: UserService = Depends(get_user_service)):
    return service.register_user(user_id)


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, service: UserService = Depends(get_user_service)):
    service.delete_user(user_id)
