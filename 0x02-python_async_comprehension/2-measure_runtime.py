#!/usr/bin/env python3
"""
Python module that contains the measure_runtime function
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total execution time for async_comprehension executed 4 times
    in parallel using asyncio.gather.
    """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.time()

    total_time = end - start
    return total_time
