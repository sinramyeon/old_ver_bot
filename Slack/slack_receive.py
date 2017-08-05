import sys
import os
from flask import Flask, request, Response
from slacker import Slacker
from slackclient import SlackClient
import websocket
import json
import time
from okky_tech import get_blog_lists
from clien import clien
import env

# 필요한 변수들

app = Flask(__name__)

hack_channel = "hackaton2017"
slack = Slacker(env.token)

Msg = {}
# 1. 슬랙과 연결합니다.
def connect(token):
    sc = SlackClient(token)
    return sc


# 2. 슬랙에 메시지를 보냅니다.
def postMsg(s, channel, text):
    try:
        s.chat.post_message(channel, text)
    except KeyError:
        print("메시지 보내기에 실패하였습니다")

# 3. 채널을 가져옵니다.
def list_channels(s):
    channels_call = s.api_call("channels.list")
    if channels_call.get('ok'):
        return channels_call['channels']
    return None

# 4. 채널 정보를 가져옵니다.
def channel_info(s, channel):
    channel_info = s.api_call("channels.info", channel=channel)
    if channel_info:
        return channel_info['channel']
    return None

# 5. 플라스크로 채널 채팅 내용을 가져옵니다.

@app.route('/slack', methods=['POST'])
def inbound():
    if request.form.get('token') == env.SLACK_WEBHOOK_SECRET:

        # 채널 이름에서
        channel = request.form.get('channel_name')
        # 누가 말했는지
        username = request.form.get('user_name')
        # 내용은?
        text = request.form.get('text')
        
        if channel == "hackaton2017" :
            if "오키" in text :

                blog = get_blog_lists()

                attachments = []

                for k, v in blog.items() :

                    a = {}

                    a["title"] = k
                    a["title_link"] = v
                    a["color"] = "#34c9d3"

                    attachments.append(a)

                slack.chat.post_message(channel, attachments=attachments)
            if "클리앙" in text :

                write = clien(1,10,1)

                print(write)

                attachments = []

                for k, v in write.items() :

                    a = {}

                    a["title"] = k
                    a["title_link"] = v
                    a["color"] = "#36a64f"

                    print(a)
                    attachments.append(a)

                print(attachments)
                slack.chat.post_message(channel, attachments=attachments)
        

    return Response(), 200

## 6. 플라스크 서버 연결 테스트용 함수
@app.route('/', methods=['GET'])
def test():
    return Response('확인!')

## 메인 시작

if __name__ == "__main__":

    app.run(debug=True)
        



