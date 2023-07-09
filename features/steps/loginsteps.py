import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


# @when('Enter username {usn:s} and {pwd:s}')
@when('Enter username {usn} and password {pwd}')
def enter_usernamePassword(context, usn, pwd):
    context.username = context.driver.find_element(By.NAME, 'username').send_keys(usn)
    context.password = context.driver.find_element(By.NAME, 'password').send_keys(pwd)


@when('Click on the login button')
def click_loginBtn(context):
    context.login_btn = context.driver.find_element(
        By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
    context.login_btn.click()
    time.sleep(5)


@then('User logins successfully')
def user_login(context):
    try:
        context.text = context.active_user = context.driver.find_element(By.XPATH,
                                                                         '/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/div[1]/div[1]').text
    except:
        context.driver.close()
        assert False, 'Test failed'
    if context.text == 'Dashboard':
        context.driver.close()
        assert True, 'Test passed'
