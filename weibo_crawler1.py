'''
ZHANG Yubo
爬取微博政务类各行业5月Top100的微博ID
（根据人民日报政务指数排行榜）
'''
from selenium.webdriver.common.keys import Keys 
from selenium import webdriver
from selenium.webdriver import ActionChains
import requests
import bs4
from bs4 import BeautifulSoup
import time

def getHTMLText(url):
    driver = webdriver.Chrome("C:/Users/zyb/Desktop/chromedriver.exe")#打开浏览器
    driver.get(url)#打开你的访问地址
    for i in range(5):
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        ActionChains(driver).key_down(Keys.DOWN).perform()
        time.sleep(1)
    return driver.page_source
def fillIdList(html,IdList):
    soup = BeautifulSoup(html,'html.parser')
    tags=soup.find_all(name='div',attrs={"class":"card m-panel card30 m-avatar-box"})
    for tag in tags:
        IdList.append(tag.get('data-uid'))
def printIdList(IdList):
    index=1
    for Id in IdList:
        print(index,Id)
        index+=1

def main():
    IdList=[]
    UrlList=["https://gov.weibo.com/rank/hangye/rank?area=buwei&datetype=3&type=1",
    "https://gov.weibo.com/rank/hangye/rank?area=waixuan&datetype=3&type=1",
    "https://gov.weibo.com/rank/hangye/rank?area=gongan&datetype=3&type=1",
    "https://gov.weibo.com/rank/hangye/rank?area=jiaojing&datetype=3&type=1",
    "https://gov.weibo.com/rank/hangye/rank?area=wangjing&datetype=3&type=1",
    "https://gov.weibo.com/rank/hangye/rank?area=sifa&datetype=3&type=1",
    "https://gov.weibo.com/rank/hangye/rank?area=tuanwei&datetype=3&type=1",
    "https://gov.weibo.com/rank/hangye/rank?area=lvyou&datetype=3&type=1",
    "https://gov.weibo.com/rank/hangye/rank?area=jiaotong&datetype=3&type=1",
    "https://gov.weibo.com/rank/hangye/rank?area=tielu&datetype=3&type=1",
    "https://gov.weibo.com/rank/hangye/rank?area=gongjiao&datetype=3&type=1",
    "https://gov.weibo.com/rank/hangye/rank?area=ditie&datetype=3&type=1",
    "https://gov.weibo.com/rank/hangye/rank?area=weiji&datetype=3&type=1",
    "https://gov.weibo.com/rank/hangye/rank?area=yiyuan&datetype=3&type=1",
    "https://gov.weibo.com/rank/hangye/rank?area=jiaoyu&datetype=3&type=1"
    ]
    for url in UrlList:
        html =getHTMLText(url)
        fillIdList(html,IdList)
    printIdList(IdList)
main()
