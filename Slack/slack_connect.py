
import os
from slacker import Slacker
from slackclient import SlackClient
import websocket
import json
import time

# 1. 슬랙과 연결합니다.

def connect(token) :
    sc = SlackClient(token)
    return sc

# 2. 슬랙에 메시지를 보냅니다.

def postMsg(s, channel, text, attachments) :
    try :

        obj = s.chat.post_message(
            channel = channel,
            text = text,
            attachments = attachments,
        )

        print (obj.successful, obj.__dict__['body']['channel'], obj.__dict__[
            'body']['ts'])
    except KeyError :
        print ("연결에 실패하였습니다")


# 3. 슬랙 메시지를 받아 옵니다.

def slackListen(s) :
    if s.rtm_connect():
        while True:
            print
            read = s.rtm_read()
            time.sleep(1)
            print(read)
    else:
        print
        "Connection Failed, invalid token?"


# 4. 채널을 가져옵니다.

def list_channels(s):
    channels_call = s.api_call("channels.list")
    if channels_call.get('ok'):
        return channels_call['channels']
    return None


token = 'xoxb-222751163605-d3ym2ljrLP3FU5EqLmHWUeLd'
hack_channel = "hackaton2017"


if __name__ == "__main__" :
    s = connect(token)
    channels = list_channels(s)
    if channels :
        print("채널 목록 : ")
        for c in channels :
            print(c['name'] + " (" + c['id'] + ")")
    else:
        print("연결 실패....")
