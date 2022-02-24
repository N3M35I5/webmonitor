from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# Will be depricated in selenium 4
# Post Url : https://stackoverflow.com/questions/64717302/deprecationwarning-executable-path-has-been-deprecated-selenium-python
#PATH = "E:\git_repo\selenium\chromedriver.exe"
#driver = webdriver.Chrome(PATH)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.google.co.in/')
