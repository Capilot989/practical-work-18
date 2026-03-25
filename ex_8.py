from typing import Callable, Any
from datetime import datetime


def log_exceptions(func: Callable) ->Callable:
    """
        Decorator that logs exceptions to a file when they occur.

        This decorator wraps a function and catches any exceptions that occur
        during its execution. When an exception is caught, it logs the timestamp,
        function name, and exception type to a log file, and prints a confirmation
        message to the console.

        Args:
            func: The function to be decorated

        Returns:
            A wrapper function that handles and logs exceptions
        """
    def wrapper(*args: Any, **kwargs: Any) -> None:
        try:
            return func(*args, **kwargs)
        except Exception as e:
            time = datetime.now()
            log_info = f"{time} Exception in {func.__name__}, type {e}"
            with open("log_file", "a", encoding="utf-8") as f:
                f.write(log_info)
            print("Log about exceptions was saved in log_info")
    return wrapper


#Example
@log_exceptions
def divide(a, b):
    return a / b
divide(10,0)
