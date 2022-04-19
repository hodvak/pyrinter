from pyrinter import Document
from .abs_printer import AbsPrinter
import win32ui
import win32con


class Printer(AbsPrinter):
    """
    windows implementation of Printer
    """

    def print_doc(self, document: Document):
        doc = win32ui.CreateDC()
        doc.CreatePrinterDC(self.name)
        doc.StartDoc(document.name)
        doc.SetMapMode(win32con.MM_HIENGLISH)
        for page in document:
            doc.StartPage()
            for to_print in page:
                if to_print["type"] == "text":
                    Printer.__add_text(doc, to_print["data"])
            doc.EndPage()
        doc.EndDoc()

    @staticmethod
    def __add_text(doc, data):
        doc.SelectObject(
            win32ui.CreateFont(
                {
                    "name": data["font"].font_name,
                    "height": int(
                        Printer.__inch_to_printer_size(data["font"].height / 72)
                    ),
                }
            )
        )
        doc.DrawText(
            data["text"], Printer.__get_printer_rect(data["rect"]), win32con.DT_LEFT
        )

    @staticmethod
    def __get_printer_rect(rect):
        return (
            int(Printer.__inch_to_printer_size(rect[0])),
            -int(Printer.__inch_to_printer_size(rect[1])),
            int(Printer.__inch_to_printer_size(rect[2])),
            -int(Printer.__inch_to_printer_size(rect[3])),
        )

    @staticmethod
    def __inch_to_printer_size(inches: float):
        return inches * 1000
