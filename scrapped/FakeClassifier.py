# the purpose of the this classifier is to emulate data readings
# so i can make other classes that would keep track of the last n positions and initiate the zap when necessary
# it must run in it's own thread

import random
import time

class FakeClassifier():
    possible_readings = ['open', 'start', 'closed', 'none']
    possible_readings_weights = [0.25, 0.75, 0.0, 0.0]

    def __init__(self, freq, PositionTracker):
        self.freq = freq
        self.PositionTracker = PositionTracker


    def random_reading(self):
        return random.choices(self.possible_readings, self.possible_readings_weights, k=1)[0]


    def start_recording(self):
        while True:
            new_reading = self.random_reading()
            self.PositionTracker.record(new_reading)
            time.sleep(1 / self.freq)