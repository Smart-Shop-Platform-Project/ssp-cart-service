from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..services.cart_service import CartService
from ..models.cart import Cart

router = APIRouter()
cart_service = CartService()

class AddItemRequest(BaseModel):
    item_id: str
    quantity: int

@router.get("/cart/{user_id}", response_model=Cart, tags=["Cart"])
async def get_cart(user_id: str):
    try:
        return await cart_service.get_cart(user_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/cart/{user_id}", response_model=Cart, tags=["Cart"])
async def add_to_cart(user_id: str, request: AddItemRequest):
    try:
        return await cart_service.add_to_cart(user_id, request.item_id, request.quantity)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/cart/{user_id}/item/{item_id}", response_model=Cart, tags=["Cart"])
async def remove_from_cart(user_id: str, item_id: str):
    try:
        return await cart_service.remove_from_cart(user_id, item_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/cart/{user_id}", response_model=Cart, tags=["Cart"])
async def clear_cart(user_id: str):
    try:
        return await cart_service.clear_cart(user_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
