"""Security utilities"""
from passlib.context import CryptContext
from pydantic import GetCoreSchemaHandler
from pydantic_core import core_schema
from pydantic_core.core_schema import ValidationInfo

from pamps.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = settings.security.secret_key
ALGORITHM = settings.security.algorithm


def verify_password(plain_password, hashed_password) -> bool:
    """Verifies a hash against a password"""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password) -> str:
    """Generates a hash from plain text"""
    return pwd_context.hash(password)


class HashedPassword(str):
    """Takes a plain text password and hashes it."""

    @classmethod
    def hash(cls, value: str) -> "HashedPassword":
        """Hashes a plain text password into HashedPassword"""
        if not isinstance(value, str):
            raise TypeError("string required")
        hashed = get_password_hash(value)
        return cls(hashed)

    @classmethod
    def __get_pydantic_core_schema__(cls, source, handler: GetCoreSchemaHandler):
        return core_schema.no_info_before_validator_function(
            cls.validate,
            core_schema.str_schema()
        )

    @classmethod
    def validate(cls, value: str, info: ValidationInfo) -> "HashedPassword":
        """Pydantic automatic validator"""
        if not isinstance(value, str):
            raise TypeError("string required")
        hashed = get_password_hash(value)
        return cls(hashed)
