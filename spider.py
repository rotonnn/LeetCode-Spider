import requests
import json
import selenium

from bs4 import BeautifulSoup
session = requests.Session()
COOKIES = None

def login4cookies():
    #登录
    url = 'https://leetcode.com'
    cookies = session.get(url).cookies
    for cookie in cookies:
        if cookie.name == 'csrftoken':
            csrftoken = cookie.value
    
    URL = 'https://leetcode-cn.com/accounts/login/'
    
    header = {
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "origin": "https://leetcode-cn.com",
        "referer": "https://leetcode-cn.com/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36",
        "x-requested - with": "XMLHttpRequest",
    }
    username = input("请输入你的用户名：\n")
    password = input("请输入你的密码：\n")
    
    payloads = {
    'csrfmiddlewaretoken':csrftoken, 
    'login' : username,
    'password' : password,
    'next' : '/'
    }
    session.post(URL, data=payloads, headers=header)
    COOKIES = session.cookies
    
    return COOKIES
