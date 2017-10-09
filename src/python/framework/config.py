import json
import os


def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return get_instance


@singleton
class Config:
    driver = None
    _path_to_resources = "../../../resources/"

    def __init__(self):
        with open(os.path.abspath("{}config.json".format(self._path_to_resources)), "r") as conf:
            self.config = json.load(conf)

        self.explicitly_wait = self.config['main']['explicitlyWaitDelay']