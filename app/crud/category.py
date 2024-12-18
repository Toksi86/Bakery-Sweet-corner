from sqlalchemy import select
from sqlalchemy.orm import aliased
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import Category, Product


class CRUDCategory(CRUDBase):
    async def get_products_by_category_name(
        self, name: str, session: AsyncSession
    ):
        category_alias = aliased(Category)
        query = (
            select(Product)
            .join(category_alias, Product.category_id == category_alias.id)
            .where(category_alias.name == name)
        )
        return (await session.execute(query)).scalars().all()


category_crud = CRUDCategory(Category)
