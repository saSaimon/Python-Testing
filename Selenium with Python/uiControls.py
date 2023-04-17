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

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes=driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value")=="option2":
        checkbox.click()
        assert checkbox.is_selected()
        
radiobuttons= driver.find_elements(By.CSS_SELECTOR, "input[name='radioButton']")

radiobuttons[1].click()
assert radiobuttons[1].is_selected()

#the is displayed interects with html and what is shown on the page but if the element is not on the page then it will return false
assert driver.find_element(By.ID, "displayed-text").is_displayed()

driver.find_element(By.ID,"hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()
driver.close()