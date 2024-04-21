# Pyrinter #
[![Github licence](https://img.shields.io/github/license/hodvak/pyrinter)](https://github.com/hodvak/pyrinter/blob/master/LICENSE)
[![PyPI version](https://img.shields.io/pypi/v/pyrinter)](https://pypi.org/project/pyrinter/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Documentation Status](https://readthedocs.org/projects/pyrinter/badge/?version=latest)](https://pyrinter.readthedocs.io/en/latest/)
## What is it ##
**Pyrinter** is a free open source python package for easy way to use physical printers.  

As for the moment the package only works on windows, 
but in the future we want to make it cross-platform

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