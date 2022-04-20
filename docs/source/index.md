# Welcome to Pyrinter's documentation! #

**Pyrinter** is a free open source python package for easy way to use physical printers.  

As for the moment the package only works on windows, 
but in the future we want to make it cross platform

## How to Install ##
Install Pyrinter using [pip](https://pip.pypa.io/):
```console
$ pip install pyrinter
```

## How to Use ##
The following code is a `hello world` for printing text using the printer `PDFCreator` 
(the printer name may be empty for default printer):
```python3
from pyrinter import Printer
from pyrinter import Document

doc = Document()
doc.add_text("Hello World")

printer = Printer("PDFCreator")
printer.print_doc(doc)
```

```{toctree}
:maxdepth: 1
getting_started
```