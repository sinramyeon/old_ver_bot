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
import env
from slackclient import SlackClient


# 필요한 변수들
SLACK_BOT_TOKEN = env.token
SLACK_VERIFICATION_TOKEN = env.SLACK_VERIFICATION_TOKEN
slack_client = SlackClient(SLACK_BOT_TOKEN)

app = Flask(__name__)

hack_channel = "hackaton2017"
slack = Slacker(env.token)

Msg = {}

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

        if "@U6JN34THT" in text :
            slack.chat.post_message(channel, attachments=attachments_json)

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

                    attachments.append(a)

                slack.chat.post_message(channel, attachments=attachments)

    return Response(), 200

# 봇에게 멘션 시

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
            }
        ]
    }

    return Response(json.dumps(menu_options), mimetype='application/json')


@app.route("/slack/message_actions", methods=["POST"])
def message_actions():

    # Parse the request payload
    form_json = json.loads(request.form["payload"])

    # Check to see what the user's selection was and update the message
    selection = form_json["actions"][0]["selected_options"][0]["value"]

    if selection == "okky":
        message_text = "오키 소식을 물어다 줄게요.\n기다려 주세요..."
    else:
        message_text = ":horse:"

    response = slack_client.api_call(
        "chat.update",
        channel=form_json["channel"]["id"],
        ts=form_json["message_ts"],
        text=message_text,
        attachments=[]
    )

    return make_response("", 200)



## 6. 플라스크 서버 연결 테스트용 함수
@app.route('/', methods=['GET'])
def test():
    return Response('확인!')

## 메인 시작

if __name__ == "__main__":

    app.run(debug=True)
        



