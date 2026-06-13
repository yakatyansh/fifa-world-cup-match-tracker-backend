import requests

from app.services.cache import (
    get_cache,
    get_stale_cache,
    set_cache,
)

BASE_URL = "https://worldcup26.ir"

session = requests.Session()

HEADERS = {
    "User-Agent": "WC26Tracker/1.0"
}


def get_teams():

    cached = get_cache("teams")
    

    if cached:
        return cached

    response = session.get(
        f"{BASE_URL}/get/teams",
        headers=HEADERS,
        timeout=5
    )

    response.raise_for_status()

    data = response.json()

    set_cache(
        "teams",
        data,
        86400
    )

    return data


def get_games():

    cached = get_cache("games")
    stale = get_stale_cache("games")

    print(f"Games cache exists: {cached is not None}")

    if cached:
        print("Returning cached games")
        return cached

    try:
        response = session.get(
            f"{BASE_URL}/get/games",
            headers=HEADERS,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        set_cache(
            "games",
            data,
            30
        )

        print("Games API success | Cached for 30 seconds")

        return data

    except Exception as e:

        print(f"Games API failed: {e}")

        if stale is not None:
            print("Returning stale games")
            return stale

        raise
def get_stadiums():

    cached = get_cache("stadiums")

    if cached:
        return cached

    response = session.get(
        f"{BASE_URL}/get/stadiums",
        headers=HEADERS,
        timeout=5
    )

    response.raise_for_status()

    data = response.json()

    set_cache(
        "stadiums",
        data,
        86400
    )

    return data