from slacker import Slacker

slack = Slacker('xoxb-222751163605-h04yphiEhPFQZwQ2pbYHpT9D')

# Send a message to #general channel
slack.chat.post_message('#general', 'Hello fellow slackers!')