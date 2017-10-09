import random

from src.python.framework.elements.base_element import BaseElement


class Select(BaseElement):
	def __init__(self, locator=None, element=None):
		super().__init__(locator, element)
		self.current_option = None

	def select_option(self, option):
		items_list = self.get_options()
		for item in items_list:
			if item.get_attribute("label") == option:
				self.current_option = option
				item.click()
				break

	def get_options(self):
		return self().find_elements_by_tag_name('option')

	def select_random_option(self):
		while True:
			rand_val = random.choice(self.get_options()).get_attribute("label")
			if 'Select' not in rand_val:
				break
		self.select_option(rand_val)
