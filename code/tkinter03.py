# coding=gbk
from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
import time
import pickle
import datetime

# ���� cookie
def save_cookies(cookies):
    pickle.dump(cookies, open(r"D:\zyn\cookies\net\hbyunan.pkl", 'wb'))

# ���� cookie
def load_cookies(driver):
    cookies = pickle.load(open(r"D:\zyn\cookies\net\hbyunan.pkl", 'rb'))
     # ����ֻ�� domain Ϊ .yeah.net �� .163.com �ļ��ؽ���
    for cookie in cookies:
        if cookie['domain'] == '.yeah.net' and cookie['domain'] == '.163.com':
            driver.add_cookie(cookie)

# �ж��Ƿ��뿪��ĳ��ҳ��
def wait_leave_page(driver, url, max_sec=10):
    time.time()
    startTime = datetime.datetime.now();
    while True:
        if (datetime.datetime.now() - startTime).seconds > max_sec:
            print('����%d��,ҳ��û���뿪%s' % (max_sec, driver.current_url))
            return False
        if driver.current_url.find(url) != -1:
            return True
        time.sleep(1)


def login():
    # ���� chrome �� driver ������һ���ȸ������
    # ע�� chromedriver.exe �ļ���·��
    driver = webdriver.Chrome(r"d:\chromedriver.exe")
    # �����������¼ҳ��
    driver.get("http://221.192.190.15:7001/")
    assert "BIMS����ƷѼ�ҵ���ۺϹ���ϵͳ" in driver.title
    # ��Ϊ ���������¼ҳ���˺�������� <iframe id = 'x-URS-iframe' ... >... ��
    # ������ ���� ��� iframe ��
    driver.switch_to.frame("x-URS-iframe")

    # ���� name �ҵ� ���������
    # <input name="password" >
    elem = driver.find_element_by_name("passwd")
    # ���ԭ������
    elem.clear()
    # ��������
    elem.send_keys("aaa111!!")

    # ͬ������ �˺�
    elem = driver.find_element_by_name("login")
    elem.clear()
    elem.send_keys("hbyunan")

    # �õ� ��¼��ť������
    elem = driver.find_element_by_id("dologin")
    elem.click()

    # �ȴ� 1s ���жϣ��Ƿ����뿪��¼ҳ�棬������뿪˵����¼�ɹ�
    time.sleep(1)

    if wait_leave_page(driver, "mail"):
        print("��¼�ɹ�")
        save_cookies(driver.get_cookies())
    else:
        print("��¼ʧ��")


if "__main__" == __name__:
    login()

