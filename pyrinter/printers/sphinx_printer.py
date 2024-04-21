from .abs_printer import AbsPrinter
from .. import Document


class Printer(AbsPrinter):
    """
    A class to represent a printer.
    """

    def print_doc(self, document: Document):
        """
        use to print a document using the printer.

        :param document: the document to print
        :return: None
        """

        raise NotImplementedError
