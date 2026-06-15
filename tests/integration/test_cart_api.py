import pytest
from app.models.cart import Cart

# Uses the client and mock_redis fixtures
def test_add_to_cart_api(client, mock_redis):
    # Execute
    response = client.post(
        "/api/v1/cart/user_api_1",
        json={"item_id": "prod_api_1", "quantity": 3}
    )

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data["user_id"] == "user_api_1"
    assert data["items"] == {"prod_api_1": 3}
    
    # Verify via second API call
    response2 = client.get("/api/v1/cart/user_api_1")
    assert response2.json()["items"] == {"prod_api_1": 3}

def test_remove_from_cart_api(client, mock_redis):
    # Setup
    client.post("/api/v1/cart/user_api_2", json={"item_id": "p1", "quantity": 1})
    client.post("/api/v1/cart/user_api_2", json={"item_id": "p2", "quantity": 2})
    
    # Execute
    response = client.delete("/api/v1/cart/user_api_2/item/p1")
    
    # Assert
    assert response.status_code == 200
    assert response.json()["items"] == {"p2": 2}

def test_clear_cart_api(client, mock_redis):
    # Setup
    client.post("/api/v1/cart/user_api_3", json={"item_id": "p1", "quantity": 1})
    
    # Execute
    response = client.delete("/api/v1/cart/user_api_3")
    
    # Assert
    assert response.status_code == 200
    assert response.json()["items"] == {}
    
def test_health_check(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "SSP Cart Service is running"}
