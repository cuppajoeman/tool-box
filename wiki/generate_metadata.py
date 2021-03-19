import pyperclip

import sys

args = sys.argv

pyperclip.copy('{{Knowledge Metadata|' + args[1] + '|' + args[2] + '}}')
