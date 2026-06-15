import pytest
from unittest.mock import AsyncMock, patch
from app.services.cart_service import CartService
from app.models.cart import Cart

@pytest.fixture
def mock_repository():
    return AsyncMock()

@pytest.fixture
def cart_service(mock_repository):
    service = CartService()
    service.repository = mock_repository
    return service

@pytest.mark.asyncio
async def test_get_cart_success(cart_service, mock_repository):
    # Setup
    mock_repository.get_cart.return_value = {"prod_1": 2, "prod_2": 1}

    # Execute
    result = await cart_service.get_cart("user_123")

    # Assert
    assert isinstance(result, Cart)
    assert result.user_id == "user_123"
    assert result.items == {"prod_1": 2, "prod_2": 1}
    mock_repository.get_cart.assert_called_once_with("user_123")

@pytest.mark.asyncio
async def test_add_to_cart(cart_service, mock_repository):
    # Setup: We mock the get_cart method to return the state AFTER adding
    mock_repository.add_item_to_cart.return_value = None
    mock_repository.get_cart.return_value = {"prod_1": 1}

    # Execute
    result = await cart_service.add_to_cart("user_123", "prod_1", 1)

    # Assert
    assert result.items == {"prod_1": 1}
    mock_repository.add_item_to_cart.assert_called_once_with("user_123", "prod_1", 1)
    mock_repository.get_cart.assert_called_once_with("user_123")

@pytest.mark.asyncio
async def test_clear_cart(cart_service, mock_repository):
    # Setup
    mock_repository.clear_cart.return_value = None

    # Execute
    result = await cart_service.clear_cart("user_123")

    # Assert
    assert result.user_id == "user_123"
    assert result.items == {}
    mock_repository.clear_cart.assert_called_once_with("user_123")
