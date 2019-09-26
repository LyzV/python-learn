#! /usr/bin/env python3

import os
import subprocess
import time


# directories of most important user data
sources = ['/home/lyzv/work/prj/']
# archive directory
archive_dir = '/home/lyzv/work/archive'
# target file of archive
target = archive_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
# archiving cmd
cmd = ['zip', '-qr', target]
for src in sources:
    cmd.append(src)
print(cmd)
result = subprocess.run(cmd)
if 0 != result.returncode:
    print('I can not create archive copy!')
else:
    print('Archive copy created successfully.')



