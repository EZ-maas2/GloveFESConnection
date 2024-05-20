# This should be replaced with FES functionality once the classifier is actually working
from FES_classes.FES import FES
from FES_classes.Stimulation_Mid_Lvl import Stimulation_Mid_Lvl

import time
class Zapper():
    recovery_time_s = 60
    port = 'COM3'
    #fes_device = FES(port)



    def __init__(self):
        self.last_zap_time = None
        self.stimulation = Stimulation_Mid_Lvl(amplitude_mA = 15, pulse_width_micros = 100, period_ms = 20, channel = 'black')
        self.duration_s = 1

    def zap(self):
        if self.last_zap_time != None and (time.perf_counter() - self.last_zap_time) < self.recovery_time_s:
            print(f'elapsed time since last zap {time.perf_counter() - self.last_zap_time}, {self.last_zap_time=}, {time.perf_counter()}')
            print("Too early to zap!")
        else:
            print('Zapped----------------------------------------')
            #self.fes_device.mid_lvl_stimulate(self.stimulation, self.duration_s)
            self.last_zap_time = time.perf_counter()
            print(self.last_zap_time)

