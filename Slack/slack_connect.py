
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

def postMsg(s, channel, text) :
    try :

       s.api_call(
           "chat.postMessage",
           channel = channel,
           text = text,
           usernmae = 'iparrot',
           
       )
    except KeyError :
        print ("메시지 보내기에 실패하였습니다")


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

# 5. 채널 정보를 가져옵니다.
def channel_info(s, channel):
    channel_info = s.api_call("channels.info", channel=channel)
    if channel_info:
        return channel_info['channel']
    return None

token = 'xoxb-222751163605-d3ym2ljrLP3FU5EqLmHWUeLd'
hack_channel = "hackaton2017"


if __name__ == "__main__" :

    s = connect(token)
    channels = list_channels(s)

    if channels :
        print("채널 목록 : ")
        for c in channels :
            # 채널 아이디 얻기
            detailed_info = channel_info(s, c['id'])
            if detailed_info :

                print(c['name']+"채널의 아이디는 : "+c['id'])
            if c['name'] == 'general' :
                postMsg(s, c['id'], "general 에 보냅니다.")
            if c['name'] == 'hackaton2017' :
                postMsg(s, c['id'], "hackaton2017 에 보냅니다.")
            if c['name'] == 'random' :
                postMsg(s, c['id'], "random 에 보냅니다.")
    else:
        print("연결 실패....")



