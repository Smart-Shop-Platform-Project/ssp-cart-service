from pydantic import BaseModel
from typing import Dict

class Cart(BaseModel):
    user_id: str
    items: Dict[str, int] # product_id: quantity
