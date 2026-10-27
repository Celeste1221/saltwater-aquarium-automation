"""Optical water level -> Adafruit IO. 
"""
import os
from time import sleep
from Adafruit_IO import Client, Data
from gpiozero import Button

# This script reads the water level from an optical sensor connected to GPIO pin 17 and sends the data to Adafruit IO. 
# The sensor returns 0 (indicating water is present) or 1 (indicating no water). 
# The data is sent at regular intervals defined by the READ_INTERVAL_SECONDS environment variable, defaulting to 3 seconds if not set.
def read_water_level(sensor):
    """Map optical sensor state to the original feed convention: 0=water, 1=no water."""
    return 0 if sensor.is_pressed else 1


def main():
    # Set up Adafruit IO client and GPIO sensor
    aio = Client(os.environ['ADAFRUIT_IO_USERNAME'], os.environ['ADAFRUIT_IO_KEY'])
    
    # Set up the optical water level sensor on GPIO pin 17 using the Button class from gpiozero, with a pull-up resistor configuration.
    sensor = Button(17, pull_up=True)
    interval = int(os.getenv('READ_INTERVAL_SECONDS', '3'))
    
    # Main loop to read water level and send data to Adafruit IO
    while True:
        # returns 0 when pressed and 1 otherwise.
        level = read_water_level(sensor)
        aio.create_data('water-level', Data(value=level))
        print('Water level signal:', level)
        sleep(interval)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
