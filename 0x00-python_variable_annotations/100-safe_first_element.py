#!/usr/bin/env python3
""" Writing a type-annotated function """
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    This function takes a sequence of any type and returns either
    the first element of the sequence or None.
    """
    if lst:
        return lst[0]
    else:
        return None
