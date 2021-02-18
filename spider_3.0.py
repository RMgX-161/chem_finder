#本爬虫为spider_3.0版本，支持对URL的分析以及对相应文献的下载。
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re  # 正则模块
import requests
import os
print('''
=====  =====   ====   ====     =====     =====                 
l      [   ]     ]    [   \    [         l    l      
[===]  =====     ]    [    ]   [====     =====          ===     l==l 
    l  l         ]    [   /    [         l  \\           ---l    l  l
=====  l       ====   ====     =====     l   \\          ===  "  l==l
''')
print('此爬虫可以通过网址访问sci-hub,进行多个文献的同时下载，\n建议不要一次性下载过多篇文献\n')
print('-----------------------')
ans=input('输入网址')
aaa=input('请输入文件储存的位置\n(类似于E:\codefield\C code\C_single\exercise\everyday):\n')
os.chdir(aaa)  # 设置文件保存的位置
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
}
a=requests.get(ans,headers=headers)
b=a.text
address_array = []
results=re.findall('/(10\..*?)\s',b)
for i in results:
    c=re.search('(10\..*?)"',i)
    # print(c.group(1))
    address_array.append(c.group(1))

def fs(aaa):
    fast,slow=0,0
    while fast<len(aaa):
        if aaa[fast]==aaa[slow]:
            fast += 1
        else:
            slow+=1
            aaa[slow]=aaa[fast]
    return aaa[:slow-1]
address_array=fs(address_array)
print('一共{}篇文献'.format(len(address_array)))

ooo=0
# 下载
for address in address_array:
    ooo+=1
    print('\n第{}篇文献正在下载'.format(ooo))
    r = requests.post('https://sci-hub.se/', data={'request': address},headers=headers)
    print('\n响应结果是：', r)
    print('访问的地址是：', r.url)
    soup = BeautifulSoup(r.text, features='lxml')
    pdf_URL = soup.iframe['src']
    if re.search(re.compile('^https:'), pdf_URL):
        pass
    else:
        pdf_URL = 'https:'+pdf_URL
    print('PDF的地址是：', pdf_URL)
    name = re.search(re.compile('fdp.*?/'),pdf_URL[::-1]).group()[::-1][1::]
    print('PDF文件名是：', name)
    print('保存的位置在：', os.getcwd())
    r = requests.get(pdf_URL, stream=True)
    with open(name, 'wb') as f:
        for chunk in r.iter_content(chunk_size=32):
            f.write(chunk)
    print('第{}篇下载完成！'.format(ooo))

print('\n全部下载完成！')
kkk=input('输入任何符号后退出\n--------------------')