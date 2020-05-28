'''
@Author: your name
@Date: 2020-05-26 00:59:51
@LastEditTime: 2020-05-28 01:35:09
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python file\爬蟲\python_crawler\中国大学排名定向爬虫.py
'''
import requests
import bs4
from bs4 import BeautifulSoup

def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""

def fillUnivList(ulist,html):
    soup=BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds=tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[2].string])


def printUnivList(ulist,num):
    tplr = "{0:^5}\t{1:{3}^15}\t{2:^10}"
    print(tplr.format("排名","学校","地区",chr(12288)))
    for i in range(num):
        u=ulist[i]
        print(tplr.format(u[0],u[1],u[2],chr(12288)))
    print("Suc"+str(num))

def main():
    uinfo=[]
    url="http://www.zuihaodaxue.com/Greater_China_Ranking2019_0.html"
    html=getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,20)

main()