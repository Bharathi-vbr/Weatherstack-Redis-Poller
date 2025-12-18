import logging
import requests
from typing import Dict, Any, List

from config import WEATHERSTACK_API_KEY, LOCATIONS
from redis_client import get_weather, set_weather, update_weather

BASE_URL = "http://api.weatherstack.com/current"

def fetch_weather_from_api(location: str) -> Dict[str, Any]:
    params = {
        "access_key": WEATHERSTACK_API_KEY,
        "query": location,
    }
    logging.info("Calling Weatherstack for %s", location)
    resp = requests.get(BASE_URL, params=params, timeout=5)
    data = resp.json()

    if isinstance(data, dict) and data.get("error"):
        raise RuntimeError(
            f"{location}: {data['error'].get('info', 'Weatherstack error')}"
        )

    return data

def poll_weather() -> List[Dict[str, Any]]:
    """
    API polling:
    - For each location, call Weatherstack.
    - For each result, create or update a Redis entry.
    """
    results: List[Dict[str, Any]] = []

    for loc in LOCATIONS:
        api_data = fetch_weather_from_api(loc)

        existing = get_weather(loc)
        if existing is None:
            set_weather(loc, api_data)
        else:
            update_weather(loc, api_data)

        results.append(api_data)

    return results
