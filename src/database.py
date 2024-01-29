from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
from .config import settings  # 确保配置文件的路径正确


class DataBase:
    """
    数据库连接类，负责管理MongoDB数据库的连接和断开。
    """
    client: MongoClient = None

    @staticmethod
    async def connect():
        """
        建立与MongoDB的连接。
        """
        DataBase.client = AsyncIOMotorClient(settings.MONGODB_URL)
        print("数据库连接成功")

    @staticmethod
    async def disconnect():
        """
        断开与MongoDB的连接。
        """
        DataBase.client.close()
        print("数据库断开连接")
