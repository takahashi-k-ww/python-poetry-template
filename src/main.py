# Standard Library
from typing import Union

Number = Union[int, float]


def add(x: Number, y: Number) -> Number:
    """数値の加算

    _extended_summary_

    Args:
        x (Number): _description_
        y (Number): _description_

    Raises:
        TypeError: _description_

    Returns:
        Number: _description_
    """
    if not isinstance(x, Number) or not isinstance(y, Number):
        raise TypeError
    return x + y
