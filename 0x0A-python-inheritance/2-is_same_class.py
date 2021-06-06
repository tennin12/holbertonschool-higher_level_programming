#!/usr/bin/python3
"""
modul: 2-is_same_class
"""

def is_same_class(obj, a_class):
    """
    determines if 'obj' is exactly an instance of 'a_class'
    """
    return issubclass(a_class, type(obj))
