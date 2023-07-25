from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pickle

driver = webdriver.Edge(executable_path="E:\celery_test_server\edgedriver_win64\msedgedriver.exe")

driver.get("https://www.baidu.com/")

# search_input = driver.find_element_by_xpath('//*[@id="kw"]')
search_input = driver.find_element(By.XPATH, '//*[@id="kw"]')
search_input.send_keys('python')

# search_button = driver.find_element_by_xpath('//*[@id="su"]')
search_button = driver.find_element(By.XPATH, '//*[@id="su"]')
search_button.click()

# time.sleep(10)
# driver.quit()

