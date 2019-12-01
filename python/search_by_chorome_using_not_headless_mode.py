import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.google.com/')
print(driver.title)

search_box = driver.find_element_by_name("q")
search_box.send_keys('ChromeDriver')
search_box.submit()
print(driver.title)

driver.save_screenshot('search_results.png')
driver.quit()
