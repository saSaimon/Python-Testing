import driver as driver
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time






chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--headless")#run in headless
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--ignore-certificate-errors")
# chrome_options.add_argument("--disable-gpu") # disable gpu
# chrome_options.add_argument("--window-size=1368,720") #change device size
# chrome_options.add_argument("--disable-notifications") #disable notification bars
# chrome_options.add_argument("--disable-infobars") #disable infobars
# chrome_options.add_argument("--no-sandbox") #for server
# chrome_options.add_argument("--disable-dev-shm-usage") #for server
chrome_options.add_argument(
    "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36"
) #add user agent

s = Service("C:\Windows\webdriver")
driver = webdriver.Chrome(service=s, options=chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)