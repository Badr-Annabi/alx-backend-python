#!/usr/bin/env python3
""" Writing a type-annotated function """
from typing import List


def sum_list(input_list: List[float] ) -> float:
    """ This function takes a list input_list of floats as 
    argument and returns their sum as a float. """
    return sum(input_list)
