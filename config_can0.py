#! /usr/bin/python3

import subprocess
import sys
import re
import os.path


def config_can0(cf):
    if not os.path.exists(cf):
        return
    try:
        f = open(cf, 'tr')
    except IOError as e:
        print('Can not open file {0}'.format(cf))
    else:
        while True:
            line = f.readline()
            if len(line) == 0:  # Нулевая длина обозначает конец файла (EOF)
                break
            print(line, end='')
    finally:
        f.close()

    return


file = '../sources/meta-yogurt/recipes-core/systemd/systemd-machine-units/can0.service'
config_can0(file)
