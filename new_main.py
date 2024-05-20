
from FakeClassifier import FakeClassifier
from PositionTracker import PositionTracker
from zapper import Zapper

if __name__ == '__main__':
    Zapper = Zapper()
    PT = PositionTracker(Zapper)
    FC = FakeClassifier(freq= 20, PositionTracker = PT)
    FC.start_recording()


