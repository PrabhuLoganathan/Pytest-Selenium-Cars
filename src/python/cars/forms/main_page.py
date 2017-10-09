from selenium.webdriver.common.by import By

from src.python.cars.models.car import Car
from src.python.framework.base_page import BasePage
from src.python.framework.config import Config
from src.python.framework.elements.form import Form
from src.python.framework.elements.select import Select
from src.python.framework.elements.tab import Tab


class MainPage(BasePage):
	# Page locator and url
	__page_locator = (By.XPATH, "//div[@class='page-body']")
	__url = Config().config['cars']['url']['mainPage']

	# Page elements' locators
	_tabLocator = (By.XPATH, "//cui-tabs[@id='superwidget']//li[@tab-for='research']")
	_formSearchCarLocator = (By.TAG_NAME, "form")
	_selectsLocator = (By.TAG_NAME, "select")
	_btnLocator = ()

	def __init__(self, driver):
		super().__init__(self.__page_locator, self.__url, driver)
		self.tabSearchCar = Tab(self._tabLocator)
		self.formSearchCar = Form(self._formSearchCarLocator)

	def click_tab(self):
		self.tabSearchCar().click()

	def select_car_options(self):
		self.formSearchCar.append_elements(self._selectsLocator, cls=Select)
		self.formSearchCar.choose_random_value()
		Car(self.formSearchCar.get_values())
		self.formSearchCar().submit()
