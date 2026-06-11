# app/services/cache.py

import time

CACHE = {}


def get_cache(key):

    item = CACHE.get(key)

    if not item:
        return None

    if time.time() > item["expires"]:
        return None

    return item["data"]


def set_cache(key, data, ttl):

    CACHE[key] = {
        "data": data,
        "expires": time.time() + ttl,
    }