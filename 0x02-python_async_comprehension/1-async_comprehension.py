#!/usr/bin/env python3
"""async generator func"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ returns 10 random value from async_generator"""
    return[i async for i in async_generator()]
