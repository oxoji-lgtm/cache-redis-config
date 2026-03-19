import os
import logging
from typing import List

# Set the logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_required_env_variables() -> List[str]:
    """Return a list of required environment variables."""
    return ['CACHE_REDIS_HOST', 'CACHE_REDIS_PORT', 'CACHE_REDIS_DB', 'CACHE_REDIS_PASSWORD']

def validate_env_variables() -> bool:
    """Validate the environment variables and return True if they are set."""
    required_env_variables = get_required_env_variables()
    for env_variable in required_env_variables:
        if env_variable not in os.environ:
            logging.error(f"Missing required environment variable: {env_variable}")
            return False
    return True

def configure_redis() -> None:
    """Configure the Redis connection based on the environment variables."""
    if not validate_env_variables():
        logging.error("Environment variables are not set correctly. Exiting.")
        exit(1)
    
    from redis import Redis
    host = os.environ['CACHE_REDIS_HOST']
    port = int(os.environ['CACHE_REDIS_PORT'])
    db = int(os.environ['CACHE_REDIS_DB'])
    password = os.environ['CACHE_REDIS_PASSWORD']
    
    logging.info(f"Connecting to Redis at {host}:{port} on database {db}")
    redis = Redis(host=host, port=port, db=db, password=password)
    
    # Perform any necessary Redis configuration here
    redis.ping()

def main() -> None:
    """Main entry point of the script."""
    configure_redis()

if __name__ == "__main__":
    main()