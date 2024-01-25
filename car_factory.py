from datetime import date

from components.batteries import spindler_battery, nubbin_battery
from components.engines import capulet_engine, willoughby_engine, sternman_engine
from components.models import calliope, thovex, palindrome, glissade, rorschach


class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        battery = spindler_battery.SpindlerBattery(last_service_date, current_date)
        engine = capulet_engine.CapuletEngine(last_service_mileage, current_mileage)

        return calliope.Calliope(engine, battery)

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        battery = spindler_battery.SpindlerBattery(last_service_date, current_date)
        engine = willoughby_engine.WilloughbyEngine(last_service_mileage, current_mileage)

        return glissade.Glissade(engine, battery)

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on):
        battery = spindler_battery.SpindlerBattery(last_service_date, current_date)
        engine = sternman_engine.SternmanEngine(warning_light_is_on)

        return palindrome.Palindrome(engine, battery)

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        battery = nubbin_battery.NubbinBattery(last_service_date, current_date)
        engine = willoughby_engine.WilloughbyEngine(last_service_mileage, current_mileage)

        return rorschach.Rorschach(engine, battery)

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        battery = nubbin_battery.NubbinBattery(last_service_date, current_date)
        engine = capulet_engine.CapuletEngine(last_service_mileage, current_mileage)

        return thovex.Thovex(engine, battery)


car_factory = CarFactory()

calliope_car = car_factory.create_calliope(date.today(), date(2021, 1, 1), 80000, 50000)
print(calliope_car.needs_service())
