#!/usr/bin/env python3
"""This module defines the element_length function."""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples (n, len(n))."""
    return [(i, len(i)) for i in lst]