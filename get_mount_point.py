#! /usr/bin/python3

import subprocess
import sys
import re


def get_mount_point(partition) -> str:
    ret = ''
    file = open('/proc/mounts', 'rt')
    if file is None:
        return ret
    all_text = file.read()
    lines = re.split('\n', all_text)
    for line in lines:
        fields = re.split(r'\s+', line)
        partition = partition.strip()
        field = fields[0].strip()
        if re.match(partition, field):
            if len(field) == len(partition):
                # ret = fields[1].strip()
                ret = re.sub(r'\\\\', fields[1].strip(), r'\\')
                break
    file.close()
    return ret


if 1 < len(sys.argv):
    mp = get_mount_point(sys.argv[1])
    if 0 < len(mp):
        print(mp)
