import requests
from lxml import etree
url='https://movie.douban.com/subject/1292052/'
data=requests.get(url).text
s=etree.HTML(data)

film=s.xpath('//*[@id="content"]/h1/span[1]/text()')
actor=s.xpath('//*[@id="info"]/span[1]/span[2]/a/text()')
director=s.xpath('//*[@id="info"]/span[3]/span[2]/a/text()')
time=s.xpath('//*[@id="info"]/span[13]/text()')
print('name:',  film)
print('导演:' , actor)
print('主演:' , director)
print('时长:' , time)
