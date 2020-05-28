'''
@Author: ZHANG Yubo
Crawl photos and information of ACADEMIC AND TEACHING STAFF in 
https://www.comp.polyu.edu.hk/en-us/staffs/
'''
import requests
import bs4
import pandas as pd
import os
from prettytable import PrettyTable
from bs4 import BeautifulSoup


def getHTMLText(url):
    try:
        r=requests.get(url,verify=False,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        print("error!")
        return ""

def fillUnivList(stafflist,html):
    soup=BeautifulSoup(html,"html.parser")
    staffinfo=soup.find_all(name='div',attrs={"class":"staff-info"})

    for staff in staffinfo:
        a_staffinfo=[]
        for info in staff.children:
            a_staffinfo.append(info.string)
        stafflist.append(a_staffinfo)


def printstaffs(stafflist):
    table=PrettyTable(['descreption','name'])
    descreption=[]
    name=[]
    for s in stafflist:
        descreption.append(s[1])
        name.append(s[3])
    pd.set_option('display_width',100)
    dataframe=pd.DataFrame({'descreption':descreption, 'name':name})
    table.add_column('descreption',descreption)
    table.add_column('name',name)
    
    print(dataframe)

def image(html):
    soup=BeautifulSoup(html,"html.parser")
    staffinfo=soup.find_all(name='li',attrs={"class":"staff-post-inner"})
    result=[]
    for staff in staffinfo:
        result.append('https://www.comp.polyu.edu.hk'+staff.contents[1].img['src'])
    
    folder_path = './photo/'
    if (os.path.exists(folder_path) == False):  # 判断文件夹是否已经存在
        os.makedirs(folder_path)
    for img in result:
        try:
            with open("./photo/"+img.split('/')[-1], 'wb') as file:
                file.write(requests.get(img,verify=False).content)
                file.flush()
                file.close()  # 关闭文件
        except:
            print(img.split('/')[-1],"ouput wrong!")
def main():
    stafflist=[]
    url="https://www.comp.polyu.edu.hk/en-us/staffs/index/1"
    html=getHTMLText(url)
    fillUnivList(stafflist,html)
    printstaffs(stafflist)
    image(html)

main()

