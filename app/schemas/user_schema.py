from datetime import date

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserBase(BaseModel):
    first_name: str = Field(min_length=1, max_length=50)
    last_name: str = Field(min_length=1, max_length=50)
    email: EmailStr
    age: int = Field(ge=0)
    address: str = Field(min_length=1, max_length=255)
    joining_date: date


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class UserResponse(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    is_registered: bool
