from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: str
    age: int
    vill: str
    state: str
    pin:int

class UserFilterDTO(BaseModel):
    name_start_with: Optional[str] = None
    name: Optional[str] = None
    name_end_with: Optional[str] = None
    age: Optional[int] = None
    age_gt: Optional[int] = None
    age_gte: Optional[int] = None
    age_lt: Optional[int] = None
    age_lte: Optional[int] = None
    vill: Optional[str] = None
    state: Optional[str] = None
    pin: Optional[int] = None

class UserUpdate(BaseModel):
    name: str | None = None
    email: str | None = None
    age: int | None = None
    vill: str | None = None
    state: str | None = None
    pin:int | None = None

class UserOut(BaseModel):
    id: int
    name: str
    email: str
    age: int
    vill: str
    state: str
    pin:int

    class Config:
        orm_mode = True
