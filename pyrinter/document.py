from collections import namedtuple
from typing import Tuple

Font = namedtuple("Font", ("font_name", "height"))


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
    ):
        """
        add text to the document
        :param text: the text to print
        :param font: the font to use
        :param page: specific page to print on, None for the last page
        :param rect: the position to print on
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
                "type": "text",
                "page": page,
                "data": {"text": text, "font": font, "rect": rect},
            }
        )

    def __getitem__(self, index: int):
        if index >= self.pages:
            raise IndexError()
        return (i for i in self.data if i["page"] == index)

    def __len__(self):
        return self.pages
