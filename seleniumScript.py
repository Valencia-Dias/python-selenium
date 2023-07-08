from selenium import webdriver
#to suppress the DeprecationWarning
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
# browser instance
# driver = webdriver.Firefox()
driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
driver.get('http://demostore.supersqa.com/')
