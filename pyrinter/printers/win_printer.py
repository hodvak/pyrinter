from pyrinter import Document
from .abs_printer import AbsPrinter
import win32ui
import win32con

from ..document import Align


class Printer(AbsPrinter):
    """
    windows implementation of Printer
    """

    def print_doc(self, document: Document):
        doc = win32ui.CreateDC()
        doc.CreatePrinterDC(self.name)
        doc.StartDoc(document.name)
        doc.SetMapMode(win32con.MM_HIENGLISH)

        type_to_command = {
            "text": Printer.__add_text,
            "frame_rect": Printer.__add_frame_rect,
        }

        for page in document:
            doc.StartPage()
            for to_print in page:
                type_to_command[to_print["type"]](doc, to_print["data"])
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
        align = win32con.DT_LEFT if data["align"] == Align.LEFT else win32con.DT_RIGHT
        doc.DrawText(
            data["text"], Printer.__get_printer_rect(data["rect"]), align
        )

    @staticmethod
    def __add_frame_rect(doc, data):
        doc.SelectObject(
            win32ui.CreatePen(
                win32con.PS_SOLID,
                int(Printer.__inch_to_printer_size(data["width"])),
                data["color"],
            )
        )
        rect = data["rect"]
        rect = Printer.__get_printer_rect(rect)

        doc.MoveTo((rect[0], rect[1]))
        doc.LineTo((rect[0], rect[3]))
        doc.LineTo((rect[2], rect[3]))
        doc.LineTo((rect[2], rect[1]))
        doc.LineTo((rect[0], rect[1]))

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
