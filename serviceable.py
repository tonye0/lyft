from abc import abstractmethod, ABC


class Serviceable(ABC):
    @abstractmethod
    def needs_service(self):
        pass
