from fastapi import APIRouter, Depends, HTTPException, status
from .schemas import UserCreate, User, Token
from .service import AuthService
from src.database import DataBase

router = APIRouter()


@router.post("/register", response_model=User)
async def register(user: UserCreate):
    """
    用户注册路由。

    :param user: UserCreate 实例，包含用户注册信息。
    :return: 注册的用户信息。
    """
    return await AuthService.create_user(user)


@router.post("/login", response_model=Token)
async def login(user: UserCreate):
    """
    用户登录路由。

    :param user: UserCreate 实例，包含登录信息。
    :return: 包含JWT Token的响应。
    """
    user_in_db = await AuthService.authenticate_user(user.username, user.password)
    if not user_in_db:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    token = AuthService.create_access_token(data={"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}


@router.get("/users/me", response_model=User)
async def read_users_me(current_user: User = Depends(AuthService.get_current_user)):
    """
    获取当前登录用户的信息。

    :param current_user: 从JWT获取的当前用户。
    :return: 当前登录的用户信息。
    """
    return current_user
