import time
import datetime

class PositionTracker:
    def __init__(self, Zapper):
        self.last_positions = []
        self.Zapper = Zapper
        with open('glove_pos.txt', 'w') as f:
            f.write(f'Started recording at {datetime.time()}\n')


    def get_last_n_pos(self, n=20):
        n = min(n, len(self.last_positions))
        return self.last_positions[-n:]

  # main logic of the stimulation
  # was supposed to detect that the last 20 hand positions has contained starting position followed by open position
    def check_for_trigger(self, how_many_pos_check = 20):
        start_coef = 0.8
        if len(self.last_positions) < 10: # Calibration time of 1 second
            return False
        else:
            last20 = self.get_last_n_pos(how_many_pos_check)
            firstPart = last20[:int(len(last20)*0.75)] # first 3/4
            secondPart = last20[int(len(last20)*0.75):]
            if firstPart.count('start') > start_coef * len(firstPart) and 'open' in secondPart:
                return True
            else:
                return False

    def record(self, position):
        self.last_positions.append(position)
        with open('glove_pos.txt', 'a') as f:
            f.write(position + '\n')
        if self.check_for_trigger():
            self.Zapper.zap()

