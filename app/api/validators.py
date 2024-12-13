from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.category import category_crud
from app.models import Category

async def check_category_exists(
        meeting_room_id: int,
        session: AsyncSession,
) -> Category:
    category = await category_crud.get(meeting_room_id, session)
    if category is None:
        raise HTTPException(
            status_code=404,
            detail='Категории с таким ID не существует'
        )
    return category