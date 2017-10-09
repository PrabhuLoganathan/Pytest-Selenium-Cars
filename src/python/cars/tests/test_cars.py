import pytest

from src.python.cars.forms.car_page import CarPage
from src.python.cars.forms.compare_page import ComparePage
from src.python.cars.forms.main_page import MainPage
from src.python.cars.forms.research_page import ResearchPage
from src.python.cars.forms.trim_page import TrimPage
from src.python.framework.config import Config
from src.python.framework.fixtures import setup_class


@pytest.mark.usefixtures('setup_class')
class TestCars:
	def test_cars(self):
		self._search_car()
		self._search_car()

		trim_page = TrimPage(Config().driver)
		trim_page.go_to_research()
		research_page = ResearchPage(Config().driver)
		research_page.go_to_compare()
		compare_page = ComparePage(Config().driver)
		compare_page.select_first_car_to_compare()
		compare_page.select_second_car_to_compare()
		compare_page.assert_cars_info()

	@staticmethod
	def _search_car():
		main_page = MainPage(Config().driver)
		main_page.go()
		main_page.click_tab()
		main_page.select_car_options()
		car_page = CarPage(Config().driver)
		car_page.go_to_trim_comparison()
		trim_page = TrimPage(Config().driver)
		trim_page.remember_car_info()
