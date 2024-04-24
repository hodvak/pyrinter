import os
import sys

if os.environ.get("SPHINX_BUILD") == "1":
    # import the sphinx documented class
    from .sphinx_printer import Printer

elif sys.platform in ["win32", "cygwin"]:
    from .win_printer import Printer
