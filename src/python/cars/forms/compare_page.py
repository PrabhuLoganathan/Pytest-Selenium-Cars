import re

from selenium.webdriver.common.by import By

from src.python.cars.models.car import Car
from src.python.framework.base_page import BasePage
from src.python.framework.config import Config
from src.python.framework.elements.button import Button
from src.python.framework.elements.container import Container
from src.python.framework.elements.form import Form
from src.python.framework.elements.label import Label
from src.python.framework.elements.select import Select
from src.python.framework.elements.textfield import TextField


class ComparePage(BasePage):
	__page_locator = (By.XPATH, "//h1[contains(text(), 'Compare Cars Side-by-Side')]")
	__url = Config().config['cars']['url']['comparePage']

	_formCompareLocator = (By.ID, "mainAddCarForm")
	_selectsLocators = (By.TAG_NAME, "select")
	_btnFormCompareLocator = (By.XPATH, "//button[contains(@class, 'done-button')]")
	_btnFormModalLocator = (By.XPATH, "//button[contains(class, 'modal-button')]")

	_labelAddCarLocator = (By.ID, "icon-div")
	_formAddCarLocator = (By.ID, "addCarFormModal")

	_templateCompareLocators = "//cars-compare-compare-info[@header='{}']{}"
	_cntrCompareEngineLocator = (By.XPATH, _templateCompareLocators.format('Engine', ''))
	_cntrCompareTransmissionLocator = (By.XPATH, _templateCompareLocators.format('Transmission', ''))
	_lblCompareEngineLocator = (By.XPATH, "//cars-compare-compare-info[@header='Engine']//p")
	_lblCompareTransmissionLocator = (By.XPATH, "//cars-compare-compare-info[@header='Transmission']//p")

	def __init__(self, driver):
		super().__init__(self.__page_locator, self.__url, driver)
		self.formCompare = Form(self._formCompareLocator)  # первая форма сравнения форма сравнения (выбор машины)
		self.lblAddCar = Label(self._labelAddCarLocator)  # ссылка на окрытие формы добавления машины для сравнения
		self.formAddCar = Form(self._formAddCarLocator)  # вторая форма сравнения (добавление машины)
		self.cntrCompareEngine = Container(self._cntrCompareEngineLocator)  # контейнер
		self.cntrCompareTransmission = Container(self._cntrCompareTransmissionLocator)  # контейнер
		self.btnFormCompare = Button(self._btnFormCompareLocator)  # кнопка подтверждения первой формы
		self.btnFormModal = Button(self._btnFormModalLocator)  # кнопка подтвержения второй формы

	def select_first_car_to_compare(self):
		self.formCompare.append_elements(self._selectsLocators, cls=Select)
		self.formCompare.select_values(Car.remembered_cars[0].make, Car.remembered_cars[0].model,
			Car.remembered_cars[0].year)
		self.btnFormCompare().click()

	def select_second_car_to_compare(self):
		self.lblAddCar().click()
		self.formAddCar.append_elements(self._selectsLocators, cls=Select)
		self.formAddCar.select_values(Car.remembered_cars[1].make, Car.remembered_cars[1].model,
			Car.remembered_cars[1].year)
		self.btnFormModal().click()

	# поиск текстовых элементов, содержащих информация о машинах и добавление в соответствующие контейнеры
	def _found_compare_info(self):
		self.cntrCompareEngine.append_elements(self._lblCompareEngineLocator, TextField)
		self.cntrCompareTransmission.append_elements(self._lblCompareTransmissionLocator, TextField)

	def assert_cars_info(self):
		self._found_compare_info()
		Engines = [re.sub(r'liter', 'L', x().text) for x in self.cntrCompareEngine.get_elements()]
		Transmissions = [t().text for t in self.cntrCompareTransmission.get_elements()[1:]]
		# для избавления от лишних запятых, чтобы не падали assert'ы
		if Transmissions[0][-1] == ',':
			Transmissions[0] = Transmissions[0][:-1]

		assert Car.remembered_cars[0].engine in Engines
		assert Car.remembered_cars[1].engine in Engines
		assert Car.remembered_cars[0].transmission in Transmissions
		assert Car.remembered_cars[1].transmission in Transmissions
