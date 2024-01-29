from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Post(BaseModel):
    """
    帖子模型，用于表示帖子的数据结构。

    属性:
    - id: 帖子ID。
    - title: 帖子标题。
    - content: 帖子内容。
    - author_id: 作者ID。
    - created_at: 创建时间。
    """
    id: Optional[str]
    title: str
    content: str
    author_id: str
    created_at: datetime = datetime.now()
