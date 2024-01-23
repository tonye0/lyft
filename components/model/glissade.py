from car import Car


class Glissade(Car):
    def __init__(self, engine, battery):
        super().__init__(engine, battery)

    def needs_service(self):
        if self.engine.needs_service() or self.battery.needs_service():
            return "Needs Servicing"
        return "Does not need servicing"
