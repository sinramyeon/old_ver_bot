import sys
import os
from flask import Flask, request, Response, make_response
from slacker import Slacker
from slackclient import SlackClient
import websocket
import json
import time
from okky_tech import get_blog_lists
from clien import clien
from ddaily import ddaily
from zdnet import zdnet
import env
from slackclient import SlackClient


# 필요한 변수들
# env.py 만들어서 설정해 놓으면 됩니다!

# 봇 토큰(봇 Oauth 토큰)
SLACK_BOT_TOKEN = env.token
slack_client = SlackClient(SLACK_BOT_TOKEN)

# Verification 토큰
SLACK_VERIFICATION_TOKEN = env.SLACK_VERIFICATION_TOKEN


# 봇에게 멘션 시 답할 멘트

attachments_json = [
    {
        "fallback": "무슨 일이신가요?",
        "color": "#3AA3E3",
        "attachment_type": "default",
        "callback_id": "menu_options_2319",
        "actions": [
            {
                "name": "IT무새가 할일",
                "text": "IT무새는 뭘 할까?",
                "type": "select",
                "data_source": "external"
            }
        ]
    }
]

attachments_json2 =  [
                {
                    "text": "IT무새를 다시 불러올까요?",
                    "fallback": "IT무새는 이미 날아간 후입니다.",
                    "callback_id": "button_tutorial",
                    "color": "#050772",
                    "attachment_type": "default",
                    "actions": [
                        {
                            "name": "yes",
                            "text": "네",
                            "type": "button",
                            "value": "yes"
                        },
                        {
                            "name": "no",
                            "text": "아니",
                            "type": "button",
                            "value": "no"
                        },
                        {
                            "name": "maybe",
                            "text": "글쎄",
                            "type": "button",
                            "value": "maybe",
                            "style": "danger"
                        }
                    ]
                }
            ]

# 플라스크 기동
app = Flask(__name__)

# 슬래커로 연결
slack = Slacker(env.token)

# 메시지를 보내는 함수
# 받아온 dict와 메시지에 설정할 컬러
def MsgSlack(x, color) :

    attachments = []

    for k, v in x.items():
        a = {}

        a["title"] = k
        a["title_link"] = v
        a["color"] = color
        attachments.append(a)

    return attachments


# 플라스크로 채널 채팅 내용을 가져옵니다.
@app.route('/slack', methods=['POST'])
def inbound():
    if request.form.get('token') == env.SLACK_WEBHOOK_SECRET:

        # 채널 이름에서
        channel = request.form.get('channel_name')
        # 누가 말했는지
        username = request.form.get('user_name')
        # 내용은?
        text = request.form.get('text')

        # "" 에게 멘션 시
        # 봇 ID(이름아님!!) 를 넣어주세요.
        if "@U6JN34THT" in text :

            if "안녕" in text :
                slack.chat.post_message(channel, "짹짹")
            if "메롱" in text :
                slack.chat.post_message(channel, ":thinking_face: ?")
            if "꺼져" in text :
                slack.chat.post_message(channel, "IT무새는 화가 나서 날아갔다!!! :anger:")
                slack.chat.post_message(channel, "", attachments= attachments_json2)
            else :
                slack.chat.post_message(channel, attachments=attachments_json)

        # "" 채널에서 말할 시
        # 채널이름(ID아님!!) 을 넣어주세요.
        if channel == "hackaton2017" :
            if "오키" in text :
                blog = get_blog_lists()
                attachments = MsgSlack(blog, "#2630b7")
                slack.chat.post_message(channel, attachments=attachments)

            if "클리앙" in text :
                write = clien(1,10,1)
                attachments = MsgSlack(write, "#26b769")
                slack.chat.post_message(channel, attachments=attachments)

            if "지디넷" in text :
                zd = zdnet()
                attachments = MsgSlack(zd, "#db7515")
                slack.chat.post_message(channel, attachments=attachments)

            if "디데일리" in text :
                dd = ddaily()
                attachments = MsgSlack(dd, "#db1515")
                slack.chat.post_message(channel, attachments=attachments)

    return Response(), 200


# 무새 -1 명령하기
@app.route("/slack/message_options", methods=["POST"])
def message_options():
    # Parse the request payload
    form_json = json.loads(request.form["payload"])

    menu_options = {
        "options": [
            {
                "text": "오키 소식 물어다 주기",
                "value": "okky"
            },
            {
                "text": "클리앙 갔다오기",
                "value": "clien"
            },
            {
                "text": "디데일리 구경하기",
                "value": "ddaily"
            },
            {
                "text": "zdnet 날아가기",
                "value": "zdnet"
            }
        ]
    }

    return Response(json.dumps(menu_options), mimetype='application/json')

# 무새 2 - 선택에 따른 명령
@app.route("/slack/message_actions", methods=["POST"])
def message_actions():

    # 리퀘스트 파징
    form_json = json.loads(request.form["payload"])

    # 선택한 값이 버튼일 때
    
    if form_json["actions"][0]["type"] == "button" :

        button =form_json["actions"][0]["value"]

        if button == "yes" :
            message_text = "IT무새는 다시 돌아왔다..."
            attachments = attachments_json
        if button == "no" :
            message_text = "그래도 IT무새는 당신을 용서한다..."
            attachments = attachments_json
        if button == "maybe" :
            message_text = "IT무새는 당신이 밉다...."
            attachments = attachments_json2


    # 선택한 값이 셀렉션일 때

    else :

        selection = form_json["actions"][0]["selected_options"][0]["value"]

        if selection == "okky":
            message_text = "오키 소식을 물어다 줄게요.\n기다려 주세요..."
            blog = get_blog_lists()
            attachments = MsgSlack(blog, "#2630b7")
        elif selection == "clien":
            message_text = "클리앙에 다녀올게요.\n기다려 주세요..."
            write = clien(1,10,1)
            attachments = MsgSlack(write, "#26b769")
        elif selection == "zdnet":
            message_text = "지디넷에 날아갔다 올게요.\n기다려 주세요..."
            zd = zdnet()
            attachments = MsgSlack(zd, "#db7515")
        elif selection == "ddaily":
            message_text = "디데일리를 구경하고 올게요.\n기다려 주세요..."
            dd = ddaily()
            attachments = MsgSlack(dd, "#db1515")

    response = slack_client.api_call(
        "chat.update",
        channel=form_json["channel"]["id"],
        ts=form_json["message_ts"],
        text=message_text,
        attachments=attachments
    )

    return make_response("", 200)


## 6. 플라스크 서버 연결 테스트용 함수
@app.route('/', methods=['GET'])
def test():
    return Response('확인!')

## 메인 시작
if __name__ == "__main__":
    app.run(debug=True)
        



