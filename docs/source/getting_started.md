(Getting Started)=
# Getting Started with Pyrinter #

## Install Pyrinter ##
install pyrinter using pip:
```sh
$ pip install pyrinter
``` 

## printer utils ##
find out about your printers data

first of all import the module:
```python3
>>> from pyrinter import printer_utils
```
now you can get all the printers names using the `get_all_printers` function:
```python3
>>> printer_utils.get_all_printers()
['printer 1', 'printer 2', 'PDFCreator', 'Microsoft Print to PDF']
```
you may also check for the default printer name using the function `get_default_printer`:
```python3
>>> printer_utils.get_default_printer()
'PDFCreator'
```

## Document ##
To print a document, the first thing you should do is create the Document:
```python3
>>> from pyrinter import Document
>>> doc = Document()
```
the `Document.__init__` method gets 2 parameters:
* `name` - the name of the document by default - `'My Document'`
* `page_size` - the size of the paper in inches (for A4 - `(8.3, 11.7)`) default is A4

now you can add text to your doc:
```python3
>>> doc.add_text("Hello World")
```
the `Document.add_text` method gets 4 parameters:
* `text` - the text that will add to the document
* `font` - the Font we are printing with see Font for more info, by default Arial 12 normal
* `page` - the page's index to print in, by default create new page and add the text to this page
* `rect` - the rect to print on in (tuple of 4 floats) in the page, by default will be 0.75 inches margin
now we want to print the document
## Printer ##
import the printer class and create instance of it:
```python3
>>> from pyrinter import Printer
>>> printer = Printer()
```
the `Printer.__init__` method gets 1 parameter:
* `name` - the name of the printer, must be one of the `printer_utils.get_all_printers()` 
           by default will be `printer_utils.get_default_printer()`

now to print the doc
```python3
>>> printer.print_doc(doc)
```
the `Printer.print_doc` gets 1 parameter:
- `doc` - the Document to print