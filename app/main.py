from typing import Any, Callable


def cache(func: Callable) -> Callable:
    """
    A decorator that caches the results of a function call.
    """
    cache_storage = {}

    def wrapper(*args, **kwargs) -> Any:
        """
        The wrapper function that handles caching logic.
        """
        key = (func, args, frozenset(kwargs.items()))

        if key in cache_storage:
            print("Getting from cache")
            return cache_storage[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_storage[key] = result
            return result

    return wrapper