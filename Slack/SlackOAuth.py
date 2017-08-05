from urllib.parse import urlencode
import string
import random

def authorize(**kwargs):
    if 'state' in kwargs:
        token = kwargs['state']
    else:
        token = _gen_csrf_token(10)
        kwargs['state'] = token
    return 'https://slack.com/oauth/authorize?' + urlencode(kwargs), token

def oauth(**kwargs):
    return 'https://slack.com/api/oauth.access?' + urlencode(kwargs)

def _gen_csrf_token(N):
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(N))