"""
Printers utils.
"""

from typing import List


def get_all_printers() -> List[str]:
    """
    :return: list of the printers names
    """
    raise NotImplementedError


def get_default_printer() -> str:
    """
    :return: the default printer's name
    """
    raise NotImplementedError
