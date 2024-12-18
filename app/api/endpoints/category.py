from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.category import category_crud
from app.schemas.category import Category
from app.schemas.product import Product
from app.api.validators import check_category_exists

router = APIRouter()


@router.get(
    "/",
    response_model=List[Category],
    response_model_exclude_none=True,
)
async def get_all_categories(
    session: AsyncSession = Depends(get_async_session),
):
    """
    Получить список всех категорий.
    """
    return await category_crud.get_multi(session)


@router.get(
    "/{category_id}",
    response_model=Category,
    response_model_exclude_none=True,
)
async def get_category(
    category_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    """
    Получить категорию по ID.
    """
    category = await check_category_exists(category_id, session)
    return category


@router.post(
    "/",
    response_model=Category,
    response_model_exclude_none=True,
)
async def create_category(
    category: Category,
    session: AsyncSession = Depends(get_async_session),
):
    """
    Создать новую категорию.
    """
    new_category = await category_crud.create(category, session)
    return new_category


@router.get(
    "/{name}/products",
    response_model=List[Product],
    response_model_exclude_none=True,
)
async def get_products_by_category_name(
    name: str,
    session: AsyncSession = Depends(get_async_session),
):
    """
    Получить список всех продуктов из указанной категории.
    """
    return await category_crud.get_products_by_category_name(
        name, session
    )
