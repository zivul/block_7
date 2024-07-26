from selenium.webdriver.common.by import By
import allure
from conftest import *


@allure.feature('Оглавление')
@allure.story('История')
@allure.title('Собака')
class TestExemple():
    @pytest.mark.skip
    def test_find_element(self, set_up_browser):
        with allure.step('Открытие страницы'):
            driver = set_up_browser    #Название функции в fixture (склеиваем их)
            driver.get('https://apteka-altay.ru/')
        with allure.step('Клик'):
            driver.find_element(By.LINK_TEXT, 'Косметика').click()
