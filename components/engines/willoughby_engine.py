from car import Engine


class WilloughbyEngine(Engine):
    def __init__(self, last_service_mileage, current_mileage):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self):
        engine_should_be_serviced = self.current_mileage - self.last_service_mileage
        if engine_should_be_serviced > 60000:
            return True
        return False
