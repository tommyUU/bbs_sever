from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from .schemas import UserCreate, UserInDB, TokenData
from ..database import DataBase

# 定义全局变量
SECRET_KEY = "你的随机秘钥"  # 应替换为实际的秘钥
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class AuthService:
    """
    认证服务类，提供用户注册和登录的业务逻辑。

    方法:
    - create_user: 创建新用户。
    - authenticate_user: 验证用户登录。
    - create_access_token: 创建JWT访问令牌。
    - get_current_user: 从JWT令牌中获取当前用户。
    """

    @staticmethod
    async def create_user(user: UserCreate) -> UserInDB:
        """
        创建新用户。

        :param user: UserCreate实例，包含用户注册信息。
        :return: 新创建的UserInDB实例。
        """
        # 方法实现...

    @staticmethod
    async def authenticate_user(username: str, password: str) -> UserInDB:
        """
        验证用户登录。

        :param username: 用户名。
        :param password: 密码。
        :return: 验证成功的UserInDB实例。
        """
        # 方法实现...

    @staticmethod
    def create_access_token(data: dict, expires_delta: timedelta = None):
        """
        创建JWT访问令牌。

        :param data: 包含用户信息的数据。
        :param expires_delta: 令牌的有效期。
        :return: 创建的JWT令牌。
        """
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    @staticmethod
    async def get_current_user(token: str = Depends(oauth2_scheme)):
        """
        从JWT令牌中获取当前用户。

        :param token: JWT令牌。
        :return: 用户实例。
        """
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise credentials_exception
            token_data = TokenData(username=username)
        except JWTError:
            raise credentials_exception
        # MongoDB查询，确保数据库名称和集合名称正确
        user = await DataBase.client.your_db_name.users.find_one({"username": token_data.username})
        if not user:
            raise credentials_exception
        return UserInDB(**user)
