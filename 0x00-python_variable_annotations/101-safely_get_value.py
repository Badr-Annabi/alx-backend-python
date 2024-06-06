#!/usr/bin/env python3
""" Writing a type-annotated function """
from typing import Mapping, Union, Any, TypeVar


T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None] = None) -> Union[Any, T]:
    """ This func takes a dict and a key.... """
    if key in dct:
        return dct[key]
    else:
        return default
