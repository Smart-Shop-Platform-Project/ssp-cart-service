# SSP Cart Service

This service provides a high-performance, volatile storage solution for user shopping carts. It is built with FastAPI and uses Redis for extremely fast read/write operations.

## Core Responsibilities & Features

1.  **Cart Management:**
    *   Provides API endpoints to add items to, retrieve, update, and clear a user's shopping cart.
    *   Each user's cart is stored as a Redis Hash, which is an ideal data structure for this use case.

2.  **High Performance:**
    *   By using Redis (an in-memory data store), all cart operations (like adding an item) are completed with very low latency, providing a smooth user experience.

3.  **Ephemeral Storage:**
    *   Carts are considered temporary. The Redis keys are configured with a Time-To-Live (TTL), ensuring that abandoned carts are automatically cleared, saving memory.

## Architecture
- **Framework:** **FastAPI**
- **Database:** **Redis** (provisioned via Amazon ElastiCache).
- **Deployment:** **AWS ECS Fargate**
- **Dependencies:**
    - `redis-py`: The standard Python client for Redis.
    - `boto3`: To fetch the Redis endpoint from AWS SSM Parameter Store at runtime.

## Local Development

1.  Create a virtual environment: `python3 -m venv venv`
2.  Activate it: `source venv/bin/activate`
3.  Install dependencies: `pip install -r requirements.txt` and `pip install -r requirements-dev.txt`
4.  **Set Up Local Database:** This service requires a running Redis instance. You can start one easily with Docker:
    ```bash
    docker run --name ssp-redis-cart -p 6379:6379 -d redis
    ```
5.  Run the application:
    ```bash
    uvicorn app.main:app --reload --port 8004 
    ```
    *(Note: The port is an example; you can run it on any available port).*
