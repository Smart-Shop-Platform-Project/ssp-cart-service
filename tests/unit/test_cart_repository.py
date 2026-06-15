import pytest
from app.repositories.cart_repository import CartRepository

# Uses the mock_redis fixture from conftest.py
@pytest.fixture
def repo(mock_redis):
    # The repository will automatically pick up the patched get_redis_client
    return CartRepository()

@pytest.mark.asyncio
async def test_add_and_get_cart(repo: CartRepository, mock_redis):
    # Execute Add
    await repo.add_item_to_cart("user_1", "prod_1", 2)
    await repo.add_item_to_cart("user_1", "prod_2", 1)
    
    # Execute Get
    cart = await repo.get_cart("user_1")
    
    # Assert
    assert cart == {"prod_1": 2, "prod_2": 1}
    # Verify underlying mock redis was hit
    assert mock_redis.hgetall("cart:user_1") == {"prod_1": "2", "prod_2": "1"}

@pytest.mark.asyncio
async def test_remove_item(repo: CartRepository):
    # Setup
    await repo.add_item_to_cart("user_2", "prod_1", 5)
    await repo.add_item_to_cart("user_2", "prod_2", 3)
    
    # Execute
    await repo.remove_item_from_cart("user_2", "prod_1")
    
    # Assert
    cart = await repo.get_cart("user_2")
    assert cart == {"prod_2": 3}

@pytest.mark.asyncio
async def test_clear_cart(repo: CartRepository):
    # Setup
    await repo.add_item_to_cart("user_3", "prod_1", 1)
    
    # Execute
    await repo.clear_cart("user_3")
    
    # Assert
    cart = await repo.get_cart("user_3")
    assert cart == {}
