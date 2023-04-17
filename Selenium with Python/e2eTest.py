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
# chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--headless")#run in headless
# chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--ignore-certificate-errors")
# chrome_options.add_argument("--disable-gpu") # disable gpu
# chrome_options.add_argument("--window-size=1368,720") #change device size
# chrome_options.add_argument("--disable-notifications") #disable notification bars
# chrome_options.add_argument("--disable-infobars") #disable infobars
# chrome_options.add_argument("--no-sandbox") #for server
# chrome_options.add_argument("--disable-dev-shm-usage") #for server
# chrome_options.add_argument(
#     "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36"
# ) #add user agent

s = Service("C:\webdriver\chromedriver")
driver = webdriver.Chrome(service=s, options=chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

# //div[@class='card h-100']/div/h4/a
for product in products:
    productName = product.find_element(By.XPATH, "div/h4/a").text

    if productName == "Blackberry":
        product.find_element(By.XPATH, "//div[@class='card h-100']/div[2]/button").click()
driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
driver.find_element(By.ID, "country").send_keys("ind")
wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
successText = driver.find_element(By.CSS_SELECTOR, '.alert').text
assert "Success! Thank you!" in successText
driver.get_screenshot_as_file("screen.png")