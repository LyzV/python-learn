#! /usr/bin/env python3

import os
import subprocess
import time
import tarfile
import sys


def get_options() -> dict:
    ret_dict = {'retcode': 0, '-s':[], '-a':''}
    arguments = sys.argv
    del arguments[0]
    src_list = []
    state = '-n' # state_list = ('-n', '-s', '-s2', '-a', '-a2')
    for arg in arguments:
        if state == '-n':
            if arg == '-s':
                ret_dict['-s'] = ''
                state = '-s2'
            elif arg == '-a':
                ret_dict['-a'] = ''
                state = '-a2'
            else:
                ret_dict['retcode'] = 1
                return ret_dict
        elif state == '-s2':
            if arg == '-a':
                ret_dict['-s'] = src_list
                ret_dict['-a'] = ''
                state = '-a2'
            else:
                src_list.append(arg)
        elif state == '-a2':
            if arg == '-s':
                ret_dict['retcode'] = 1
                return ret_dict
            else:
                ret_dict['-a'] = arg
                state = '-n'
        else:
            ret_dict['retcode'] = 1
            return ret_dict

    if 's2' == state:
        ret_dict['-s'] = src_list
    ret_dict['retcode'] = 0
    return ret_dict

# directories of most important user data
sources = ['/home/lyzv/work/prj/']
# archive directory
archive_dir = '/home/lyzv/work/archive'

options = get_options()
if 0 != options['retcode']:
    print('Fail arguments. Program stopped')
    exit(1)
print('sources=' + options['-s'])



# today directory
today = archive_dir + os.sep + time.strftime('%Y%m%d')
# short target file name
now = time.strftime('%H%M%S')
# create today directory
if not os.path.exists(today):
    os.makedirs(today)
print('Directory {0} created successfully!'.format(today))
# Comment of archive
comment = input('Enter a comment: ')
# target file of archive
if 0 == len(comment):
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
        comment.replace(' ', '_') + '.zip'
# archiving cmd
cmd = ['zip', '-qr', target]
for src in sources:
    cmd.append(src)
print('Waiting for archiving has finished ...')
result = subprocess.run(cmd)
if 0 != result.returncode:
    print('I can not create archive copy!')
else:
    print('Archive copy created successfully.')



