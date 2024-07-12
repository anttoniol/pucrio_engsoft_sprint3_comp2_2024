import MySQLdb

from api.properties import Properties

class Repository:
    __properties = Properties()

    def __init__(self):
        user = self.__properties.get_value("mysql", "user")
        password = self.__properties.get_value("mysql", "password")

        self._db = MySQLdb.connect(host="db", user=user, password=password, database="events_storage")

