# -*- coding: utf-8 -*-

import requests
import md5sign1
from importlib import reload
import sys
reload(sys)


def get_content_emotion(plus_item):
    url = "https://api.ai.qq.com/fcgi-bin/nlp/nlp_textpolar"  # API地址
    params = md5sign1.get_params(plus_item)#获取请求参数
    url = url+'?'+ str(params)#请求地址拼接

    try:
        r = requests.get(url)
        #print(r.json()['data'])
        return r.json()['data']['polar'],r.json()['data']['confd']

    except Exception:
        print('error')
        return 0,0,0


if __name__ == '__main__':
    texts = ["展示完了", "之后写论文再完善一下子"]
    for text in texts:
        polar, confd = get_content_emotion(text)
        print('文本：'+str(text)+'\n'+'情感倾向：'+str(polar)+' '+'置信度：' + str(confd)+"\n")

