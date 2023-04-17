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
# driver=webdriver.Edge(service=s1, options=options)
driver.get("https://rahulshettyacademy.com/angularpractice/")
# driver.find_element(By.NAME,"name").send_keys("saimon")

driver.find_element(By.ID, "exampleCheck1").click()

dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
# dropdown.select_by_index(1)
# dropdown.select_by_value("M")
driver.find_element(By.XPATH, "//input[@name='email']").send_keys("msasaimon@gmail.com")
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Saimon")
driver.find_element(By.NAME, "email").send_keys("msasaimon@tulip-tech.com")
driver.find_element(By.XPATH, "//input[@type='submit']").click()
print(driver.find_element(By.CLASS_NAME, "alert-success").text)
message= driver.find_element(By.CSS_SELECTOR, "div[class*='alert-success']").text
time.sleep(2)
driver.close()
print('Done')
assert "success" in message