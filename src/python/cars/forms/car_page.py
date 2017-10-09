from selenium.webdriver.common.by import By

from src.python.framework.base_page import BasePage
from src.python.framework.config import Config
from src.python.framework.elements.label import Label


class CarPage(BasePage):
	__page_locator = (By.XPATH, "//nav[contsins(class, 'mmy-jumpnav')]")
	__url = Config().config['cars']['url']['carPage']

	_label_trim_locator = (By.XPATH, "//div[@id='mmy-trims']//a")

	def __init__(self, driver):
		super().__init__(self.__page_locator, self.__url, driver)
		self.lblTrims = Label(self._label_trim_locator)

	def go_to_trim_comparison(self):
		self.lblTrims().click()
