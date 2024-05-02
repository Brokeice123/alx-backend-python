#!/usr/bin/env python3
"""This module defines the safe_first_element function."""

from typing import Sequence, Any, Union, Type


def safe_first_element(lst: Sequence[Any]) -> Union[Any, Type[None]]:
    """Return the first element of a list."""
    if lst:
        return lst[0]
    else:
        return None