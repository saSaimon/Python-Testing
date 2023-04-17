import driver as driver
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time




s = Service("C:\webdriver\chromedriver")
# s1= Service("D:\Programming with Saimon\Selenium webdriver with python")
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
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(5)
# #wait untill 5 seconds if objects are not displayed
#global wait
#1.5 second to rach next page-execution will resume in 1.5 seconds
#if objcets do not show at all then maximum time your test waits 5 seconds
driver.find_element(By.CSS_SELECTOR, "input.search-keyword").send_keys("ber")
time.sleep(4)
count=len(driver.find_elements(By.XPATH, "//div[@class='products']/div"))
assert count == 3
print(count)
buttons = driver.find_elements(By.XPATH, "//div[@class='product-action']/button")
for button in buttons:
    button.click()
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver, 5)
wait.until(expected_conditions.presence_of_element_located(By.CSS_SELECTOR, "input[class='promoCode']"))
driver.find_element(By.CSS_SELECTOR, "input[class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

wait.until(expected_conditions.presence_of_element_located(By.CSS_SELECTOR, "span.promoinfo"))
print(driver.find_element(By.CSS_SELECTOR, "span.promoinfo").text)