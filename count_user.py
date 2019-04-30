#!/usr/bin/env python
# encoding: utf-8

"""
@description: 统计用户数

@author: baoqiang
@time: 2019-04-30 17:21
"""

import re
from collections import defaultdict

pat = re.compile('\\((.*)/(.*)/(.*)\\)$')


def count_user():
    count_dic = defaultdict(int)

    with open('README.md', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()

            if not line.startswith('1. '):
                continue

            m = pat.search(line)

            name = m.group(2)

            count_dic[name] += 1

    sorted_list = sorted(count_dic.items(), key=lambda x: x[1], reverse=True)

    for k, v in sorted_list:
        print('{} -> {}'.format(k, v))


if __name__ == '__main__':
    count_user()
