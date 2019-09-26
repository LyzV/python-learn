#! /usr/bin/env python3

import re

my_str = r'Телефон: 123-12-12'
pattern = re.compile(r'\d\d\D\d\d$', re.ASCII)
if pattern.search(my_str):
    print(pattern.pattern)


