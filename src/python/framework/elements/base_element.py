from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.python.framework.config import Config


class BaseElement:
	def __init__(self, locator=None, element=None):
		self.locator = locator
		self.element = element

	def __call__(self, *args, **kwargs):
		if self.element is not None:
			return self.element
		else:
			self.element = WebDriverWait(Config().driver, Config().explicitly_wait).until(
				EC.element_to_be_clickable(self.locator), "Couldn't find element {}".format(self.__class__))
			return self.element
