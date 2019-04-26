#!/usr/bin/env python
# encoding: utf-8

"""
@description: 翻译

@author: baoqiang
@time: 2019-04-26 11:35
"""
import json
from concurrent import futures

import requests
from py_translator import Translator
import re

filepath = '/Users/baoqiang/Downloads'
pat = re.compile('[a-zA-Z \\-_]')


def translate():
    items = build_items()
    results = translate_many(items)

    with open('{}/zh.txt'.format(filepath), 'w', encoding='utf-8') as fw:
        for item in items:
            for k, v in results:
                if k == item:
                    fw.write('{}\n'.format(v))
                    break
            else:
                print('not found: {}'.format(item))


def build_items():
    results = []
    with open('{}/en.txt'.format(filepath), 'r', encoding='utf-8') as f:
        for line in f:
            en = line.strip()

            trimed = trim(en)

            results.append(trimed)

    return results


def translate_many(cc_list):
    with futures.ThreadPoolExecutor(max_workers=20) as executor:
        to_do = []
        for cc in sorted(cc_list):
            future = executor.submit(translate_one, cc)
            to_do.append(future)
            # msg = 'Scheduled for {}: {}'
            # print(msg.format(cc, future))

        results = []
        for future in futures.as_completed(to_do):
            res = future.result()
            msg = '{} result: {!r}'
            print(msg.format(future, res))
            results.append(res)

    return results


def translate_one(trimed):
    zh = ''
    try:
        # zh = Translator().translate(text=trimed, dest='zh-cn').text
        zh = youdao_api(trimed)
    except Exception as e:
        print("err occur: {}".format(e))
    # zh = 'Formatted: {}'.format(trimed)
    return trimed, zh


def trim(text):
    res = []

    for s in text:
        m = pat.match(s)
        if m:
            res.append(s)

    return ''.join(res)


def youdao_api(text):
    # 有道词典 api
    # 传输的参数，其中 i 为需要翻译的内容
    key = {
        'type': "AUTO",
        'i': text,
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "ue": "UTF-8",
        "action": "FY_BY_CLICKBUTTON",
        "typoResult": "true"
    }

    response = requests.post(youdao_url, data=key)
    if response.status_code != 200:
        return ""

    result = response.json()
    return result['translateResult'][0][0]['tgt']


youdao_url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'

if __name__ == '__main__':
    translate()
