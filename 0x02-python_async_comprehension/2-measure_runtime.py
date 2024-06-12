#!/usr/bin/env python3
"""Async Comprehension"""

from asyncio import gather
from time import time

async_generator = __import__('1-async_comprehension').async_comprehension


async def async_comprehension() -> List[float]:
    """This function runs time for parallel comprehension"""
    start_time = time()
    tasks = [async_comprehension() for i in range(4)]
    await gather(*tasks)
    end_time = time()
    return (end_time - start_time)
