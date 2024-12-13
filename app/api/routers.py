from fastapi import APIRouter


from app.api.endpoints import category_router, product_router

main_router = APIRouter()

main_router.include_router(
    category_router,
    prefix='/categories',
    tags=['Categories']
)

main_router.include_router(
    product_router,
    prefix='/products',
    tags=['Products']
)