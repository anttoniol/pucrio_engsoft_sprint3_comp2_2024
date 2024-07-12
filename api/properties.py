from configparser import ConfigParser, ExtendedInterpolation
import os

PATH = os.path.dirname(os.path.abspath(__file__))
PARENT_PATH = os.path.dirname(PATH)

class Properties:
    def __init__(self):
        self.__config = ConfigParser(interpolation=ExtendedInterpolation())
        self.__config.read(PARENT_PATH + "/properties.ini")

    def get_value(self, section, key):
        try:
            return self.__config.get(section, key)
        except Exception as ex:
            print("Either section or key not found!")
            return None
