
import mymodule
import os
import subprocess

file_lines = os.popen("ls -la").read()
print('\n\n')

print('ls -la')
files = ' '
for line in file_lines.split('\n'):
    # print(line)
    words = line.split(' ')
    for word in words:
        pass
    files += ' ' + word

print(files)
mymodule.sayhi()
print('Версия', mymodule.__version__)
print(dir(mymodule))

