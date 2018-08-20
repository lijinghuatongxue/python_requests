##  环境
python 3.5.2

## 依赖库
requests
lxml

## 安装依赖库
`pip install  lxml`

`pip install  requests` 


## 放脚本

```
(papa) [root@pa2 first]#python ll.py 

name: ['肖申克的救赎 The Shawshank Redemption']

导演: ['弗兰克·德拉邦特']

主演: ['蒂姆·罗宾斯', '摩根·弗里曼', '鲍勃·冈顿', '威廉姆·赛德勒', '克兰西·布朗', '吉尔·贝罗斯', '马克·罗斯顿', '詹姆斯·惠特摩', '杰弗里·德曼', '拉里·布兰登伯格', '尼尔·吉恩托利', '布赖恩·利比', '大卫·普罗瓦尔', '约瑟夫·劳格诺', '祖德·塞克利拉', '保罗·麦克兰尼', '芮妮·布莱恩', '阿方索·弗里曼', 'V·J·福斯特', '弗兰克·梅德拉诺', '马克·迈尔斯', '尼尔·萨默斯', '耐德·巴拉米', '布赖恩·戴拉特', '唐·麦克马纳斯']

时长: ['142分钟']

(papa) [root@pa2 first]#cat ll.py 

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

```




