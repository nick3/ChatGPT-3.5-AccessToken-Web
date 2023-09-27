# -*- coding: utf-8 -*-

import os
from os import path
from certifi import where
import json
import requests

from pandora.openai.auth import Auth0


def parse_access_token(resp):
    if resp.status_code == 200:
        json = resp.json()
        if 'access_token' in json:
            return json['access_token']
        else:
            raise Exception('Get access token failed.')
    else:
        raise Exception(resp.text)
    
def get_access_token_by_refresh_token(refresh_token: str) -> str:
    url = 'https://auth0.openai.com/oauth/token'
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                          'Chrome/109.0.0.0 Safari/537.36'
    headers = {
        'User-Agent': user_agent,
    }
    data = {
        "redirect_uri": "com.openai.chat://auth0.openai.com/ios/com.openai.chat/callback",
        "grant_type": "refresh_token",
        "client_id": "pdlLIX2Y72MIl2rhLhTE9VV9bN905kBh",
        "refresh_token": refresh_token
    }
    req_kwargs = {
        'verify': where(),
        'timeout': 100,
    }
    session = requests.Session()
    resp = session.post(url=url, headers=headers, data=data, allow_redirects=False, **req_kwargs)

    return parse_access_token(resp)

def run():
    proxy = None
    expires_in = 0
    unique_name = 'my share token'
    current_path = os.getcwd()  # 获取当前工作目录路径
    parent_path = os.path.dirname(current_path)  # 获取父目录路径
    current_dir = path.dirname(path.abspath(__file__))
    credentials_file = '/config/users.txt'
    # credentials_file = path.join(current_dir, 'user.txt')

    tokens_file = '/config/tokens.txt'
    # tokens_file = path.join(current_dir, 'token.txt')

    with open(credentials_file, 'r', encoding='utf-8') as f:
        credentials = f.read().split('\n')
    credentials = [credential.split(',', 2) for credential in credentials]
    print(credentials)

    count = 0
    token_keys = []
    for credential in credentials:
        progress = '{}/{}'.format(credentials.index(credential) + 1, len(credentials))
        if not credential or len(credential) != 3:
            continue

        count += 1
        username, password, refresh_token = credential[0].strip(), credential[1].strip(), credential[2].strip()
        print('Login begin: {}, {}'.format(username, progress))
        print(password, refresh_token)

        token_info = {
            'username': username,
            'token': 'None',
            'share_token': 'None',
        }
        token_keys.append(token_info)

        try:
            if refresh_token:
                token_info['token'] = get_access_token_by_refresh_token(refresh_token)
            else:
                token_info['token'] = Auth0(username, password, proxy).auth()
            print('Login success: {}, {}'.format(username, progress))
        except Exception as e:
            err_str = str(e).replace('\n', '').replace('\r', '').strip()
            print('Login failed: {}, {}'.format(username, err_str))
            token_info['token'] = err_str
            continue

        # data = {
        #     'unique_name': unique_name,
        #     'access_token': token_info['token'],
        #     'expires_in': expires_in,
        # }
        # resp = requests.post('https://ai.fakeopen.com/token/register', data=data)
        # if resp.status_code == 200:
        #     token_info['share_token'] = resp.json()['token_key']
        #     print('share token: {}'.format(token_info['share_token']))
        # else:
        #     err_str = resp.text.replace('\n', '').replace('\r', '').strip()
        #     print('share token failed: {}'.format(err_str))
        #     token_info['share_token'] = err_str
        #     continue

    # with open(tokens_file, 'w', encoding='utf-8') as f:
    #     for token_info in token_keys:
    #         f.write('{}\n'.format(token_info['token']))


    with open(tokens_file, 'w', encoding='utf-8') as f:
        data = {token_info['username']: token_info['token'] for token_info in token_keys}
        json_data = json.dumps(data)
        f.write(json_data)


if __name__ == '__main__':
    run()