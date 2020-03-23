#coding:utf-8
import os
import json
import Levenshtein
from selenium import webdriver
from time import sleep
import random
from selenium.webdriver import ChromeOptions, Chrome
from os.path import dirname, join, abspath
import sys

DRIVER_PATH = "./chromedriver"
SIMI = 0.8

if __name__ == '__main__':
    #reload(sys)
    #sys.setdefaultencoding('utf-8')
    option = ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    driver = webdriver.Chrome(DRIVER_PATH, chrome_options=option)

    default = 'https://github.com/BlankerL'
    with open('./urls.json', 'r') as f:
        urls = json.load(f)
    print(len(urls))
    for i in range(100, len(urls), 7):
        #url = "https://github.com/BlankerL/DXY-COVID-19-Data/blob/9a76e244d203d3ec63b93bf3af6c7163ca7df5ed/json/DXYArea.json"
        url = urls[i]
        if url.index(default) < 0 or len(url) <= len(default):
            continue
        try:
            driver.get(url+'/json/DXYArea.json')
            print(url+'/json/DXYArea.json')
            driver.set_page_load_timeout(45)
            driver.implicitly_wait(random.randint(1, 5))
        except:
            continue

        try:
            title = driver.find_element_by_css_selector("[class='lh-default v-align-middle']")
            title = title.find_element_by_tag_name('a').get_attribute('title')[0:16]
        except:
            continue
        title = title.replace(' ', '_')
        title = title.replace(':', '_')

        content = ''
        try:
            item = driver.find_element_by_tag_name('tbody')
            lines = item.find_elements_by_tag_name('tr')
        except:
            continue
        for i in range(len(lines)):
            if i % 100 == 0:
                print(i)
            content += lines[i].text.strip()
        
        content = json.loads(content)
        content = json.dumps(content, ensure_ascii=False)
        
        print('write')
        file = open('./data/'+title+'.json', 'w', encoding='utf-8')
        file.write(content)
    

    driver.close()

