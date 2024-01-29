# 全局模型
# 在models.py中添加角色字段
class UserInDB(UserCreate):
    # ... 其他字段 ...
    role: str = "user"  # 默认为'user'，可以是'admin'等
