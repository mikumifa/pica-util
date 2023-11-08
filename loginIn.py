import json
import time

from requests import Session

from util.signature import getsignature, getNonce


def login_request(username, password):
    login_base_url = "https://api.manhuapica.com/"
    login_url = "auth/sign-in"
    payload = {
        "email": username,
        "password": password
    }
    ts = str(int(time.time()))  # 用实际时间戳替换

    headers = {
        'authority': 'api.manhuapica.com',
        'accept': 'application/vnd.picacomic.com.v1+json',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5,ja;q=0.4',
        'app-channel': '1',
        'app-platform': 'android',
        'app-uuid': 'webUUID',
        'authorization': '',
        'content-type': 'application/json; charset=UTF-8',
        'image-quality': 'medium',
        'nonce': getNonce(),
        'origin': 'http://manhuapica.com',
        'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'signature': getsignature(login_url, ts, "POST"),
        'time': ts,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'
    }

    session = Session()
    # 发送登录请求
    response = session.post(login_base_url + login_url, headers=headers, json=payload)
    data = json.loads(response.text)
    token = data["data"]["token"]
    headers['authorization'] = token
    session.headers.update(headers)
    return session


def login_can(username, password):
    login_base_url = "https://api.manhuapica.com/"
    login_url = "auth/sign-in"
    payload = {
        "email": username,
        "password": password
    }
    ts = str(int(time.time()))  # 用实际时间戳替换

    headers = {
        'authority': 'api.manhuapica.com',
        'accept': 'application/vnd.picacomic.com.v1+json',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5,ja;q=0.4',
        'app-channel': '1',
        'app-platform': 'android',
        'app-uuid': 'webUUID',
        'authorization': '',
        'content-type': 'application/json; charset=UTF-8',
        'image-quality': 'medium',
        'nonce': getNonce(),
        'origin': 'http://manhuapica.com',
        'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'signature': getsignature(login_url, ts, "POST"),
        'time': ts,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'
    }

    try:
        session = Session()
        response = session.post(login_base_url + login_url, headers=headers, json=payload)
        data = json.loads(response.text)
        token = data["data"]["token"]
        headers['authorization'] = token
        return True
    except Exception as e:
        return False
