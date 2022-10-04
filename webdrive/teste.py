from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
driver.get('https://www.google.com')
driver.maximize_window()
driver.refresh()