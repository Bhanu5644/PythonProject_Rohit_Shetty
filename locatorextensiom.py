from selenium import webdriver

#chrome driver
from selenium.webdriver.chrome.service import Service

service_obj= Service("C:\Users\BHANU\Downloads\chromedriver_win32.exe")
driver = webdriver.Chrome(service=service_obj)