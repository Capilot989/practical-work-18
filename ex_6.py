from typing import Callable, Any


def print_result(func: Callable) -> Callable:
    """
    Decorator that prints the return value of a function before returning it.

    This decorator wraps a function, executes it, prints the result to stdout,
    and then returns the result unchanged.

    Args:
        func: The function to be decorated

    Returns:
        A wrapper function that prints the result before returning it
    """
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        result = func(*args, **kwargs)
        print(result)
        return result
    return wrapper


#Example
@print_result
def sumary(a: int, b:int) -> int:
    return a + b


sumary(2,3)
