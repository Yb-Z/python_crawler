'''
@Author: your name
@Date: 2020-05-25 14:37:26
@LastEditTime: 2020-05-25 15:06:03
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python file\爬蟲\python_crawler\ip查询.py
'''
import requests
url="https://m.ip138.com/iplookup.asp?ip="
print("Please input the ip that u want to find location:")
ip=str(input())
kv={'user-agent':'Mozilla/5.0'}

try:
    r=requests.get(url+ip,headers=kv)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text)
except:
    print("Error!")