#!/usr/bin/env python3
"""
Python module that contains the async_generator function
"""

import asyncio
import random


async def async_generator():
    """
    async_generator function
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
