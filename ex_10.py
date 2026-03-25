from typing import Callable, Any
from time import time, sleep


def limit_time(
        *, max_time: float,
        max_calls: int, period: int
) -> Callable:
    """
    Decorator factory that limits function execution time and call frequency.

    This decorator imposes two restrictions on the decorated function:
    1. Maximum execution time per call (raises Timeout error if exceeded)
    2. Maximum number of calls within a specified time period (raises
       Too many calls error if exceeded)
    Args:
        max_time: Maximum allowed execution time per call in seconds
        max_calls: Maximum number of calls allowed within the period
        period: Time window in seconds for counting calls

    Returns:
        A decorator that applies the time and call limits
    """
    def decorator(func: Callable) -> Callable:
        calls = []

        def wrapper(*args: Any, **kwargs: Any) -> Any:
            nonlocal calls

            current_time = time()
            calls = [t for t in calls if current_time - t < period]

            if len(calls) > max_calls:
                raise Exception("Too many calls error")

            calls.append(current_time)
            start = time()
            result = func(*args, **kwargs)
            end = time()
            if end - start > max_time:
                raise Exception("Timeout error")

            return result
        return wrapper
    return decorator


# Example1
@limit_time(max_time=2, max_calls=5, period=10)
def slow_function():
    sleep(2)
    return "Done"
print(slow_function())


# Example2
@limit_time(max_time=2, max_calls=4, period=10)
def fast_function():
    return "OK"

for _ in range(6):
    print(fast_function())


