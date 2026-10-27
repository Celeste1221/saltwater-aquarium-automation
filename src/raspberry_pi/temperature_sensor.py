import glob
from time import sleep

# TemperatureSensor class to read temperature from DS18B20 sensor
# read temp in Celsius and Fahrenheit code modified from: https://gist.github.com/elktros/03f874be7960e4a766d36c0679cbf7d2? 
class TemperatureSensor:
    def __init__(self, check_sensor_frequency=3600):
        self.check_sensor_frequency = check_sensor_frequency
        self.device_file = self.find_DS18B20_temp_sensor()
        
    # Find the DS18B20 temperature sensor device file
    def find_DS18B20_temp_sensor(self):
        base_dir = '/sys/bus/w1/devices/'
        device_folders = glob.glob(base_dir + '28*')
        if not device_folders:
            raise RuntimeError('No DS18B20 sensor found! Is 1-Wire enabled and wired correctly?')
        return device_folders[0] + '/w1_temperature'
    
    # Read raw temperature data from the sensor
    def read_temp_raw(self):
        with open(self.device_file, 'r') as f:
            return f.readlines()
        
    # Read temperature in Celsius
    def read_temp_C(self):
        lines = self.read_temp_raw()
        retry = 0
        while lines[0].strip()[-3:] != 'YES' and retry < 5:
            sleep(0.2)
            lines = self.read_temp_raw()
            retry += 1
        if lines[0].strip()[-3:] != 'YES':
            return None
        equals_pos = lines[1].find('t=')
        if equals_pos == -1:
            return None
        return round(float(lines[1][equals_pos + 2:]) / 1000.0, 1)
    
    # Read temperature in Fahrenheit
    def read_temp_F(self):
        temp_C = self.read_temp_C()
        if temp_C is None:
            return None
        return round(temp_C * 9.0 / 5.0 + 32.0, 1)
