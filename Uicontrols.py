from selenium import webdriver


driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome('C:\\chromedriver.exe')
driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
