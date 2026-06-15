from pydantic_settings import BaseSettings
import os
import boto3
import logging

logger = logging.getLogger("ssp-cart-service")

def get_ssm_parameter(name, region):
    try:
        ssm_client = boto3.client('ssm', region_name=region)
        parameter = ssm_client.get_parameter(Name=name, WithDecryption=True)
        return parameter['Parameter']['Value']
    except Exception as e:
        logger.critical(f"Error fetching parameter {name}: {e}")
        raise

class Settings(BaseSettings):
    AWS_REGION: str = os.environ.get("AWS_REGION", "us-east-1")
    REDIS_HOST_PARAM_NAME: str = os.environ.get("REDIS_HOST_PARAM_NAME", "/ssp/cart/redis_host")
    REDIS_HOST: str = ""
    REDIS_PORT: int = 6379

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            self.REDIS_HOST = get_ssm_parameter(self.REDIS_HOST_PARAM_NAME, self.AWS_REGION)
        except Exception:
             self.REDIS_HOST = "localhost"

settings = Settings()
