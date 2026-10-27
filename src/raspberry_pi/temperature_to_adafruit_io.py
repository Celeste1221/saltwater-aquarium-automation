"""DS18B20 -> Adafruit IO REST feed.
"""
import os
from time import sleep
from Adafruit_IO import Client, Data
from temperature_sensor import TemperatureSensor

# Main function to read temperature and send to Adafruit IO
def main():
    # Get Adafruit IO credentials from environment variables
    username = os.environ['ADAFRUIT_IO_USERNAME']
    key = os.environ['ADAFRUIT_IO_KEY']
    
    # Create an Adafruit IO client instance
    aio = Client(username, key)
    
    # Create a temperature sensor instance and read temperature at specified intervals
    sensor = TemperatureSensor()
    interval = int(os.getenv('READ_INTERVAL_SECONDS', '3'))
    
    # Continuously read temperature and send to Adafruit IO
    while True:
        value = sensor.read_temp_F()
        if value is not None:
            aio.create_data('temperature', Data(value=value))
            print('Temperature (F):', value)
        sleep(interval)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
