import unittest
from components.tires.octoprime_tires import OctoprimeTire


class TestOctoprimeTire(unittest.TestCase):
    def test_needs_service_true(self):
        wear_sensors = [0.8, 0.95, 0.92, 0.88]
        tire = OctoprimeTire(wear_sensors)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        wear_sensors = [0.87, 0.5, 0.13, 0.2]
        tire = OctoprimeTire(wear_sensors)
        self.assertFalse(tire.needs_service())


if __name__ == '__main__':
    unittest.main()
