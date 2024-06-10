#!/usr/bin/env python3
"""The basics of async"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> float:
    """ This function takes an integer max_delay and
    returns a asyncio.Task. """
    return asyncio.create_task(wait_random(max_delay))