#! /usr/bin/python3

import subprocess
import os
import re
import getpass


def get_dev_list() -> list:
    dev_list = []
    file_list = os.listdir(path="/dev/")
    for file in file_list:
        if re.match('sd[a-z]', file) and (3 == len(file)):
            dev_list.append('/dev/' + file)
    dev_list.sort()
    return dev_list


def get_partition_list() -> list:
    partition_list = []
    file_list = os.listdir(path="/dev/")
    for file in file_list:
        if re.match('sd[a-z][0-9]', file) and (4 == len(file)):
            partition_list.append('/dev/' + file)
    partition_list.sort()
    return partition_list


def get_disk_dict(devl, parl) -> dict:
    disk_dict = {}
    for dev in devl:
        dev_partitions = []
        for par in parl:
            if re.match(dev, par):
                dev_partitions.append(par)
        disk_dict[dev] = dev_partitions
    return disk_dict


def list2str(the_list=[]) -> str:
    ret = ''
    for elem in the_list:
        ret += str(elem) + ' '
    return ret


def list2nstr(l=[]) -> str:
    ret = ''
    for elem in l:
        ret += str(elem) + '\n'
    return ret


def get_mounted_dict() -> dict:
    mounted_dict = {}
    file = open('/proc/mounts', 'rt')
    if file is None:
        return mounted_dict
    all_text = file.read()
    lines = re.split('\n', all_text)
    for line in lines:
        fields = re.split(' ', line)
        # first filter /dev/sd[a-z][0-9]
        if (not re.match('/dev/sd[a-z][0-9]', fields[0])) and (not (9 == fields[0])):
            continue
        # second filter /media/${USER}/
        splitted_path = re.split('/', fields[1])
        if '' == splitted_path[0]:
            del splitted_path[0]
        # print(splitted_path)
        if 'media' != splitted_path[0]:
            continue
        user = getpass.getuser()
        if user != splitted_path[1]:
            continue
        mounted_dict[fields[0]] = fields[1]

    return mounted_dict


md = get_mounted_dict()
for point in md:
    print(point[:8])
    print('\t' + point + ' ' + md[point])


