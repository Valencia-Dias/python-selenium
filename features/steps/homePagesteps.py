import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


@given('Launch the browser')
def launchBrowser(context):
    # for selenium 4 you have to use service and not executable path alone
    service = Service('/usr/bin/chromedriver')
    context.driver = webdriver.Chrome(service=service)
    context.driver.maximize_window()


@when('Open the homepage')
def openHomePage(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/')
    time.sleep(5)


@then('Verify the presence of the logo')
def verifyLogo(context):
    status = context.driver.find_element(By.CLASS_NAME, 'orangehrm-login-branding').is_displayed()
    assert status is True


@then('Close the browser')
def closeBrowser(context):
    context.driver.close()




