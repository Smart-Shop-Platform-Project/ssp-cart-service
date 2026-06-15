import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from app.main import app
import fakeredis

@pytest.fixture(scope="module")
def client():
    return TestClient(app)

@pytest.fixture(scope="function")
def mock_redis():
    # Use fakeredis to simulate a real Redis server in memory for tests
    server = fakeredis.FakeServer()
    client = fakeredis.FakeStrictRedis(server=server, decode_responses=True)
    
    with patch("app.core.redis_client.redis_client", client):
        with patch("app.core.redis_client.get_redis_client", return_value=client):
            # We also need to patch the global redis_client used directly in routes for legacy code
            with patch("app.api.cart_routes.cart_service.repository.redis", client):
                yield client
    client.flushall()
