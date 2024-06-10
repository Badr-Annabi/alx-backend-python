#!/usr/bin/env python3
"""The basics of async"""

wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio


async def wait_n(n: int, max_delay: int) -> list:
    tasks = [wait_random(max_delay) for _ in range(n)]
    delay_list = await asyncio.gather(*tasks)
    return sorted(delay_list)
