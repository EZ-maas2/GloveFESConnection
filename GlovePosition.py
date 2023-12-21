# For example, we could be tracking glove position with frequency 10/sec = 10Hz
# if we cache last 100 positions of the glove and it was in the starting position with probability above 75% for
# all of these 30 positions (3 second), than we say that the stimulation has to be delivered for 1 sec


class Hand:

    def __init__(self, sensor_readout):
        self.update_hand(sensor_readout)

    def update_hand(self, sensor_readout):
        self.thumb = Finger(distal=sensor_readout[0], proximal=sensor_readout[1])
        self.pointer = Finger(distal=sensor_readout[2], proximal=sensor_readout[3])
        self.middle = Finger(distal=sensor_readout[4], proximal=sensor_readout[5])
        self.ring = Finger(distal=sensor_readout[6], proximal=sensor_readout[7])
        self.pinky = Finger(distal=sensor_readout[8], proximal=sensor_readout[9])


    def isStartingPosition(self):
        if self.thumb.straight and not(self.pointer.straight or self.ring.straight or self.middle.straight or self.pinky.straight):
            return True
        else:
            return False

    def isOpenPalm(self):
        if self.thumb.straight and self.pointer.straight and self.ring.straight and self.middle.straight and self.pinky.straight:
            return True
        else:
            return False


class Finger:
    def __init__(self, distal, proximal):
        self.distal = distal
        self.proximal = proximal
        self.set_straight()

    def set_straight(self):
        if self.distal> 150  and self.proximal > 150:
            self.straight = True
        else: self.straight = False