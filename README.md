# HQ_bot

python 으로 만든 slack bot입니다. 사용 라이브러리는 아래와 같습니다.

1. Flask
2. Slacker
3. SlackClient
4. bs4
5. FeedParser

---

위 봇은 아래와 같이 작동합니다.
![](https://raw.githubusercontent.com/hero0926/HQ_bot/master/1.gif)
![](https://raw.githubusercontent.com/hero0926/HQ_bot/master/2.gif)

---

## 사용법

### @봇 이름

봇에게 멘션할 시 

### 오키, 클리앙 , 지디넷, 디데일리, 블로그, 시사 키워드 입력 시 해당 사이트를 크롤링하여 보여줍니다.

---

## 설정법

1. 슬랙 앱부터 만듭니다.(https://api.slack.com/apps/)
![](https://www.fullstackpython.com/img/160604-simple-python-slack-bot/sign-in-slack.png)
저기서 만드시면 됩니다.

만드신 후 여기(https://api.slack.com/bot-users)로 이동하셔서, 봇을 만드세요.
![](https://www.fullstackpython.com/img/160604-simple-python-slack-bot/custom-bot-users.png)
왜 앱에서 봇을 만드냐면, 앱만이 interaction(사용자의 버튼 클릭 등)을 할 수 있거든요!

2. 슬랙 봇 토큰들을 등록합니다.
![](https://raw.githubusercontent.com/hero0926/HQ_bot/master/1.gif)

3. oAuth도 만들어서 등록합니다.
![](https://raw.githubusercontent.com/hero0926/HQ_bot/master/2.gif)

위 곳에서 등록할 수 있습니다.(사실 어디인지 찾기가 아주 불편합니다)

5. 이 내용들을 env.py안에 등록하여 사용합니다.
> 자신의 개인정보는 소중하니 이 정보들을 깃허브 등에 올리지 않게 주의 하도록 하세요.

6. 서버를 만듭니다.
	가. 로컬 서버인 경우
		a. ngrok를 까세요.
		b. 그리고 ngrok가 있는 곳에 가서 cmd창에 `./ngrok http 5000`을 쳐보세요.(5000은 포트 번호예요.)
		c. ![](https://realpython.com/images/blog_images/slack-api/ngrok.png)
		d. 이렇게 online 이 뜨면 되어요.
		여기서 뜬 주소에서 Forwarding 에 있는 주소가 외부에서 자신의 컴퓨터로 접속하는 주소입니다.

	나. 이미 있는 경우
		a. `자신의 주소/slack/message_actions` 와 `/slack/message_options` 로 설정하세요.


7. ![](/src/HQ_bot/slack3.png) 여기가 보이시나요?
여기서 이 주소를 설정 하세요.
위는 버튼 클릭 등에 대한 리퀘스트를 받아 올 주소이고, 아래는 옵션 선택에 대한 값을 받아 올 주소입니다.
저희 봇에서는 차례로 `/slack/message_actions`과 `/slack/message_options` 로 설정했어요.

8. outgoing webhook(https://api.slack.com/outgoing-webhooks) 설정 페이지로 가서, ![](https://realpython.com/images/blog_images/slack-api/slack-outgoing-webhooks.png) 를 설정하세요.

9. ![](https://realpython.com/images/blog_images/slack-api/slack-outgoing-webhooks-settings.png) 포스팅할 채널 이름을 입력하고, URL에 저런식으로 `자기 주소/slack`으로 설정하세요.

10. 설정에 `SLACK_WEBHOOK_SECRET` 도 등록하세요.

11. `pip install requirements.txt`로 필요 라이브러리도 설치 한 후,

12. 봇을 `python slack.py` 로 실행 해 보세요

---

##### 질문이나 안되는 기능은 이슈에 적어 주세요.
