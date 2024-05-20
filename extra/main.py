from GlovePosition import Hand
from PositionTracker import PositionTracker
import time
import sys


def get_new_readout():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


if __name__ == '__main__':
    # every 1/10 sec we get new sensor readout
    # we update the hand object with the new sensor readout
    # hand then appends the 'starting position' 'openpalm' or False to the list
    # class position tracker notifies it's subscriber if there is a pattern
    # stimulation module receives the notification and delivers the stimulation
    pos_tracker = PositionTracker()
    sensors_initial = get_new_readout()
    hand_tracker = Hand(sensors_initial)
    freq_update = 10

    while True:
        sensors_data = get_new_readout()
        hand_tracker.update_hand(sensors_data)
        trigger = pos_tracker.check_for_trigger()
        if trigger:
            print('Stimulate!!')
        time.sleep(1/freq_update)

