import requests

from app.services.cache import (
    get_cache,
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
        timeout=10
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
            900
        )

        print("Games API success")

        return data

    except Exception as e:

        print(f"Games API failed: {e}")

        if cached:
            print("Returning cached games")
            return cached

        raise


def get_stadiums():

    cached = get_cache("stadiums")

    if cached:
        return cached

    response = session.get(
        f"{BASE_URL}/get/stadiums",
        headers=HEADERS,
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    set_cache(
        "stadiums",
        data,
        86400
    )

    return data