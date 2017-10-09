import pytest

from src.python.framework.browser import Browser
from src.python.framework.config import Config


@pytest.fixture(scope="module")
def setup_class(request):
	browser = Browser(Config().config['main']['browserName'])
	Config().driver = browser.driver

	def teardown_class():
		browser.driver.quit()

	request.addfinalizer(teardown_class)
