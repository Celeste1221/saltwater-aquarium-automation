"""Hardware-free unit tests of parser logic using stub sensor readings."""
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src' / 'raspberry_pi'))
from temperature_sensor import TemperatureSensor

# Unit tests for the TemperatureSensor class
class SensorTest(unittest.TestCase):
    def setUp(self):
        self.sensor = TemperatureSensor.__new__(TemperatureSensor)

    def test_celsius(self):
        self.sensor.read_temp_raw = lambda: ['aa YES\n', 'aa t=25437\n']
        self.assertEqual(self.sensor.read_temp_C(), 25.4)

    def test_fahrenheit(self):
        self.sensor.read_temp_raw = lambda: ['aa YES\n', 'aa t=25000\n']
        self.assertEqual(self.sensor.read_temp_F(), 77.0)

    def test_crc_failure(self):
        self.sensor.read_temp_raw = lambda: ['aa NO\n', 'aa t=25000\n']
        self.assertIsNone(self.sensor.read_temp_C())

if __name__ == '__main__':
    unittest.main()
