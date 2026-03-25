from typing import Callable, Any
import json


def to_json(func: Callable) -> Callable:
    """
    Decorator that converts a function's return value to a JSON string.

    This decorator wraps a function, executes it, and converts the result
    to a JSON-formatted string using json.dumps().

    Args:
        func: The function to be decorated

    Returns:
        A wrapper function that returns the JSON string representation
        of the original function's return value
    """
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        result = func(*args, **kwargs)
        return json.dumps(result)
    return wrapper


#Example1
@to_json
def get_info(name: str, age: int) -> dict[str: str]:
    """
    Return user information as a dictionary.

    Args:
        name: User's name
        age: User's age

    Returns:
        Dictionary containing user information
    """
    return {"Name": name, "Age": age}
print(get_info("Ilya", "19"))


#Example2
@to_json
def get_numbers_list(numb: int) -> list[int]:
    """
        Generate a list of numbers from 1 to numb.

        Args:
            numb: Upper bound for the number list

        Returns:
            List of integers from 1 to numb inclusive
        """
    return list(range(1, numb + 1))
print(get_numbers_list(9))
