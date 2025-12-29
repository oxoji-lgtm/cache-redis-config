import logging
from redis import Redis
from config import REDIS_URL
from cache_config import CacheConfig

logging.basicConfig(level=logging.INFO)

def get_redis_client():
    """Get a Redis client instance."""
    return Redis.from_url(REDIS_URL)

def get_cache_config():
    """Get the cache configuration."""
    return CacheConfig()

def main():
    """Main application entry point."""
    redis_client = get_redis_client()
    cache_config = get_cache_config()

    try:
        logging.info("Connecting to Redis...")
        redis_client.ping()
        logging.info("Cache config: %s", cache_config)

    except Exception as e:
        logging.error("Error occurred: %s", e)

if __name__ == "__main__":
    main()