#!/usr/bin/env python3
""" Writing a type-annotated function """
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ the function is a iterableå"""
    return [(i, len(i)) for i in lst]
