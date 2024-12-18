from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import check_category_exists
from app.core.db import get_async_session
from app.crud.product import product_crud
from app.schemas.product import Product

router = APIRouter()


@router.get(
    "/",
    response_model=List[Product],
    response_model_exclude_none=True,
)
async def get_all_products(
    session: AsyncSession = Depends(get_async_session),
):
    """
    Получить список всех продуктов.
    """
    return await product_crud.get_multi(session)


@router.post(
    "/",
    response_model=Product,
    response_model_exclude_none=True,
)
async def create_product(
    product: Product,
    session: AsyncSession = Depends(get_async_session),
):
    """
    Создать новый продукт.
    """
    await check_category_exists(product.category_id, session)
    return await product_crud.create(product, session)


@router.get(
    "/{name}",
    response_model=List[Product],
    response_model_exclude_none=True,
)
async def get_product_by_name(
    name: str,
    session: AsyncSession = Depends(get_async_session),
):
    """
    Получить продукт по имени.
    """
    return await product_crud.get_by_name(session, name)
