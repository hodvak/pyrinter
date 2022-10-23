from enum import Enum
from tkinter import Tk
from tkinter.font import Font as TkFont
from collections import namedtuple
from typing import Tuple

Font = namedtuple("Font", ("font_name", "height"))


class Align(Enum):
    RIGHT = 0
    LEFT = 1


class Document:
    """
    document that can be printed with Printer
    """

    def __init__(
            self, name: str = "My Document", page_size: Tuple[float] = (8.3, 11.7)
    ):
        """
        create document with name and
        :param name:
        :param page_size:
        """
        self.data = []
        self.pages = 0
        self.page_size = page_size
        self.name = name

    def add_text(
            self,
            text: str,
            font: Font = Font(font_name="Arial", height=12),
            page: int = None,
            rect: Tuple[float, float, float, float] = None,
            align: Align = Align.LEFT,
            color: int = 0x000000
    ):
        """
        add text to the document
        :param text: the text to print
        :param font: the font to use
        :param page: specific page to print on, None for the last page
        :param rect: the position to print on (inches)
        :param align: align to what side of the rect
        :param color: the color of the text (rgb)
        :return: None
        """
        if page is None:
            page = self.pages

        if page >= self.pages:
            self.pages = page + 1

        if rect is None:
            rect = (0.75, 0.75, self.page_size[0] - 0.75, self.page_size[1] - 0.75)

        new_lines = []
        for line in text.split("\n"):
            new_lines.append("")
            for word in line.split(" "):
                if new_lines[-1]:
                    if (
                            Document.__get_text_size(new_lines[-1] + " " + word, font)
                            < rect[2] - rect[0]
                    ):
                        new_lines[-1] += " " + word
                    else:
                        new_lines.append(word)
                else:
                    new_lines[-1] = word

        text = "\n".join(new_lines)

        self.data.append(
            {
                "type": "text",
                "page": page,
                "data": {"text": text, "font": font, "rect": rect, "align": align, "color": color},
            }
        )

    def add_frame_rect(
            self,
            rect: Tuple[float, float, float, float],
            width: float = 0.01,
            color: int = 0x000000,
            page: int = None,
    ):
        """
        add frame rectangle to the document
        :param rect: the rectangle to draw
        :param width: the width of the frame (inch)
        :param color: the color of the frame
        :param page: specific page to print on, None for the last page
        :return: None
        """
        if page is None:
            page = self.pages

        if page >= self.pages:
            self.pages = page + 1

        if rect is None:
            rect = (0.75, 0.75, self.page_size[0] - 0.75, self.page_size[1] - 0.75)

        self.data.append(
            {
                "type": "frame_rect",
                "page": page,
                "data": {"rect": rect, "color": color, "width": width},
            }
        )

    @staticmethod
    def __get_text_size(text: str, font: Font) -> float:
        root = Tk()  # Needed to estimate the width.
        font_var = TkFont(family=font.font_name, size=font.height, weight="normal")
        width = font_var.measure(text) / 105
        root.destroy()  # Destroy the created window
        return width

    def __getitem__(self, index: int):
        if index >= self.pages:
            raise IndexError()
        return (i for i in self.data if i["page"] == index)

    def __len__(self):
        return self.pages
