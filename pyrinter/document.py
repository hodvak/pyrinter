from enum import Enum
from tkinter import Tk
from tkinter.font import Font as TkFont
from collections import namedtuple
from typing import Tuple, Generator, Optional, Union
from PIL import Image


class Font(namedtuple("Font", ("font_name", "height", "weight"))):
    """
    class to represent font properties (font name, height and weight)

    weight can be either "normal" or "bold"
    """


class Align(Enum):
    """
    Alignment for text
    """

    RIGHT = 0
    LEFT = 1


class PaperSize(Enum):
    """
    Common paper sizes
    """

    LETTER = (8.5, 11)
    A4 = (8.3, 11.7)


class Document:
    """
    document that can be printed with Printer
    """

    def __init__(
        self,
        name: str = "My Document",
        page_size: Union[PaperSize, Tuple[float, float]] = PaperSize.A4,
    ):
        """
        create document with name and

        :param name: the name of the document (default "My Document")
        :param page_size: the size of the document (default A4)
        """
        self.data = []
        self.pages = 0

        if isinstance(page_size, PaperSize):
            page_size = page_size.value
        self.page_size = page_size
        self.name = name

    def add_text(
        self,
        text: str,
        font: Font = Font(font_name="Arial", height=12, weight="normal"),
        page: Optional[int] = None,
        rect: Optional[Tuple[float, float, float, float]] = None,
        align: Align = Align.LEFT,
        color: int = 0x000000,
    ):
        """
        add text to the document

        :param text: the text to print
        :param font: the font to use
        :param page: specific page to print on, None for new page. Negative indexing is supported. Default None
        :param rect: the position to print on (inches)
        :param align: align to what side of the rect
        :param color: the color of the text (rgb)
        :return: None
        """
        if page is None:
            page = self.pages

        if page < 0:
            page += self.pages

        if page >= self.pages:
            self.pages = page + 1

        if page < 0:
            raise IndexError(
                f"Page index out of range, must be above or equal to {-self.pages}  (the number of pages)"
            )

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
                "data": {
                    "text": text,
                    "font": font,
                    "rect": rect,
                    "align": align,
                    "color": color,
                },
            }
        )

    def add_frame_rect(
        self,
        rect: Optional[Tuple[float, float, float, float]] = None,
        width: float = 0.01,
        color: int = 0x000000,
        page: Optional[int] = None,
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

        if page < 0:
            page += self.pages

        if page >= self.pages:
            self.pages = page + 1

        if page < 0:
            raise IndexError(
                f"Page index out of range, must be above or equal to {-self.pages} (the number of pages)"
            )

        if rect is None:
            rect = (0.75, 0.75, self.page_size[0] - 0.75, self.page_size[1] - 0.75)

        self.data.append(
            {
                "type": "frame_rect",
                "page": page,
                "data": {"rect": rect, "color": color, "width": width},
            }
        )

    def add_image(
        self,
        image: Union[str, Image.Image],
        rect: Optional[Tuple[int, int, int, int]] = None,
        page: Optional[int] = None,
    ):
        """
        | add image to the document.
        | on windows: transparent will become white background

        :param image: the image to add, an PIL Image instance or a path to an image
        :param rect: the rectangle to draw on (inches), None to draw on the whole page
        :param page: the page to draw on, None for new page. Negative indexing is supported. Default None
        """
        if page is None:
            page = self.pages

        if page < 0:
            page += self.pages

        if page >= self.pages:
            self.pages = page + 1

        if page < 0:
            raise IndexError(
                f"Page index out of range, must be above or equal to {-self.pages} (the number of pages)"
            )

        if isinstance(image, str):
            image = Image.open(image)

        image_width, image_height = image.size
        if rect is None:
            scale = min(
                (self.page_size[0] - 0.75 * 2) / image_width,
                (self.page_size[1] - 0.75 * 2) / image_height,
            )
            new_width = int(image_width * scale)
            new_height = int(image_height * scale)
            center = (self.page_size[0] / 2, self.page_size[1] / 2)

            rect = (
                center[0] - new_width / 2,
                center[1] - new_height / 2,
                center[0] + new_width / 2,
                center[1] + new_height / 2,
            )

        self.data.append(
            {"type": "image", "page": page, "data": {"image": image, "rect": rect}}
        )

    @staticmethod
    def __get_text_size(text: str, font: Font) -> float:
        """
        get the text size of a text (width) by the given font

        :param text: the text to print
        :param font: the font to use
        :return: the width of the text
        """
        root = Tk()  # Needed to estimate the width.
        font_var = TkFont(family=font.font_name, size=font.height, weight=font.weight)
        width = font_var.measure(text) / 105
        root.destroy()  # Destroy the created window
        return width

    def __getitem__(self, index: int) -> Generator:
        """
        get the document data by pages (a generator)

        :param index: the index of the page. Negative indexing is supported
        :return: the document data by page
        """
        if index < 0:
            index += self.page_size
        if index >= self.pages or index < 0:
            raise IndexError(
                f"page index is out of range, supported indexes are between {-self.pages} and {self.pages - 1}"
            )
        return (i for i in self.data if i["page"] == index)

    def __len__(self):
        return self.pages
