# Third Party Library
import pytest

# First Party Library
from src.main import add


def test_add() -> None:
    assert add(1, 3) == 4
    assert add(-1, 3) == 2
    assert add(0, 0) == 0
    assert add(1, 0) == 1


def test_add_with_str() -> None:
    with pytest.raises(TypeError):
        add("1", "3")

    with pytest.raises(TypeError):
        add("1", 1)

    with pytest.raises(TypeError):
        add(1, "3")
