from ..repositories.cart_repository import CartRepository
from ..models.cart import Cart
import logging

logger = logging.getLogger("ssp-cart-service")

class CartService:
    def __init__(self):
        self.repository = CartRepository()

    async def get_cart(self, user_id: str):
        items = await self.repository.get_cart(user_id)
        return Cart(user_id=user_id, items=items)

    async def add_to_cart(self, user_id: str, item_id: str, quantity: int):
        await self.repository.add_item_to_cart(user_id, item_id, quantity)
        return await self.get_cart(user_id)

    async def remove_from_cart(self, user_id: str, item_id: str):
        await self.repository.remove_item_from_cart(user_id, item_id)
        return await self.get_cart(user_id)

    async def clear_cart(self, user_id: str):
        await self.repository.clear_cart(user_id)
        return Cart(user_id=user_id, items={})
