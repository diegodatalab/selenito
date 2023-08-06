
# * [dom]:   document.documentElement.innerText

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com")

text_on_page = str(driver.execute_script("return document.documentElement.innerText"))

print(text_on_page)