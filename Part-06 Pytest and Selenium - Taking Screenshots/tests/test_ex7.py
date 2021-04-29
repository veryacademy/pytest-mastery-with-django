import os
import time

import pytest
from selenium import webdriver


def take_screenshot(driver, name):
    time.sleep(1)
    os.makedirs(os.path.join("screenshot", os.path.dirname(name)), exist_ok=True)
    driver.save_screenshot(os.path.join("screenshot", name))


# def test_example(live_server):
#     options = webdriver.ChromeOptions()
#     options.add_argument("--headless")
#     options.add_argument("--window-size=1920,1080")
#     chrome_driver = webdriver.Chrome("./chromedriver", options=options)
#     chrome_driver.get(("%s%s" % (live_server.url, "/admin/")))
#     take_screenshot(chrome_driver, "admin/admin.png")


@pytest.fixture(params=["chrome1920", "chrome411", "firefox"], scope="class")
def driver_init(request):
    if request.param == "chrome1920":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        web_driver = webdriver.Chrome(executable_path=r"./chromedriver", options=options)
        request.cls.browser = "Chrome1920x1080"
    if request.param == "chrome411":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--window-size=411,823")
        web_driver = webdriver.Chrome(executable_path=r"./chromedriver", options=options)
        request.cls.browser = "Chrome411x823"
    if request.param == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        web_driver = webdriver.Firefox(executable_path=r"./geckodriver", options=options)
        request.cls.browser = "Firefox"
    request.cls.driver = web_driver
    yield
    web_driver.close()


@pytest.mark.usefixtures("driver_init")
class Screenshot:
    def screenshot_admin(self, live_server):
        self.driver.get(("%s%s" % (live_server.url, "/admin/")))
        take_screenshot(self.driver, "admin/" + "admin" + self.browser + ".png")
        assert "Log in | Django site admin" in self.driver.title
