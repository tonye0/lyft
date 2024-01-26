from components.tires.tire import Tire


class CarriganTire(Tire):
    def __init__(self, wear_sensors: list):
        self.wear_sensors = wear_sensors

    def needs_service(self):
        tire_should_be_serviced = any(wear >= 0.9 for wear in self.wear_sensors)
        return tire_should_be_serviced
