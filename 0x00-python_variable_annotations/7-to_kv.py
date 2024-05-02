#!/usr/bin/env python3
"""This module defines the to_kv function."""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with k as first element and the square of v as second element."""
    return (k, v**2)
