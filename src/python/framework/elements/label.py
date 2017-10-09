from src.python.framework.elements.base_element import BaseElement


class Label(BaseElement):
    def get_href(self):
        return self().get_property('href')
