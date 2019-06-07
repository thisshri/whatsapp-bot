from selenium import webdriver

import pygame
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

pygame.mixer.init()
pygame.mixer.music.load('person_online_notification.mp3')

browser = webdriver.Chrome()
browser.get('https://web.whatsapp.com/')

css_sel_search_bar = '#side > div._3CPl4 > div > label > input'

STATUS = ''

def watch(name):
    global STATUS
    elem = browser.find_element_by_css_selector(css_sel_search_bar)
    elem.clear()
    elem.click()
    elem.send_keys(name)
    elem.send_keys(u'\ue007')
    #first item on the search list.

    #first_elem_in_search = '# pane-side > div > div > div > div:nth-child(1) > div > div'
    #user_chat = browser.find_element_by_css_selector(first_elem_in_search)
    #user_chat.click()

    el_status = browser.find_element_by_css_selector('#main > header')
    str_status = el_status.text

    if str_status.find('online') != -1:
        STATUS = 'online'
        #print("online")
    elif str_status.find('last') != -1 :
        STATUS = ''
        #print(str_status)

    elif str_status.find('check') != -1:
        STATUS = ''
        #print('checking status')

    else:
        STATUS = ''
        #print('Status not available')


def keepWatching(name, num):
    print("++++++++++++++++++++++ web.whatsapp scrapping started ++++++++++++++++++++++")

    for x in range(num):
        #wait for 30 secs
        time.sleep(10)
        #call watch(name)
        watch(name);
        print("staus is : ",STATUS)
        if (STATUS == "online"):
            #play the sound
            pygame.mixer.music.play()
        else:
            print(name," is offline")

