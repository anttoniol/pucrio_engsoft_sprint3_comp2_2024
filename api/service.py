from api.repositories.event_repository import EventRepository
from api.properties import Properties

properties = Properties()
event_repository = EventRepository()


def save(data):
    return event_repository.save(data)


def get_by_id(id):
    return event_repository.get_by_id(id)


def get_by_coordinates(lat, lon):
    return event_repository.get_by_coordinates(lat, lon)


def update(id, data):
    return event_repository.update(id, data)


def delete(id):
    return event_repository.delete(id)



