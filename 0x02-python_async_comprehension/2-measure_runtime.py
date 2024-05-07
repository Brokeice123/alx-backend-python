#!/usr/bin/env python3
"""
Python module that contains the measure_runtime function
"""

import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension
import time


async def measure_runtime():
    """
    Measures the total execution time for async_comprehension executed 4 times
    in parallel using asyncio.gather.
    """
    start = time.time()
    results = await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end = time.time()

    total_time = end - start
    return total_time
