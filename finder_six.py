#此版本为1.0版本
#此爬虫支持jacs,joc,inorg,chem review,org lett,angrew六种文献的搜索以及下载
#finder_six
# run again.  Do not edit this file unless you know what you are doing.
'''
__time__:2021,2,8
__author__:Tosey
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import re,time,requests,os
def get_v_p():
    vol=input('vol?')       #收集卷数,页码信息
    page=input('page?')
    return vol,page

# vol=0
# page=0
# vol,page=get_v_p()
wangzhi={
    'jacs':'https://pubs.acs.org/journal/jacsat',
    'joc':'https://pubs.acs.org/journal/joceah',
    'inorg':'https://pubs.acs.org/journal/inocaj',
    'chem review':'https://pubs.acs.org/journal/chreay',
    'org lett':'https://pubs.acs.org/journal/orlef7'
}

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
}

def getacs(vol,page,mz):
    # vol=vol
    # page=page
    url=wangzhi[mz]     #获得相关文献对应的网址
    print('正在加载'+url)
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    browser=webdriver.Chrome(chrome_options=chrome_options)     #不显示浏览器界面
    browser.get(url)
    button0=browser.find_element_by_class_name('quick-search_all-field')
    button0.click()
    input1=browser.find_element(By.CLASS_NAME,'quick-search_volume-input')
    input1.send_keys(vol)
    input2=browser.find_element(By.CLASS_NAME,'quick-search_page-input')
    input2.send_keys(page)
    input2.send_keys(Keys.ENTER)
    aaaa=browser.current_url        #返回当前网址
    browser.close()
    result=re.search('doi/abs/(.*)\?jou',aaaa)      #正则表达式选取doi
    bbb=result.group(1)
    return bbb      #返回doi

def getangew(vol,page):
    # chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # browser=webdriver.Chrome(chrome_options=chrome_options)
    browser=webdriver.Chrome()      #由于技术限制，此处不隐藏标签页
    browser.get('https://www.onlinelibrary.wiley.com/search/advanced?publication=15213773&text1=#citation')
    input1=browser.find_element(By.ID,'citationVolume')
    input1.send_keys(vol)
    input2=browser.find_element(By.ID,'citationPage')
    input2.send_keys(page)
    input2.send_keys(Keys.ENTER)
    time.sleep(5)       #获得五秒缓冲
    aaaa=browser.current_url
    browser.close()
    bbbb=aaaa[::-1]     #倒置进行正则表达式选取
    sna=re.match('(.*?)/sba/iod',bbbb)
    sna1=sna.group(1)
    ans=sna1[::-1]
    return ans

def down(doi):
    address=doi
    print(doi)
    weizhi='E:\书籍资料\化竞书籍\文献'      #Tosey
    os.chdir(weizhi)
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

def get_v_p():
    vol=input('vol?')       #收集卷数,页码信息
    page=input('page?')
    return vol,page

def main():
    #主程序运行
    print('jacs:1\njoc:2\ninorg:3\nchem_review:4\norg_lett:5\nangrew:6\n')
    which=int(input('请输入对应的数字'))
    if which==1:
        vol,page=get_v_p()
        doi=getacs(vol,page,'jacs')
        down(doi)
    elif which==2:
        vol,page=get_v_p()
        doi=getacs(vol,page,'joc')
        down(doi)
    elif which==3:
        vol,page=get_v_p()
        doi=getacs(vol,page,'inorg')
        down(doi)
    elif which==4:
        vol,page=get_v_p()
        doi=getacs(vol,page,'chem review')
        down(doi)
    elif which==5:
        vol,page=get_v_p()
        doi=getacs(vol,page,'org lett')
        down(doi)   
    elif which==6:
        vol,page=get_v_p()
        doi=getangew(vol,page)
        down(doi)        
           
main()