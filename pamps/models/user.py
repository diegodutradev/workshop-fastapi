from typing import Optional, List, TYPE_CHECKING
from pydantic import BaseModel, EmailStr, AnyUrl, Field as PydanticField
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import UniqueConstraint

from pamps.security import HashedPassword

if TYPE_CHECKING:
    from pamps.models.post import Post

class User(SQLModel, table=True):
    __tablename__ = "user"
    __table_args__ = (
        UniqueConstraint("username", name="uq_user_username"),
        UniqueConstraint("email", name="uq_user_email"),
    )

    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True)
    email: EmailStr
    password: HashedPassword  # Garante que seja compatível com banco
    avatar: Optional[str] = None  # ← Corrigido: usar str!
    bio: Optional[str] = Field(default=None, max_length=300)
    posts: List["Post"] = Relationship(back_populates="user")


class UserRequest(BaseModel):
    username: str
    email: EmailStr
    password: str
    avatar: Optional[AnyUrl] = None  # ← Mantém validação de URL
    bio: Optional[str] = PydanticField(default=None, max_length=300)

    def to_user(self) -> User:
        return User(
            username=self.username,
            email=self.email,
            password=HashedPassword.hash(self.password),
            avatar=str(self.avatar) if self.avatar else None,
            bio=self.bio
        )


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    avatar: Optional[AnyUrl] = None
    bio: Optional[str] = PydanticField(default=None, max_length=300)
