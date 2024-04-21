from typing import Optional

from pyrinter import Document
from pyrinter import printer_utils
import abc


class AbsPrinter(abc.ABC):
    """
    printer class to print with the printer, each OS will have its own implementation of this class
    """

    def __init__(self, name: Optional[str] = None):
        """
        makes a Printer object to print with
        :param name: the name of the printer, None for default printer
        """
        if not name:  # name is None or empty
            name = printer_utils.get_default_printer()

        if (
            name not in printer_utils.get_all_printers()
        ):  # check that the printer's name is one of the printers
            raise ValueError(f'not a valid printer name (""{name}"")')

        self.name = name

    @abc.abstractmethod
    def print_doc(self, document: Document):
        """
        use to print text with the printer
        :param document: the document to print
        :return: None
        """
