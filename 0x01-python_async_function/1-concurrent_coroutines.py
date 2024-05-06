#!/usr/bin/env python3
"""
This module is an example of how to use asyncio to run concurrent coroutines.
"""

import asyncio
from typing import List
from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run wait_random n times with the given max_delay and return the list of delays
    in ascending order without using sort() because of concurrency.
    """
    delays = []
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delays.append(await task)
    return delays