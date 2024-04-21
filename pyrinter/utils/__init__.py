import os
import sys

if os.environ.get('SPHINX_BUILD') == '1':
    # import the sphinx documented class
    from . import sphinx_utils as printer_utils

elif sys.platform in ['win32', 'cygwin']:
    from . import win_utils as printer_utils
