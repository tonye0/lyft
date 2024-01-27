from datetime import date

from components.batteries import spindler_battery, nubbin_battery
from components.engines import capulet_engine, willoughby_engine, sternman_engine
from components.tires import octoprime_tires, carrigan_tires
from car import Car
from utils import wear_sensors


class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, wear_sensors):
        battery = spindler_battery.SpindlerBattery(current_date, last_service_date)
        engine = capulet_engine.CapuletEngine(current_mileage, last_service_mileage)
        tire = carrigan_tires.CarriganTire(wear_sensors)

        return Car(engine, battery, tire)

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        battery = spindler_battery.SpindlerBattery(last_service_date, current_date)
        engine = willoughby_engine.WilloughbyEngine(last_service_mileage, current_mileage)
        tire = carrigan_tires.CarriganTire(wear_sensors)

        return Car(engine, battery, tire)

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on):
        battery = spindler_battery.SpindlerBattery(last_service_date, current_date)
        engine = sternman_engine.SternmanEngine(warning_light_is_on)
        tire = carrigan_tires.CarriganTire(wear_sensors)

        return Car(engine, battery, tire)

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        battery = nubbin_battery.NubbinBattery(last_service_date, current_date)
        engine = willoughby_engine.WilloughbyEngine(last_service_mileage, current_mileage)
        tire = carrigan_tires.CarriganTire(wear_sensors)

        return Car(engine, battery, tire)

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        battery = nubbin_battery.NubbinBattery(last_service_date, current_date)
        engine = capulet_engine.CapuletEngine(last_service_mileage, current_mileage)
        tire = octoprime_tires.OctoprimeTire(wear_sensors)

        return Car(engine, battery, tire)


if __name__ == "__main__":
    car_factory = CarFactory()

    calliope_car = car_factory.create_calliope(date.today(), date(2021, 1, 1), 80000, 50000, wear_sensors())
    print(calliope_car.needs_service())
