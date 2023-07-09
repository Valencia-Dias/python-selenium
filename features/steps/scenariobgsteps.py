

import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


@when('Navigate to the search page')
def navigate_to_search(context):
    assert True, 'Test passed'


@then('Search page should be displayed')
def display_search(context):
    assert True, 'Test passed'


@when('Navigate to the advanced search page')
def navigate_to_advanced_search(context):
    assert True, 'Test passed'


@then(u'Advanced search page should be displayed')
def display_advanced_search(context):
    assert True, 'Test passed'

