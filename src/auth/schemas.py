# pydantic 模型
from pydantic import BaseModel, EmailStr
from typing import Optional


class UserCreate(BaseModel):
    """
    用户创建模型，用于用户注册。

    属性:
    - username: 用户名。
    - email: 电子邮件地址。
    - password: 密码。
    """
    username: str
    email: EmailStr
    password: str


class UserInDB(UserCreate):
    """
    数据库中的用户模型，继承自UserCreate。

    属性:
    - hashed_password: 加密后的密码。
    """
    hashed_password: str


class TokenData(BaseModel):
    """
    用于JWT认证的数据模型。

    属性:
    - username: 用户名。
    """
    username: Optional[str] = None


class User(BaseModel):
    # User模型的属性定义...
    username: str
    email: EmailStr
    hashed_password: str


class Token(BaseModel):
    # Token模型的属性定义...
    access_token: str
    token_type: str
