# Pyrinter #
[![Github licence](https://img.shields.io/github/license/hodvak/pyrinter)](https://github.com/hodvak/pyrinter/blob/master/LICENSE)
[![PyPI version](https://img.shields.io/pypi/v/pyrinter)](https://pypi.org/project/pyrinter/)

## What is it ##
Pyrinter (python printer adapter) is a free open source python package for physical printers use.

## How to Install ##
with pip:
```sh
pip install pyrinter
```

## How to Use ##
the following code is a `hello world` for printing text using the printer `PDFCreator` 
(the printer name may be empty for default printer):
```python3
from pyrinter import Printer
from pyrinter import Document

doc = Document()
doc.add_text("Hello World")

printer = Printer("PDFCreator")
printer.print_doc(doc)
```