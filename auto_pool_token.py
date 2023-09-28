# -*- coding: utf-8 -*-

import os
import json
import requests
from certifi import where
from pandora.openai.auth import Auth0

# 获取访问令牌的 URL
ACCESS_TOKEN_URL = 'https://auth0.openai.com/oauth/token'
# 伪装的用户代理
USER_AGENT = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
              'Chrome/109.0.0.0 Safari/537.36')

# 请求参数
REQ_KWARGS = {
    'verify': where(),
    'timeout': 100,
}

def parse_access_token(resp):
    """
    解析获取到的访问令牌。
    """
    if resp.status_code == 200:
        response_json = resp.json()
        if 'access_token' in response_json:
            return response_json['access_token']
        else:
            raise Exception('Get access token failed.')
    else:
        raise Exception(resp.text)

def login_with_refresh_token(refresh_token):
    """
    使用刷新令牌登录。
    """
    headers = {'User-Agent': USER_AGENT}
    data = {
        "redirect_uri": "com.openai.chat://auth0.openai.com/ios/com.openai.chat/callback",
        "grant_type": "refresh_token",
        "client_id": "pdlLIX2Y72MIl2rhLhTE9VV9bN905kBh",
        "refresh_token": refresh_token
    }
    resp = requests.post(url=ACCESS_TOKEN_URL, headers=headers, data=data, allow_redirects=False, **REQ_KWARGS)
    return parse_access_token(resp)

def login_with_password(username, password, proxy):
    """
    使用用户名和密码登录。
    """
    return Auth0(username, password, proxy).auth()

def handle_login(credential):
    """
    处理登录逻辑。
    """
    token_info = {
        'username': credential[0].strip(),
        'token': 'None',
        'share_token': 'None',
    }

    try:
        if len(credential) == 3:
            # 使用刷新令牌登录
            print('Login begin with refresh token: {}'.format(token_info['username']))
            token_info['token'] = login_with_refresh_token(credential[2].strip())
        elif len(credential) == 2:
            # 使用用户名和密码登录
            print('Login begin with username/password: {}'.format(token_info['username']))
            token_info['token'] = login_with_password(credential[0].strip(), credential[1].strip(), None)
    except Exception as e:
        err_str = str(e).replace('\n', '').replace('\r', '').strip()
        print('Login failed: {}, {}'.format(token_info['username'], err_str))
        token_info['token'] = err_str

    return token_info

def run():
    # current_dir = os.path.dirname(os.path.abspath(__file__))
    # credentials_file = os.path.join(current_dir, 'config', 'users.txt')
    # tokens_file = os.path.join(current_dir, 'config', 'tokens.txt')
    credentials_file = '/config/users.txt'
    tokens_file = '/config/tokens.txt'

    with open(credentials_file, 'r', encoding='utf-8') as f:
        credentials = [credential.split(',', 2) for credential in f.read().split('\n') if credential]

    token_keys = []
    for idx, credential in enumerate(credentials):
        progress = '{}/{}'.format(idx + 1, len(credentials))
        token_info = {
            'username': credential[0].strip(),
            'token': 'None',
            'share_token': 'None',
        }
        print('Login: {}, {}'.format(token_info['username'], progress))
        token_info = handle_login(credential)
        token_keys.append(token_info)

    with open(tokens_file, 'w', encoding='utf-8') as f:
        data = {token_info['username']: token_info['token'] for token_info in token_keys}
        json_data = json.dumps(data)
        f.write(json_data)

if __name__ == '__main__':
    run()
