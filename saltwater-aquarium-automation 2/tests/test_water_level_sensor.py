"""Hardware-free tests for optical water-level signal mapping."""
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src' / 'raspberry_pi'))

# gpiozero/Adafruit_IO are Raspberry Pi dependencies. Stub them for tests so importing the module doesn't require a Raspberry Pi or real credentials.
from types import ModuleType

# Create fake modules to satisfy imports in water_level_to_adafruit_io.py
fake_adafruit = ModuleType('Adafruit_IO')
fake_adafruit.Client = object
fake_adafruit.Data = object
fake_gpiozero = ModuleType('gpiozero')
fake_gpiozero.Button = object

# Patch sys.modules to use the fake modules during import of the module under test
with patch.dict(sys.modules, {'Adafruit_IO': fake_adafruit, 'gpiozero': fake_gpiozero}):
    from water_level_to_adafruit_io import read_water_level

# Define a fake optical sensor class to simulate the behavior of the real sensor in tests
class FakeOpticalSensor:
    def __init__(self, is_pressed):
        self.is_pressed = is_pressed

# Define the test case class for the water level sensor
class WaterLevelSensorTest(unittest.TestCase):
    def test_pressed_reports_zero(self):
        self.assertEqual(read_water_level(FakeOpticalSensor(True)), 0)

    def test_not_pressed_reports_one(self):
        self.assertEqual(read_water_level(FakeOpticalSensor(False)), 1)

    def test_sensor_read_failure_propagates(self):
        class FaultySensor:
            @property
            def is_pressed(self):
                raise OSError('sensor disconnected')

        with self.assertRaises(OSError):
            read_water_level(FaultySensor())


if __name__ == '__main__':
    unittest.main()
