#!/usr/bin/env python3
"""The basics of async"""

import asyncio
from typing import List
wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """This function returns wait_random n times"""
    tasks = [wait_random(max_delay) for _ in range(n)]
    delay_list = await asyncio.gather(*tasks)
    return sorted(delay_list)
