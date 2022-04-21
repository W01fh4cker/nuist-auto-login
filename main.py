print("""
@Author: W01f
@repo: https://github.com/W01fh4cker/nuist-auto-login/
@version: 1.0
@time: 2022/4/21
             _     _                    _              _             _       
 _ __  _   _(_)___| |_       __ _ _   _| |_ ___       | | ___   __ _(_)_ __  
| '_ \| | | | / __| __|____ / _` | | | | __/ _ \ _____| |/ _ \ / _` | | '_ \ 
| | | | |_| | \__ \ ||_____| (_| | |_| | || (_) |_____| | (_) | (_| | | | | |
|_| |_|\__,_|_|___/\__|     \__,_|\__,_|\__\___/      |_|\___/ \__, |_|_| |_|
                                                               |___/         
""")
from requests import get, post
from time import perf_counter, sleep
import json
import configparser
import os

def getConfig(section, key):
    config = configparser.ConfigParser()
    a = os.path.split(os.path.realpath(__file__))
    path = 'data.conf'
    config.read(path,encoding="utf-8")
    return config.get(section, key)

def get_ip() -> str:
    json = get(url="http://10.255.255.34/api/v1/ip").json()
    ip = json["data"]
    return str(ip)

def login(ip):
    res2 = {"username": phone, "password": password, "channel": type,
            "ifautologin": "0", "pagesign": "secondauth", "usripadd": ip}
    resp2 = post(url="http://10.255.255.34/api/v1/login",
                 data=json.dumps(res2, separators=(",", ":"))).json()
    outport = resp2["data"]["outport"]
    code = resp2["code"]
    if code == 200:
        print("[√]连接成功！")
    else:
        print("[√]连接失败。请先自查原因，若确实没有，请联系邮箱sharecat2022@gmail.com反馈！")
    if not operator == outport:
        sleep(3)
        login(ip)

def logout(ip):
    auth = {"username": phone, "password": password, "ifautologin": "0",
            "pagesign": "thirdauth", "channel": "0", "usripadd": ip}
    post(url="http://10.255.255.34/api/v1/logout",
         data=json.dumps(auth, separators=(",", ":")))

if __name__ == '__main__':
    try:
        phone = getConfig("data","phone")
        password = getConfig("data","password")
        operator = getConfig("data","operator")
        if operator == "中国移动":
            type = "2"
        elif operator == "中国电信":
            type = "3"
        else:
            type = "4"
        ip = get_ip()
        login(ip)
        # logout(ip)
    except Exception as e:
        print(e)