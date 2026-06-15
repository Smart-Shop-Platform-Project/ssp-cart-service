import redis
from .config import settings
import logging

logger = logging.getLogger("ssp-cart-service")

redis_client = None

def get_redis_client():
    global redis_client
    if not redis_client:
        try:
            logger.info(f"Connecting to Redis at {settings.REDIS_HOST}:{settings.REDIS_PORT}")
            redis_client = redis.Redis(
                host=settings.REDIS_HOST, 
                port=settings.REDIS_PORT, 
                decode_responses=True
            )
            # Test connection
            redis_client.ping()
        except Exception as e:
            logger.critical(f"Failed to connect to Redis: {e}")
            raise
    return redis_client
