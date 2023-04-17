import driver as driver
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time



s = Service("C:\webdriver\chromedriver")
options = Options()
# options.add_argument("--headless") #run in headless
# options.add_argument("--disable-gpu") # disable gpu
options.add_argument("--window-size=1368,720") #change device size
# options.add_argument("--disable-notifications") #disable notification bars
# options.add_argument("--disable-infobars") #disable infobars
# options.add_argument("--no-sandbox") #for server
# options.add_argument("--disable-dev-shm-usage") #for server
options.add_argument(
    "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36"
) #add user agent


driver = webdriver.Chrome(service=s, options=options)
driver.get("https://staging-api-admin.verifyplus.co.uk/")
driver.find_element(By.ID, "uname").send