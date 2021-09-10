from os.path import dirname, abspath
from os import remove
from sys import executable
from subprocess import run

py_path = dirname(executable).replace('\\', '\\\\')
scr_name = abspath('decoder.py').replace('\\', '\\\\')

reg_file = f"Windows Registry Editor Version 5.00\n\n[HKEY_CLASSES_ROOT\\spwn]\n\"URL Protocol\"=\"\"\n@=\"URL:spwn Protocol\"\n\n[HKEY_CLASSES_ROOT\\spwn\\shell]\n\n[HKEY_CLASSES_ROOT\\spwn\\shell\\open]\n\n[HKEY_CLASSES_ROOT\\spwn\\shell\\open\\command]\n@=\"\\\"{py_path}\\\\python.exe\\\" \\\"{scr_name}\\\" \\\"%1\\\"\""
file = open('temp.reg', 'w')
file.write(reg_file)
file.close()
path = abspath('temp.reg')
run(['REG', 'IMPORT', path])
remove("temp.reg")