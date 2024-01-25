import unittest
from datetime import datetime

from components.models.calliope import Calliope
from components.models.glissade import Glissade
from components.models.palindrome import Palindrome
from components.models.rorschach import Rorschach
from components.models.thovex import Thovex

from components.engines import capulet_engine, willoughby_engine, sternman_engine
from components.batteries import spindler_battery, nubbin_battery


class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        engine = capulet_engine.CapuletEngine(last_service_mileage, current_mileage)
        battery = spindler_battery.SpindlerBattery(last_service_date, today)

        car = Calliope(engine, battery)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        engine = capulet_engine.CapuletEngine(last_service_mileage, current_mileage)
        battery = spindler_battery.SpindlerBattery(last_service_date, today)

        car = Calliope(engine, battery)
        self.assertTrue(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        engine = capulet_engine.CapuletEngine(last_service_mileage, current_mileage)
        battery = spindler_battery.SpindlerBattery(last_service_date, last_service_date)

        car = Calliope(engine, battery)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        engine = capulet_engine.CapuletEngine(last_service_mileage, current_mileage)
        battery = spindler_battery.SpindlerBattery(last_service_date, last_service_date)

        car = Calliope(engine, battery)
        self.assertTrue(car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        engine = willoughby_engine.WilloughbyEngine(last_service_mileage, current_mileage)
        battery = spindler_battery.SpindlerBattery(last_service_date, today)

        car = Glissade(engine, battery)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        engine = willoughby_engine.WilloughbyEngine(last_service_mileage, current_mileage)
        battery = spindler_battery.SpindlerBattery(last_service_date, today)

        car = Glissade(engine, battery)
        self.assertTrue(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        engine = willoughby_engine.WilloughbyEngine(last_service_mileage, current_mileage)
        battery = spindler_battery.SpindlerBattery(last_service_date, last_service_date)

        car = Glissade(engine, battery)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        engine = willoughby_engine.WilloughbyEngine(last_service_mileage, current_mileage)
        battery = spindler_battery.SpindlerBattery(last_service_date, last_service_date)

        car = Glissade(engine, battery)
        self.assertTrue(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False
        engine = sternman_engine.SternmanEngine(warning_light_is_on)
        battery = spindler_battery.SpindlerBattery(last_service_date, today)

        car = Palindrome(engine, battery)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        warning_light_is_on = False
        engine = sternman_engine.SternmanEngine(warning_light_is_on)
        battery = spindler_battery.SpindlerBattery(last_service_date, today)

        car = Palindrome(engine, battery)
        self.assertTrue(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True
        engine = sternman_engine.SternmanEngine(warning_light_is_on)
        battery = spindler_battery.SpindlerBattery(last_service_date, last_service_date)

        car = Palindrome(engine, battery)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        engine = sternman_engine.SternmanEngine(warning_light_is_on)
        battery = spindler_battery.SpindlerBattery(last_service_date, last_service_date)

        car = Palindrome(engine, battery)
        self.assertTrue(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        engine = willoughby_engine.WilloughbyEngine(last_service_mileage, current_mileage)
        battery = nubbin_battery.NubbinBattery(last_service_date, today)

        car = Rorschach(engine, battery)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        engine = willoughby_engine.WilloughbyEngine(last_service_mileage, current_mileage)
        battery = nubbin_battery.NubbinBattery(last_service_date, today)

        car = Rorschach(engine, battery)
        self.assertTrue(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        engine = willoughby_engine.WilloughbyEngine(last_service_mileage, current_mileage)
        battery = nubbin_battery.NubbinBattery(last_service_date, last_service_date)

        car = Rorschach(engine, battery)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        engine = willoughby_engine.WilloughbyEngine(last_service_mileage, current_mileage)
        battery = nubbin_battery.NubbinBattery(last_service_date, last_service_date)

        car = Rorschach(engine, battery)
        self.assertTrue(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        engine = capulet_engine.CapuletEngine(last_service_mileage, current_mileage)
        battery = nubbin_battery.NubbinBattery(last_service_date, today)

        car = Thovex(engine, battery)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        engine = capulet_engine.CapuletEngine(last_service_mileage, current_mileage)
        battery = nubbin_battery.NubbinBattery(last_service_date, today)

        car = Thovex(engine, battery)
        self.assertTrue(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        engine = capulet_engine.CapuletEngine(last_service_mileage, current_mileage)
        battery = nubbin_battery.NubbinBattery(last_service_date, last_service_date)

        car = Thovex(engine, battery)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        engine = capulet_engine.CapuletEngine(last_service_mileage, current_mileage)
        battery = nubbin_battery.NubbinBattery(last_service_date, last_service_date)

        car = Thovex(engine, battery)
        self.assertTrue(car.needs_service())


if __name__ == '__main__':
    unittest.main()
