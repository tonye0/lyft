from components.tires.tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, wear_sensors: list):
        self.wear_sensors = wear_sensors

    def needs_service(self):
        tire_should_be_serviced = sum(self.wear_sensors) >= 3
        return tire_should_be_serviced

