from fastapi import HTTPException

from app.clients.poll_client import PollClient
from app.models.user_model import User
from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserCreate, UserUpdate


class UserService:
    def __init__(self, repository: UserRepository, poll_client: PollClient):
        self.repository = repository
        self.poll_client = poll_client

    def create_user(self, data: UserCreate) -> User:
        if self.repository.get_by_email(data.email):
            raise HTTPException(status_code=409, detail="Email already exists")
        user = User(**data.model_dump(), is_registered=False)
        return self.repository.create(user)

    def get_user(self, user_id: int) -> User:
        user = self.repository.get_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    def update_user(self, user_id: int, data: UserUpdate) -> User:
        user = self.get_user(user_id)
        existing = self.repository.get_by_email(data.email)
        if existing and existing.id != user_id:
            raise HTTPException(status_code=409, detail="Email already exists")
        for field, value in data.model_dump().items():
            setattr(user, field, value)
        return self.repository.update(user)

    def register_user(self, user_id: int) -> User:
        user = self.get_user(user_id)
        user.is_registered = True
        return self.repository.update(user)

    def delete_user(self, user_id: int) -> None:
        user = self.get_user(user_id)
        self.poll_client.delete_user_answers(user_id)
        self.repository.delete(user)
