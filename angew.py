
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import re,time


vol=44
page=3485
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# browser=webdriver.Chrome(chrome_options=chrome_options)
browser=webdriver.Chrome()
browser.get('https://www.onlinelibrary.wiley.com/search/advanced?publication=15213773&text1=#citation')
input1=browser.find_element(By.ID,'citationVolume')
input1.send_keys(vol)
input2=browser.find_element(By.ID,'citationPage')
input2.send_keys(page)
input2.send_keys(Keys.ENTER)
# browser.switch_to.window(browser.window_handles[0])
time.sleep(5)
aaaa=browser.current_url
browser.close()

bbbb=aaaa[::-1]
sna=re.match('(.*?)/sba/iod',bbbb)
sna1=sna.group(1)
ans=sna1[::-1]
print(ans)