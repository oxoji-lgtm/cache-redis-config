import redis
from typing import Dict, Any
from logging import getLogger

logger = getLogger(__name__)

def get_redis_connection(
    host: str = "localhost",
    port: int = 6379,
    db: int = 0,
    password: str = None,
    ssl: bool = False,
    ssl_cert_reqs: str = 'required',
) -> redis.Redis:
    try:
        if ssl:
            return redis.Redis(
                host=host,
                port=port,
                db=db,
                password=password,
                ssl=True,
                ssl_cert_reqs=ssl_cert_reqs,
            )
        return redis.Redis(
            host=host,
            port=port,
            db=db,
            password=password,
        )
    except redis.ConnectionError as e:
        logger.error(f"Failed to connect to redis: {e}")
        raise

def get_config_value(config: Dict[str, Any], key: str, default: Any) -> Any:
    return config.get(key, default)