from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

vol=125
page=6042
browser=webdriver.Chrome()
browser.get('https://pubs.acs.org/action/quickLink?quickLink=true&quickLinkJournal=jacsat&quickLinkVolume={}&quickLinkPage={}'.format(str(vol),str(page)))
