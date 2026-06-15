from fastapi import FastAPI
import logging
import sys
from .api.cart_routes import router as cart_router

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='{"time":"%(asctime)s", "level":"%(levelname)s", "message":"%(message)s"}',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("ssp-cart-service")

app = FastAPI(title="SSP Cart Service")

app.include_router(cart_router, prefix="/api/v1")

@app.get("/", tags=["Health Check"])
async def root():
    return {"message": "SSP Cart Service is running"}
