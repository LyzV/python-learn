
import subprocess
import re


class LinuxCmd:
    def __init__(self):
        self.ret_code = 0  # return code of linux command
        self.result = []  # output of command

    def __del__(self):
        self.ret_code = 0
        self.result = []

    def produce(self, cmd):
        ret = subprocess.run(cmd, stdout=subprocess.PIPE)
        self.result = []
        self.ret_code = ret.returncode
        if 0 != self.ret_code:
            return self.ret_code
        output_lines = re.split('\n', ret.stdout.decode('utf-8'))
        for line in output_lines:
            fields = re.split(r' +', line)
            self.result.append(fields)
        return self.ret_code

    def print(self):
        print('return code: {0}'.format(self.ret_code))
        for line in self.result:
            print(line)


linux_cmd = LinuxCmd()
args = ["ls", "-la"]
linux_cmd.produce(args)
linux_cmd.print()
