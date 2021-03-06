# coding=gbk
from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
import time
import pickle
import datetime

# 保存 cookie
def save_cookies(cookies):
    pickle.dump(cookies, open(r"D:\zyn\cookies\net\hbyunan.pkl", 'wb'))

# 加载 cookie
def load_cookies(driver):
    cookies = pickle.load(open(r"D:\zyn\cookies\net\hbyunan.pkl", 'rb'))
     # 这里只将 domain 为 .yeah.net 和 .163.com 的加载进来
    for cookie in cookies:
        if cookie['domain'] == '.yeah.net' and cookie['domain'] == '.163.com':
            driver.add_cookie(cookie)

# 判断是否离开了某个页面
def wait_leave_page(driver, url, max_sec=10):
    time.time()
    startTime = datetime.datetime.now();
    while True:
        if (datetime.datetime.now() - startTime).seconds > max_sec:
            print('超过%d秒,页面没有离开%s' % (max_sec, driver.current_url))
            return False
        if driver.current_url.find(url) != -1:
            return True
        time.sleep(1)


def login():
    # 加载 chrome 的 driver 这里会打开一个谷歌浏览器
    # 注意 chromedriver.exe 文件的路径
    driver = webdriver.Chrome(r"d:\chromedriver.exe")
    # 打开网易邮箱登录页面
    driver.get("http://221.192.190.15:7001/")
    assert "BIMS宽带计费及业务综合管理系统" in driver.title
    # 因为 网易邮箱登录页面账号输入框在 <iframe id = 'x-URS-iframe' ... >... 中
    # 这里先 跳到 这个 iframe 中
    driver.switch_to.frame("x-URS-iframe")

    # 根据 name 找到 密码输入框
    # <input name="password" >
    elem = driver.find_element_by_name("passwd")
    # 清空原有内容
    elem.clear()
    # 填入密码
    elem.send_keys("aaa111!!")

    # 同理填入 账号
    elem = driver.find_element_by_name("login")
    elem.clear()
    elem.send_keys("hbyunan")

    # 得到 登录按钮并单击
    elem = driver.find_element_by_id("dologin")
    elem.click()

    # 等待 1s 并判断，是否能离开登录页面，如果能离开说明登录成功
    time.sleep(1)

    if wait_leave_page(driver, "mail"):
        print("登录成功")
        save_cookies(driver.get_cookies())
    else:
        print("登录失败")


if "__main__" == __name__:
    login()

