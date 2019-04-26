#!/usr/bin/env python
# encoding: utf-8

"""
@description: 去重，判断数据有没有重复

@author: baoqiang
@time: 2019-04-26 11:16
"""

import re

pat = re.compile('\\((.*)\\)$')


def dup():
    exists = set()

    with open('README.md', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()

            if not line.startswith('1. '):
                continue

            m = pat.search(line)

            repo = m.group(1)

            if repo not in exists:
                exists.add(repo)
            else:
                print("dup: {}".format(repo))

        print('repos count: {}'.format(len(exists)))


if __name__ == '__main__':
    dup()
