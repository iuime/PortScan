# -*- coding:utf8 -*- #
import smtplib
import requests
import base64,sys,re,json


def sendWebhook(alertMsg,Webhookkey,title):
    #钉钉告警配置
    #url = "https://oapi.dingtalk.com/robot/send?access_token="+Webhookkey
    #headers = {'Content-Type': 'application/json;charset=utf-8'}
    #data_text = {
    #"msgtype": "text",
    #"text": {
    #    "content": "端口扫描机器人\n"+alertMsg
    #},
    #    "isAtAll": False  #此处为是否@所有人
    #}
    
    #发送链接消息
    #data_link = {
    #"msgtype": "link",
    #"link": {
    #    "text": "任务通知-这是一条消息", #消息内容
    #    "title": "历史的车轮滚滚向前", #消息标题
    #    "picUrl": "https://i.loli.net/2021/09/26/JNTYrWKywd34Lqb.jpg",#图片链接
    #"messageUrl": "https://developers.dingtalk.com/document/robots/custom-robot-access/title-zob-eyu-qse" 
    #消息跳转链接

#}}

    #Lark 告警配置
    url = "https://open.larksuite.com/open-apis/bot/v2/hook/"+Webhookkey
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    data_text = {
    "msg_type": "text",
    "content": {
        "text": "端口扫描机器人\n"+alertMsg
    }
    }
    print (alertMsg)


    # 发送文字消息
    r = requests.post(url,data=json.dumps(data_text),headers=headers)
    # 发送链接消息
    #r = requests.post(url, data=json.dumps(data_link), headers=headers)
    print(r.text)
