import os

# Required API key
WEATHERSTACK_API_KEY = os.environ["WEATHERSTACK_API_KEY"]

# Required locations list
raw_locations = os.environ.get("WEATHER_LOCATIONS")
if not raw_locations:
    raise RuntimeError(
        "WEATHER_LOCATIONS must be set, e.g. 'New York, USA;Dallas, USA'"
    )

LOCATIONS = [loc.strip() for loc in raw_locations.split(";") if loc.strip()]

# Redis connection + cache TTL
REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
REDIS_PORT = int(os.environ.get("REDIS_PORT", "6379"))
REDIS_DB   = int(os.environ.get("REDIS_DB", "0"))
CACHE_TTL  = int(os.environ.get("WEATHER_CACHE_TTL", "600"))  # 10 minutes

# Polling interval in seconds (override via env if needed)
POLL_INTERVAL_SECONDS = int(os.environ.get("POLL_INTERVAL_SECONDS", "60"))

# Convenience values
REDIS_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"
DEFAULT_CITY = LOCATIONS[0]
