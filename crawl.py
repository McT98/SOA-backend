#!/usr/bin/python
#coding:utf-8
import os
import json
from selenium import webdriver
from time import sleep
import random
from selenium.webdriver import ChromeOptions, Chrome
from os.path import dirname, join, abspath

DRIVER_PATH = "./chromedriver"
SIMI = 0.8

if __name__ == '__main__':
    option = ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    driver = webdriver.Chrome(DRIVER_PATH, chrome_options=option)

    url = "https://github.com/BlankerL/DXY-COVID-19-Data/commits/master"
    driver.get(url)
    driver.set_page_load_timeout(45)
    driver.implicitly_wait(random.randint(1, 5))

    #xpath = "//*[class=\"commit-group Box Box--condensed\"]/li[1]/div[2]/a"
    #xpath = "//*[@class=\"d-none d-md-block flex-shrink-0\"]/a"
    urls = []
    month = 'Apr'
    date = 6
    while True:
        title = driver.find_elements_by_class_name('commit-group-title')
        time = title[0].text
        print(time)
        if time.find(month) >= 0:
            date_ = time[time.find(month)+len(month)+1:time.find(',')]
            if int(date_) <= date:
                break
        items = driver.find_elements_by_css_selector("[class='d-none d-md-block flex-shrink-0']")
        for item in items:
            urls.append(item.find_element_by_tag_name('a').get_attribute('href').replace('commit', 'tree'))
        nextpage = driver.find_elements_by_class_name('BtnGroup')
        if len(nextpage) < 36:
            break
        nextpage_link = nextpage[-1].find_elements_by_tag_name('a')[-1].get_attribute('href')
        driver.get(nextpage_link)

    '''
    urls = []
    for i in range(800,1387):
        for j in range(2,22):
            xpath = "//*[@id=\"SHOW_FORUMS_TABLE\"]/tbody/tr[" + str(j) + "]/td[2]/b/a"
            item = driver.find_element_by_xpath(xpath)
            urls.append(item.get_attribute('href'))
        if i == 0:
            nextpage = driver.find_element_by_xpath("//*[@id=\"pager_top2\"]/a[10]")
        elif i < 5 or i > 1382:
            nextpage = driver.find_element_by_xpath("//*[@id=\"pager_top2\"]/a[11]")
        else:
            nextpage = driver.find_element_by_xpath("//*[@id=\"pager_top2\"]/a[12]")
        nextpage_link = nextpage.get_attribute('href')
        driver.get(nextpage_link)
        if (i+1) % 100 == 0:
            with open("F:/crawl/urls.json",'w') as f:
                json.dump(urls,f,indent=4)

    with open("F:/crawl/urls.json",'w') as f:
        json.dump(urls,f,indent=4)
    '''

    str = json.dumps(urls)
    with open('./urls.json', 'w') as f:
        f.write(str)

    driver.close()

