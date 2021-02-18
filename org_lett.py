from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

vol=input('vol?')
page=input('page?')
browser=webdriver.Chrome()
browser.get('https://pubs.acs.org/journal/orlef7')
button0=browser.find_element_by_class_name('quick-search_all-field')
button0.click()
input1=browser.find_element(By.CLASS_NAME,'quick-search_volume-input')
input1.send_keys(vol)
input2=browser.find_element(By.CLASS_NAME,'quick-search_page-input')
input2.send_keys(page)
input2.send_keys(Keys.ENTER)
print(browser.current_url)

browser.close()