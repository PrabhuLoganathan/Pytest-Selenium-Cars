class Car:
	remembered_cars = []

	def __init__(self, val):
		self.make = val[0]
		self.model = val[1]
		self.year = val[2]
		self.engine = None
		self.transmission = None
		self.remembered_cars.append(self)
