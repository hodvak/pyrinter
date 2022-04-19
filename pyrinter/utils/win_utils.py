from typing import List

import win32print


def get_all_printers() -> List[str]:
    """
    :return: list of the printers names
    """
    return [i[2] for i in win32print.EnumPrinters(2)]


def get_default_printer() -> str:
    """
    :return: the default printer's name
    """
    return win32print.GetDefaultPrinter()
