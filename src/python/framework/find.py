from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.python.framework.config import Config


class Find(object):
	by = None
	locator = None
	ui_type = None
	context = None
	_target_element = None

	def __init__(self, ui_type=WebElement, by=By.XPATH, locator=None, context=None, *args, **kwargs):
		self.by = by
		self.locator = locator
		self.ui_type = ui_type
		self.context = context
		self._target_element = None
		self._validate_params()

	def _validate_params(self):
		if self.by and not self.locator:
			raise ValueError('Provide search value in addition to by')
		if not self.by:
			if issubclass(self.ui_type, WebElement):
				raise TypeError('Logical containers shouldn\'t be WebElement')
		else:
			if not issubclass(self.ui_type, WebElement):
				raise TypeError('UI types should inherit WebElement')

	def __get__(self, obj, *args):
		self.context = obj
		self._search_element()
		return self._target_element

	def __getattribute__(self, item):
		if hasattr(Find, item):
			return object.__getattribute__(self, item)
		self._search_element()
		return self._target_element.__getattribute__(item)

	def __getitem__(self, key):
		self._search_element()
		return self._target_element.__getitem__(key)

	def _search_element(self):
		if not self.context:
			raise ValueError(
				"Search context should be defined with dynamic Find usage." + " Please define context in __init__.")
		if (self.by is not None) and (self.locator is not None):
			web_element = WebDriverWait(self.context.driver, Config().explicitly_wait).until(
				EC.presence_of_element_located((self.by, self.locator)),
				"Couldn't find element through {}".format(self.locator))
			web_element.__class__ = self.ui_type
			web_element.driver = self.context.driver
			self._target_element = web_element


class Finds(Find):
	def _validate_params(self):
		if not self.locator:
			raise ValueError('Provide value to search elements')
		if not issubclass(self.ui_type, WebElement):
			raise TypeError('Finds is applicable only for WebElements')

	def _search_element(self):
		self._target_element = WebDriverWait(self.context.driver, Config().explicitly_wait).until(
			EC.visibility_of_all_elements_located((self.by, self.locator)))
		for item in self._target_element:
			item.__class__ = self.ui_type
