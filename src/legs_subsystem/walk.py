import threading
import time
from servo import Servo
from legs import Legs

def movement(legs):
    legs.rf_elbow.move_time(40, .2)
    legs.lb_elbow.move_time(40, .2)

if __name__ == "__main__":
    legs = Legs()
    time.sleep(1)

    while(True):
        try:
            movement(legs)
            time.sleep(30)
        except KeyboardInterrupt:
            break

    legs.stop_thread()