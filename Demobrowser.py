from selenium import webdriver

# Chrome driver
from selenium.webdriver.chrome.service import Service

---------Chrome---
service_obj = Service("C:\Users\BHANU\Downloads\chromedriver_win32.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("http://rahulshettyacademy.com")

service_obj = Service("C:\Users\BHANU\Downloads\chromedriver_win32.exe")
driver = webdriver.firefox(service=service_obj)
driver.get("http://rahulshettyacademy.com")

