#!/usr/bin/env python3
"""This module defines the make_multiplier function."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by multiplier."""
    def multiplier_func(num: float) -> float:
        return num * multiplier
    return multiplier_func
