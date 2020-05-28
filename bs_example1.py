import requests
from bs4 import BeautifulSoup

url="https://python123.io/ws/demo.html"
r= requests.get(url)

demo =r.text
soup = BeautifulSoup(demo,"html.parser")

print(soup.prettify())
print(soup.title)

tag =soup.a  #return tag a
print(tag.name)  #tag a's name
print(tag.parent.name)   #tag a father's name
print(tag.parent.parent.name)

print(tag.attrs)  #attributes of tag a
print(type(tag.attrs))
print(type(tag))

print(tag.string)
print(tag.parent.string)

#several elements of BS
# <p>...</p>: tag 
# <p class="title">...</p> title is one of tag's attributes, dictorary
# ... between > < is NavigableString, <tag>.string
# comment

# .contents 子节点的列表，将<tag>所有儿子节点存入列表
# .children 子节点的迭代类型，与.contents类似，用于循环遍历儿子节点
# .descendants 子孙节点的迭代类型，包含所有子孙节点，用于循环遍历

