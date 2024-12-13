from app.crud.base import CRUDBase
from app.models import Product


class CRUDCategory(CRUDBase):
    pass


product_crud = CRUDCategory(Product)
