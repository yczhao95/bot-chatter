#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import requests    
import md5sign
import time
import sentimental_analysis as emo
  
def get_content(plus_item):      
    # 聊天的API地址      
    url = "https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat"        
    # 获取请求参数    
    plus_item = plus_item.encode('utf-8')    
    payload = md5sign.get_params(plus_item)
    #print(payload)
    # r = requests.get(url,params=payload)      
    r = requests.post(url, data=payload)
    return r.json()["data"]["answer"]    
    

if __name__ == '__main__':
    comment = input('please give a seed: ')
    now = 1
    while True:
        if comment == 'q':      
            break
        if comment == '':
            comment = input('please give a seed: ')
        answer = get_content(comment)
        polar,confd = emo.get_content_emotion(answer)
        if polar == 1:
            polar = '正面'
        else:
            polar = '负面'
        print('机器人'+str(now)+': '+answer +' 情绪:'+ polar +' 强度:'+ str(confd))
        time.sleep(2)
        comment = answer
        if now == 1:
            now = 2
        else:
            now = 1
