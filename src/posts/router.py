from fastapi import APIRouter, HTTPException, status
from .models import Post
from .service import PostService

router = APIRouter()


@router.post("/posts", response_model=Post)
async def create_post(post: Post):
    """
    创建帖子的API接口。

    :param post: 需要创建的帖子数据。
    :return: 创建的帖子对象。
    """
    return await PostService.create_post(post)


@router.get("/posts/{post_id}", response_model=Post)
async def get_post(post_id: str):
    """
    获取单个帖子的API接口。

    :param post_id: 帖子ID。
    :return: 请求的帖子对象。
    """
    return await PostService.get_post(post_id)

# 其他API路由...
