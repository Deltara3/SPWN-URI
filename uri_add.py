from os.path import dirname, abspath
from os import remove
from sys import executable, platform
from subprocess import run
from pathlib import Path

if platform == 'win32':
    py_path = dirname(executable).replace('\\', '\\\\')
    scr_name = abspath('decoder.py').replace('\\', '\\\\')

    reg_file = f"Windows Registry Editor Version 5.00\n\n[HKEY_CLASSES_ROOT\\spwn]\n\"URL Protocol\"=\"\"\n@=\"URL:spwn Protocol\"\n\n[HKEY_CLASSES_ROOT\\spwn\\shell]\n\n[HKEY_CLASSES_ROOT\\spwn\\shell\\open]\n\n[HKEY_CLASSES_ROOT\\spwn\\shell\\open\\command]\n@=\"\\\"{py_path}\\\\python.exe\\\" \\\"{scr_name}\\\" \\\"%1\\\"\""
    file = open('temp.reg', 'w')
    file.write(reg_file)
    file.close()
    path = abspath('temp.reg')
    run(['REG', 'IMPORT', path])
    remove("temp.reg")
elif platform.startswith('linux'):
    py_path = dirname(executable)
    scr_name = abspath('decoder.py')

    home_dir = Path.home()
    entry = f"[Desktop Entry]\nType=Application\nName=SPWN Scheme Handler\nExec={py_path}/python3 {scr_name} %u\nStartupNotify=false\nMimeType=x-scheme-handler/spwn;"
    file = open(f'{home_dir}/.local/share/applications/spwn-handler.desktop', 'w')
    file.write(entry)
    file.close()
    run(['xdg-mime', 'default', 'spwn-handler.desktop', 'x-scheme-handler/spwn'])
else:
    print(f"Platform '{platform}' is currently unsupported.")