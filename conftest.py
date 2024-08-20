import logging
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from time import sleep
from playwright.sync_api import sync_playwright, Playwright
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(level=logging.DEBUG, filename='my_log.log',
                    format='%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d) [%(filename)s]',
                    datefmt='%d/%m/%Y %I:%M:%S', encoding='utf-8', filemode='w')

logger = logging.getLogger(__name__)
handler = logging.FileHandler('test.log', encoding='utf-8')
formatter = logging.Formatter('%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d) [%(filename)s]')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.info('Тестируем файл на данные')



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
    driver.implicitly_wait(60)
    driver.maximize_window()
    yield driver
    driver.quit()


