from urllib.parse import urlparse, unquote
from sys import argv
from subprocess import check_output, CalledProcessError
from pathlib import Path
from os import remove
from re import compile
import base64

# Base64 = b64
# Console output = c
# No level = l
# No optimize = o

out_url = None
prog = None
out = None
temp = None
file = None
console = ''
no_level = ''
no_opti = ''

try:
    out_url = urlparse(argv[1])
    params = out_url.query.split('&')
    if 'b64' in params:
        home = Path.home()
        prog = base64.b64decode(out_url.netloc).decode()
        temp = open(f'{home}/temp.spwn', 'w')
        temp.write(prog)
        temp.close()
        file = f'{home}/temp.spwn'
    else:
        file = unquote(out_url.netloc)
    if 'c' in params:
        print("Console output on.")
        console = '-c'
    if 'l' in params:
        print("No level on.")
        no_level = '-l'
    if 'o' in params:
        print("No optimize on.")
        no_opti = '-o'
    try:
        out = check_output(['spwn', 'build', file, console, no_level, no_opti])
        esc = compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        print(esc.sub('', out.decode()))
    except CalledProcessError:
        print("Failed.")
except IndexError:
    pass
input("Press Enter to exit...")