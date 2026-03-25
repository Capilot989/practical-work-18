from typing import Callable, Any, Union
import json
import yaml
import dicttoxml


def to_format(format: str = None) -> Callable:
    """
    Decorator factory that formats a function's return value into a specified format.

    This decorator factory creates a decorator that converts the return value of
    a function into the specified format (JSON, YAML, or XML). If no format is
    specified, JSON is used as the default.

    Args:
        format: The output format - "json", "yaml", or "xml" (default: "json")

    Returns:
        A decorator that formats the function's return value
    """
    format = format or "json"

    def decorator(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            result = func(*args, **kwargs)
            match format.lower():
                case "json":
                    return json.dumps(result)
                case "yaml":
                    return yaml.dump(result)
                case "xml":
                    return dicttoxml.dicttoxml(
                        result, attr_type=False
                    )
            return f"Unsopported format: {format}"
        return wrapper
    return decorator


#Example
@to_format("yaml")
def get_info(name: str, age: int) -> dict[str: Union[str, int]]:
    return {"name": name, "age": age}

print(get_info("Ilya", 19))
