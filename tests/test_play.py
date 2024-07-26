from conftest import *


class TestPlaywright:
    def test_github_1(self, browser):
        page = browser
        page.goto("https://github.com/microsoft/vscode/issues")
        page.get_by_label("Search or jump to…").click()
        page.get_by_role("combobox", name="Search").click()
        page.locator('#query-builder-test').clear()
        page.get_by_role("combobox", name="Search").fill("bug")
        page.wait_for_timeout(1000)
        page.get_by_role("combobox", name="Search").press("Enter")
        sleep(3)

    def test_github_2(self, browser):
        page = browser
        page.goto('https://github.com/microsoft/vscode/issues')
        page.get_by_role("button", name="Author").click()
        page.get_by_role("textbox", name="Filter users").fill("bpasero")
        page.wait_for_timeout(1000)
        page.get_by_role("menuitemradio", name="@bpasero bpasero Benjamin").click()
        page.wait_for_timeout(2000)

    def test_github_3(self, browser):
        page = browser
        page.goto('https://github.com/search/advanced')
        page.get_by_label("Written in this language").select_option("Python")
        page.get_by_placeholder("200, >1000").click()
        page.wait_for_timeout(1000)
        page.get_by_placeholder("200, >1000").fill("20000")
        page.get_by_placeholder("app.rb, footer.erb").click()
        page.wait_for_timeout(1000)
        page.get_by_placeholder("app.rb, footer.erb").fill("environment.yml")
        page.locator("#search_form div").filter(has_text="Advanced options From these").get_by_role("button").click()
        page.wait_for_timeout(1000)

    def test_skillbox(self, browser):
        page = browser
        page.goto('https://skillbox.ru/code/')
        page.locator("(//*[contains(text(), 'Профессия')])[3]").click()
        page.wait_for_timeout(1000)

        page.locator('(//button[@class="ui-range__dot"])[1]').hover()
        page.mouse.down()
        page.mouse.move(x=150, y=0)
        page.mouse.up()
        page.locator('(//button[@class="ui-range__dot"])[2]').hover()
        page.mouse.down()
        page.mouse.move(x=230, y=0)
        page.mouse.up()
        page.wait_for_timeout(1000)

        page.locator("(//*[contains(@class, 'ui-checkbox-field__value ui-checkbox-field__value--small')])[1]").click()
        page.wait_for_timeout(1000)

    def test_vscode(self, browser):
        page = browser
        page.goto('https://github.com/microsoft/vscode/graphs/commit-activity')
        page.wait_for_timeout(1000)
        page.locator("(//*[contains(@class, 'bar mini')])[18]").hover()
        page.wait_for_timeout(3000)











