from functools import lru_cache
from collections.abc import Callable


def cache(func: Callable) -> Callable:
    cache = {}

    def wrapper(*args, **kwargs):
        if not cache.get(args):
            func_result = func(*args, **kwargs)
            cache[args] = func_result
            return func_result
        else:
            return cache[args]

    return wrapper


def cache_lru(func: Callable) -> Callable:
    return lru_cache(func)
