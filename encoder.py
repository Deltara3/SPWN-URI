from urllib.parse import quote
from os.path import abspath
from sys import argv
from base64 import b64encode
from pyperclip import copy
# Base64 = --b64
# Console output = --c
# No level = --l
# No optimization = --o

c = ''
l = ''
o = ''
output = None
try:
    if '--c' in argv:
        c = '&c'
    if '--l' in argv:
        l = '&l'
    if '--o' in argv:
        o = '&o'
    if '--b64' in argv:
        try:
            script = open(argv[1], 'r')
            content = script.read()
            script.close()
            output = f"spwn://{b64encode(content.encode()).decode()}?&b64{c}{l}{o}"
        except FileNotFoundError:
            print("File not found.")
            pass
    else:
        output = f"spwn://{quote(abspath(argv[1]))}?{c}{l}{o}"
except IndexError:
    pass
if output is not None:
    print(f"Output:\n{output}")
    copy(output)
    print("Copied to clipboard!")