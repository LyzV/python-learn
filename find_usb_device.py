#! /usr/bin/env python3

import os
import re
import subprocess


def get_dev_size(device_name: str) -> str:
    split_device_name = re.split('/', device_name)
    short_device_name = split_device_name[-1]
    ret = subprocess.run('lsblk', stdout=subprocess.PIPE)
    if 0 != ret.returncode:
        return '0'
    output_lines = re.split('\n', ret.stdout.decode('utf-8'))
    for line in output_lines:
        if re.search(short_device_name, line):
            fields = re.split(r' +', line)
            return fields[3]
    return '0'


def get_device_info_list() -> list:
    dev_list = []
    file_list = os.listdir(path="/dev/disk/by-id/")
    for file in file_list:
        if not re.match('usb-', file):
            continue
        # fill device information
        device_info = []
        rl = os.readlink('/dev/disk/by-id/' + file)
        split_dev_path = re.split('/', rl)
        dev_path = '/dev/' + split_dev_path[2]
        device_info.append(file)  # device id
        device_info.append(dev_path)  # full device name
        device_info.append(get_dev_size(dev_path))  # device size
        dev_list.append(device_info)

    return dev_list


device_info_list = get_device_info_list()
for device_info in device_info_list:
    print(device_info[0] + '\t' + device_info[1] + '\t' + device_info[2])





