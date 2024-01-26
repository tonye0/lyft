import unittest
from components.tires.carrigan_tires import CarriganTire


class TestCarriganTire(unittest.TestCase):
    def test_needs_service_true(self):
        wear_sensors = [0.8, 0.95, 0.92, 0.88]
        tire = CarriganTire(wear_sensors)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        wear_sensors = [0.8, 0.65, 0.73, 0.88]
        tire = CarriganTire(wear_sensors)
        self.assertFalse(tire.needs_service())

if __name__ == '__main__':
    unittest.main()
