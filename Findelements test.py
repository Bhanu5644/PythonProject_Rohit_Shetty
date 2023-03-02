from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:\Users\BHANU\Downloads\chromedriver_win32.exe")
driver = webdriver.Chrome(service=service_obj)