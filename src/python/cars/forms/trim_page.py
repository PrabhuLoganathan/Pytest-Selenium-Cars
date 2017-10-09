from selenium.webdriver.common.by import By

from src.python.cars.models.car import Car
from src.python.framework.base_page import BasePage
from src.python.framework.config import Config
from src.python.framework.elements.label import Label
from src.python.framework.elements.textfield import TextField


class TrimPage(BasePage):
	__page_locator = ()
	__url = Config().config['cars']['url']['trimPage']

	_trim_engine_locator = (By.XPATH, "//div[@class='cell cell-bg grow-2']")
	_trim_transmission_locator = (By.XPATH, "//div[@class='cell grow-2']")

	_buy_label_locator = (By.XPATH, "//div[@class='global-nav']//a[@menu-name='Buy']")
	_research_label_locator = (By.XPATH, "//div[@id='user-setting']//li/a[contains(text(), 'Research Car Models')]")

	def __init__(self, driver):
		super().__init__(self.__page_locator, self.__url, driver)
		self.txtCarEngine = TextField(self._trim_engine_locator)
		self.txtCarTransmission = TextField(self._trim_transmission_locator)
		self.lblBuy = Label(self._buy_label_locator)
		self.lblResearch = Label(self._research_label_locator)

	def remember_car_info(self):
		Car.remembered_cars[-1].engine = self.txtCarEngine().text
		Car.remembered_cars[-1].transmission = self.txtCarTransmission().text

	def go_to_research(self):
		self.lblBuy().click()
		self.lblResearch().click()
