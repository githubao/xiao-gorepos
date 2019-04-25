#!/usr/bin/env python
# encoding: utf-8

"""
@description: 

@author: pacman
@time: 2018/2/13 11:13
"""

import json
import random
import sys
import time
from collections import OrderedDict, defaultdict
from github import Github

import requests
import re

root_path = '/Users/baoqiang/Downloads'

ps_file = '{}/ps.txt'.format(root_path)
input_file = '{}/github.txt'.format(root_path)
out_file = '{}/github.json'.format(root_path)

focus_keys = ['id', 'url', 'name', 'description', 'language',
              'forks', 'stars', 'created_at', 'updated_at', 'full_name']

# owner/repo
url_fmt = 'https://api.github.com/repos/{}'

pat = re.compile('github.com/(.*?/[0-9a-zA-Z\\-_\\.]*)\\)')


def run():
    auth = get_auth()

    datas = []
    cnt = 0
    exists = set()

    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip('\n')

            m = pat.search(line)
            if not m:
                # print('err: {}'.format(line))
                continue
            else:
                # print('proc: {} [{}]'.format(m.group(1), line))
                pass

            key = m.group(1)

            if key not in exists:
                exists.add(key)
            else:
                continue

            url = url_fmt.format(key)
            resp = requests.get(url, auth=auth)

            if resp.status_code != 200:
                continue

            print(resp.json())

            # process json
            dic = process_data(resp.json())
            if dic:
                datas.append(dic)

            cnt += 1
            if cnt % 100 == 0:
                print('process cnt: {}'.format(cnt))

                # break

    # 排序
    sorted_lst = sorted(datas, key=lambda x: x['stars'], reverse=True)

    with open(out_file, 'a', encoding='utf-8') as fw:
        for item in sorted_lst:
            json.dump(item, fw, ensure_ascii=False)
            fw.write('\n')


def get_auth():
    with open(ps_file, 'r') as f:
        for line in f:
            attr = line.strip().split(' ')

            return attr[0], attr[1]
    # return 'mailbaoqiang@gmail.com', raw_input('password: ')


def process_data(dic):
    if dic.get('id', 0) == 0:
        return {}

    res = {
        'id': dic['id'],
        'url': dic['html_url'],
        'name': dic['name'],
        'description': dic['description'],
        'forks': dic['forks'],
        'stars': dic['stargazers_count'],
        'created_at': dic['created_at'],
        'updated_at': dic['updated_at'],
        'full_name': dic['full_name'],
    }
    return res


focus_keys = ['id', 'url', 'name', 'description', 'language',
              'forks', 'stars', 'created_at', 'updated_at', 'full_name']


def main():
    run()


if __name__ == '__main__':
    main()
