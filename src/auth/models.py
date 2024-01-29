# db 模型
class User(BaseModel):
    """
    用户模型，用于表示用户的数据结构。

    属性:
    - id: 用户ID。
    - username: 用户名。
    - email: 电子邮件地址。
    - hashed_password: 加密后的密码。
    """
    id: Optional[str]
    username: str
    email: EmailStr
    hashed_password: str
