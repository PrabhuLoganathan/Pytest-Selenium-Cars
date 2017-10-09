from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.python.framework.config import Config
from src.python.framework.elements.base_element import BaseElement
from src.python.framework.elements.label import Label


class Container(BaseElement):
	def __init__(self, locator=None, element=None):
		super().__init__(locator=locator, element=element)
		self.my_elements = []

	def append_elements(self, locator, cls=Label):
		for e in self().find_elements(*locator):
			self.my_elements.append(cls(element=e))

	def find_one_element(self, locator):
		return WebDriverWait(Config().driver, Config().explicitly_wait).until(
			EC.element_to_be_clickable(self().find_element(locator)),
                "Couldn't find element in this container")

	def get_elements(self):
		return self.my_elements
