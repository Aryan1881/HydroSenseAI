import random

class SensorSimulator:
    def __init__(self, pressure_threshold=75):
        self.pressure_threshold = pressure_threshold

    def read_sensor(self):
        # Simulate random pressure reading
        pressure_value = random.uniform(0, 100)
        return pressure_value

    def is_pressure_high(self):
        return self.read_sensor() > self.pressure_threshold