from ..core.redis_client import get_redis_client
import logging
import json

logger = logging.getLogger("ssp-cart-service")

class CartRepository:
    def __init__(self):
        self.redis = get_redis_client()

    async def get_cart(self, user_id: str):
        try:
            cart_data = self.redis.hgetall(f"cart:{user_id}")
            # Convert string quantities back to integers
            cart = {item_id: int(quantity) for item_id, quantity in cart_data.items()}
            return cart
        except Exception as e:
            logger.error(f"Repository Error retrieving cart for user {user_id}: {e}")
            raise

    async def add_item_to_cart(self, user_id: str, item_id: str, quantity: int):
        try:
            self.redis.hincrby(f"cart:{user_id}", item_id, quantity)
        except Exception as e:
            logger.error(f"Repository Error adding item {item_id} to cart for user {user_id}: {e}")
            raise

    async def remove_item_from_cart(self, user_id: str, item_id: str):
        try:
            self.redis.hdel(f"cart:{user_id}", item_id)
        except Exception as e:
            logger.error(f"Repository Error removing item {item_id} from cart for user {user_id}: {e}")
            raise

    async def clear_cart(self, user_id: str):
        try:
            self.redis.delete(f"cart:{user_id}")
        except Exception as e:
            logger.error(f"Repository Error clearing cart for user {user_id}: {e}")
            raise
