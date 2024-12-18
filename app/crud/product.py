from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import Product


class CRUDProduct(CRUDBase):
    async def get_by_name(self, session: AsyncSession, name: str):
        return (
            (
                await session.execute(
                    select(Product).where(Product.name == name)
                )
            )
            .scalars()
            .all()
        )


product_crud = CRUDProduct(Product)
