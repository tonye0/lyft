from abc import ABC, abstractmethod


class Serviceable(ABC):
    @abstractmethod
    def needs_service(self):
        pass


class Car(Serviceable, ABC):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery


class Engine(Serviceable, ABC):
    pass


class Battery(Serviceable, ABC):
    pass


