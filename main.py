import time
import logging

from config import LOCATIONS, POLL_INTERVAL_SECONDS, REDIS_URL
from weather_client import poll_weather

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    force=True,  # ensure our config wins
)

def poll_once() -> None:
    """
    One polling cycle for all configured locations.
    poll_weather():
      - calls Weatherstack for each location
      - upserts into Redis
      - returns list of responses
    """
    results = poll_weather()

    for data in results:
        location = data["location"]["name"]
        country = data["location"]["country"]
        current = data["current"]

        logging.info(
            "%s, %s | temp=%s°C desc=%s humidity=%s%%",
            location,
            country,
            current["temperature"],
            ", ".join(current["weather_descriptions"]),
            current["humidity"],
        )

def poll_forever() -> None:
    logging.info(
        "Starting poller for %d locations every %s seconds (Redis=%s)",
        len(LOCATIONS),
        POLL_INTERVAL_SECONDS,
        REDIS_URL,
    )
    while True:
        poll_once()
        logging.info("Sleeping %s seconds before next poll", POLL_INTERVAL_SECONDS)
        time.sleep(POLL_INTERVAL_SECONDS)

if __name__ == "__main__":
    poll_forever()
