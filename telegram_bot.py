from crawling.okky_tech import get_blog_lists
import telegram

okky_list = get_blog_lists()
texts = '안녕하세요! OKKY의 인기 많은 TECH 뉴스를 정리해드립니다. \n '

for key in okky_list:
    texts = texts + ' \n ' + str(key) + str(okky_list[key])

# print(message)


# print(okky_list)
bot = telegram.Bot(token='427898694:AAELlD5oznmGGuskujn-L8VJQgHzpQglZlY')

updates = bot.getUpdates()
# print(updates)

# for u in updates:
#     print(u.message)
chat_id = bot.getUpdates()[-1].message.chat.id

bot.sendMessage(chat_id=chat_id, text=texts)

