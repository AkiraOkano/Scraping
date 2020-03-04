import time
from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)  # 今は chrome_options= ではなく options=

driver.get('https://www.google.com/')
print(driver.title)

search_box = driver.find_element_by_name("q")
search_box.send_keys('ChromeDriver')
search_box.submit()
print(driver.title)

driver.save_screenshot('search_results.png')

for g_h3 in driver.find_elements_by_css_selector(".g h3"):
    print(g_h3.text)

stats = driver.find_elements(by=By.ID, value="resultStats")[0].text
stats = driver.find_elements_by_id("resultStats")[0].text

print(stats)

for i, g in enumerate(driver.find_elements(By.CLASS_NAME, "g")):
    print("------ " + str(i+1) + " ------")
    r = g.find_element(By.CLASS_NAME, "r")
    print(r.find_element(By.TAG_NAME, "h3").text)
    print("\t" + r.find_element(By.TAG_NAME, "a").get_attribute("href"))
    s = g.find_element(By.CLASS_NAME, "s")
    print("\t" + s.find_element(By.CLASS_NAME, "st").text)

for a in driver.find_elements_by_xpath("//a[contains(text(), '訳す')]"):
    print(a.get_attribute("href"))
driver.quit()