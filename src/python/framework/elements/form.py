from src.python.framework.elements.container import Container


class Form(Container):
	def select_value(self, value):
		self.my_elements[0].select_option(value)

	def select_values(self, *values):
		for el, val in zip(self.my_elements, values):
			el.select_option(val)

	def get_values(self):
		values = []
		for el in self.my_elements:
			values.append(el.current_option)
		print(values)
		return values

	def choose_random_value(self):
		for el in self.my_elements:
			el.select_random_option()

	def submit_form(self):
		self().submit()
