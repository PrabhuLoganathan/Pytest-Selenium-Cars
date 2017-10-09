import sys

from selenium import webdriver

from src.python.framework.config import Config


def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return get_instance


# Class for working with browser
@singleton
class Browser:
    def __init__(self, brwsr_name):
        if brwsr_name == 'Firefox':
            if sys.platform == 'linux':
                self.driver = webdriver.Firefox(
                    executable_path=Config().config['main']['pathToDriver']['geckoLinux'])
            elif sys.platform == 'win64':
                self.driver = webdriver.Firefox(
                    executable_path=Config().config['main']['pathToDriver']['geckoWin64'])
            elif sys.platform == 'win32':
                self.driver = webdriver.Firefox(
                    executable_path=Config().config['main']['pathToDriver']['geckoWin32'])
        elif brwsr_name == 'Chrome':
            if sys.platform == 'linux':
                self.driver = webdriver.Chrome(
                    executable_path=Config().config['main']['pathToDriver']['chromeLinux'])
            elif sys.platform == 'win32':
                self.driver = webdriver.Chrome(
                    executable_path=Config().config['main']['pathToDriver']['chromeWin32'])
        else:
            raise NameError('Not support this browser or wrong name. Please try another browser.')
