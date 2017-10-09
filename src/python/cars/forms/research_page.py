from selenium.webdriver.common.by import By

from src.python.framework.base_page import BasePage
from src.python.framework.elements.label import Label


class ResearchPage(BasePage):
	__page_locator = ()
	__url = ""

	_lbl_compare_locator = (
		By.XPATH, "//div[@id='ta-linkcards-container']//h4[contains(text(), 'Side-by-side')]/parent::a")

	def __init__(self, driver):
		super().__init__(self.__page_locator, self.__url, driver)
		self.lblCompare = Label(self._lbl_compare_locator)

	def go_to_compare(self):
		self.lblCompare().click()
