from bs4 import BeautifulSoup
from urllib.request import urlopen
import re  # 正则模块
import requests
import os
print('此爬虫可以通过doi访问sci-hub,进行多个文献的同时下载，\n建议不要一次性下载超过10篇文献\n')
print('-----------------------')
aaa=input('请输入文件储存的位置(类似于E:\codefield\C code\C_single\exercise\everyday):\n')
os.chdir(aaa)  # 设置文件保存的位置

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
}

# 输入
address_array = []
while True:
    aa=input('输入DOI(输入q则结束):')
    if aa=='q':
        break
    else:
        address_array.append(aa)


# 下载
for address in address_array:
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
    print('\n正在下载')
    r = requests.get(pdf_URL, stream=True)
    with open(name, 'wb') as f:
        for chunk in r.iter_content(chunk_size=32):
            f.write(chunk)
    print('下载完成！')

print('\n全部下载完成！')