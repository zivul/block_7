import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from time import sleep
from playwright.sync_api import sync_playwright, Playwright


@pytest.fixture(scope='class')
def browser(playwright: Playwright):
    chromium = playwright.chromium
    browser = chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()
    page.set_viewport_size({'height': 1080, 'width': 1920})
    yield page
    page.close()
    browser.close()



@pytest.fixture()
def set_up_browser():
    options = ChromeOptions()
    driver = webdriver.Chrome(options=options)
    yield driver
    sleep(5)
    driver.quit()

