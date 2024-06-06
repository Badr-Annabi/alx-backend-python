#!/usr/bin/env python3
""" Writing a type-annotated function """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ This function to_kv takes a float multiplier as argument
    and returns a function that multiplies a float by multiplier. """
    def multiplier_function(value: float) -> float:
        return value * multiplier
    return multiplier_function
