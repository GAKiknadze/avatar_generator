
def validate_int_param(params: dict, key: str, min_value: int = None, max_value: int = None, default: int = None) -> int:
    """Validate and retrieve an integer parameter from a dictionary.
    
    Args:
        params (dict): The dictionary containing parameters.
        key (str): The key of the parameter to validate.
        min_value (int, optional): Minimum acceptable value. Defaults to None.
        max_value (int, optional): Maximum acceptable value. Defaults to None.
        default (int, optional): Default value if key is not present. Defaults to None.
    
    Returns:
        int: The validated integer parameter.
    Raises:
        TypeError: If the parameter is not an integer.
        ValueError: If the parameter is out of the specified range.
    """
    if key in params:
        value = params[key]
        if not isinstance(value, int):
            raise TypeError(f"{key} must be an integer")
        if min_value is not None and value < min_value:
            raise ValueError(f"{key} must be at least {min_value}")
        if max_value is not None and value > max_value:
            raise ValueError(f"{key} must be at most {max_value}")
        return value
    else:
        return default


def validate_bool_param(params: dict, key: str, default: bool = None) -> bool:
    """Validate and retrieve a boolean parameter from a dictionary.
    
    Args:
        params (dict): The dictionary containing parameters.
        key (str): The key of the parameter to validate.
        default (bool, optional): Default value if key is not present. Defaults to None.
    
    Returns:
        bool: The validated boolean parameter.
    Raises:
        TypeError: If the parameter is not a boolean.
    """
    if key in params:
        value = params[key]
        if not isinstance(value, bool):
            raise TypeError(f"{key} must be a boolean")
        return value
    else:
        return default
