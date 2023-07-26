import threading
import time
from servo import Servo
from legs import Legs

# legs = Legs()
# rf_elbow = legs.rf_elbow 
# lf_elbow = legs.lf_elbow 
# rb_elbow = legs.rb_elbow 
# lb_elbow = legs.lb_elbow 

# rf_wrist = legs.rf_wrist 
# lf_wrist = legs.lf_wrist 
# rb_wrist = legs.rb_wrist 
# lb_wrist = legs.lb_wrist 

def other_wrist_movement(legs):
    # legs.lf_wrist.move_time(0, 5)
    legs.rb_elbow.move_time(60, .1)
    

def wrist_movement(legs):
    legs.rb_wrist.move_time(0, 5)
    legs.rb_elbow.move_time(30, 5)
    time.sleep(5)

    legs.rb_wrist.move_time(-40, 1)
    legs.rb_elbow.move_time(-30, 1)
    time.sleep(1)

    legs.rb_wrist.move_time(0, 5)
    legs.rb_elbow.move_time(0, 5)
    time.sleep(5)

def elbow_movement(legs):
    legs.rb_elbow.move_time(70, 3)
    time.sleep(7)
    legs.rb_elbow.move_time(-50, 2)
    time.sleep(2)

def sit_down(legs):
    legs.rb_wrist.move_time(-110, 2)
    legs.rf_wrist.move_time(-110, 2)
    legs.lb_wrist.move_time(-110, 2)
    legs.lf_wrist.move_time(-110, 2)

    legs.rb_elbow.move_time(70, 2)
    legs.lb_elbow.move_time(70, 2)
    legs.lf_elbow.move_time(70, 2)
    legs.rf_elbow.move_time(70, 2)

def stand_up(legs):
    legs.rb_wrist.move_time(0, 2)
    legs.rf_wrist.move_time(0, 2)
    legs.lb_wrist.move_time(0,2)
    legs.lf_wrist.move_time(0,2)

    legs.rb_elbow.move_time(0, 2)
    legs.lb_elbow.move_time(0, 2)
    legs.lf_elbow.move_time(0,2)
    legs.rf_elbow.move_time(0, 2)


def push_ups(legs):
    sit_down(legs)
    time.sleep(3)
    stand_up(legs)
    time.sleep(3)
def which_direction(legs):
    legs.rf_elbow.move_time(70, .2)
    time.sleep(5)
    legs.rf_elbow.move_time(0, .2)
    time.sleep(5)
    legs.rf_wrist.move_time(70, .2)
if __name__ == "__main__":
    legs = Legs()
    time.sleep(1)

    while(True):
        try:
            # push_ups(legs)
            for i in range(-90, 90):
                legs.lb_wrist.move_time(i, .1)
                time.sleep(.2)
            time.sleep(4)
        except KeyboardInterrupt:
            break

    legs.stop_thread()