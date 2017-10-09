from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.python.framework.config import Config


class BasePage:
    def __init__(self, locator, url, driver):
        self._page_locator = locator
        self.driver = driver
        self.url = url

    def go(self):
        self.driver.get(self.url)
        self._assert_page_load()

    def _assert_page_load(self):
        WebDriverWait(self.driver, Config().explicitly_wait).until(
            EC.presence_of_element_located(self._page_locator), "Couldn't load page {}".format(self.url))

    def scroll_window_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0);")

    def refresh(self):
        self.driver.refresh()
