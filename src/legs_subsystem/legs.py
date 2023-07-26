import threading
import time
from servo import Servo

class Legs:

    def __init__(self):
        self.lb_shoulder = Servo(0,90,False)
        self.lb_elbow = Servo(1,180)
        self.lb_wrist = Servo(2,110)

        self.lf_shoulder = Servo(4,80,True)
        self.lf_elbow = Servo(5,120)
        self.lf_wrist = Servo(6,110)

        self.rf_shoulder = Servo(8,97,False) 
        self.rf_elbow = Servo(9,100,True) #100
        self.rf_wrist = Servo(10,110,True)

        self.rb_shoulder = Servo(12,90,True)
        self.rb_elbow = Servo(13,110,True)
        self.rb_wrist = Servo(14,110,True)

        self.running = True
        self.thread = threading.Thread(target=self.periodic)
        self.start_thread()

    def periodic(self):
        while self.running:
            self.lb_shoulder.periodic()
            self.lb_elbow.periodic()
            self.lb_wrist.periodic()
            
            self.lf_shoulder.periodic()
            self.lf_elbow.periodic()
            self.lf_wrist.periodic()
            
            self.rf_shoulder.periodic()
            self.rf_elbow.periodic()
            self.rf_wrist.periodic()
            
            self.rb_shoulder.periodic()
            self.rb_elbow.periodic()
            self.rb_wrist.periodic()
            time.sleep(0.01)


    def start_thread(self):
        self.running = True
        self.thread.start()


    def stop_thread(self):
        self.running = False
        self.thread.join()
    
    def run_rb_lf_elbow(self, angle, time):
        self.rb_elbow.move_time(angle, time)
        self.lf_elbow.move_time(angle, time)

    def run_rb_lf_wrist(self, angle, time):
        self.rb_wrist.move_time(angle, time)
        self.lf_wrist.move_time(angle, time)    

    def run_rb_lf_shoulder(self, angle, time):
        self.rb_shoulder.move_time(angle, time)
        self.lf_shoulder.move_time(angle, time)        


def dance(legs):

    # Setup
    legs.lf_shoulder.move_time(0, .25)
    legs.lf_elbow.move_time(40, .25)
    legs.lf_wrist.move_time(-40, .25)
    legs.rf_shoulder.move_time(0, .25)
    legs.rf_elbow.move_time(40, .25)
    legs.rf_wrist.move_time(-40, .25)
    legs.lb_shoulder.move_time(-20, .25)
    legs.lb_elbow.move_time(-20, .25)
    legs.lb_wrist.move_time(-60, .25)
    legs.rb_shoulder.move_time(-20, .25)
    legs.rb_elbow.move_time(-20, .25)
    legs.rb_wrist.move_time(-60, .25)

    time.sleep(0.25)

    time.sleep(1)
    for __ in range(4):
        for _ in range(2):
            legs.lf_shoulder.move_time(-20, .25)
            legs.lf_elbow.move_time(20, .25)
            legs.lf_wrist.move_time(-20, .25)
            legs.rf_shoulder.move_time(20, .25)
            legs.rf_elbow.move_time(20, .25)
            legs.rf_wrist.move_time(-20, .25)
            time.sleep(0.25)

            legs.lf_shoulder.move_time(0, .25)
            legs.lf_elbow.move_time(40, .25)
            legs.lf_wrist.move_time(-40, .25)
            legs.rf_shoulder.move_time(0, .25)
            legs.rf_elbow.move_time(40, .25)
            legs.rf_wrist.move_time(-40, .25)
            time.sleep(0.25)

            time.sleep(.25)

            legs.lf_shoulder.move_time(20, .25)
            legs.lf_elbow.move_time(20, .25)
            legs.lf_wrist.move_time(-20, .25)
            legs.rf_shoulder.move_time(-20, .25)
            legs.rf_elbow.move_time(20, .25)
            legs.rf_wrist.move_time(-20, .25)
            time.sleep(0.25)

            legs.lf_shoulder.move_time(0, .25)
            legs.lf_elbow.move_time(40, .25)
            legs.lf_wrist.move_time(-40, .25)
            legs.rf_shoulder.move_time(0, .25)
            legs.rf_elbow.move_time(40, .25)
            legs.rf_wrist.move_time(-40, .25)
            time.sleep(0.25)

            time.sleep(.25)

        legs.lf_shoulder.move_time(-20, .5)
        legs.lf_elbow.move_time(20, .5)
        legs.lf_wrist.move_time(-20, .5)
        legs.rf_shoulder.move_time(50, .5)
        legs.rf_elbow.move_time(-70, .5)
        legs.rf_wrist.move_time(30, .5)
        time.sleep(0.5)

        legs.lf_shoulder.move_time(0, .5)
        legs.lf_elbow.move_time(40, .5)
        legs.lf_wrist.move_time(-40, .5)
        legs.rf_shoulder.move_time(0, .5)
        legs.rf_elbow.move_time(40, .5)
        legs.rf_wrist.move_time(-40, .5)
        time.sleep(0.5)

        time.sleep(.25)

        legs.lf_shoulder.move_time(50, .5)
        legs.lf_elbow.move_time(-70, .5)
        legs.lf_wrist.move_time(30, .5)
        legs.rf_shoulder.move_time(-20, .5)
        legs.rf_elbow.move_time(20, .5)
        legs.rf_wrist.move_time(-20, .5)
        time.sleep(0.5)


        legs.lf_shoulder.move_time(0, .5)
        legs.lf_elbow.move_time(40, .5)
        legs.lf_wrist.move_time(-40, .5)
        legs.rf_shoulder.move_time(0, .5)
        legs.rf_elbow.move_time(40, .5)
        legs.rf_wrist.move_time(-40, .5)
        time.sleep(0.5)

        time.sleep(.25)


    #time.sleep(3)
    # Finish
    # legs.lf_shoulder.move_time(0, .5)
    # legs.lf_elbow.move_time(0, .5)
    # legs.lf_wrist.move_time(0, .5)
    # legs.rf_shoulder.move_time(0, .5)
    # legs.rf_elbow.move_time(0, .5)
    # legs.rf_wrist.move_time(0, .5)
    # legs.lb_shoulder.move_time(0, .5)
    # legs.lb_elbow.move_time(0, .5)
    # legs.lb_wrist.move_time(0, .5)
    # legs.rb_shoulder.move_time(0, .5)
    # legs.rb_elbow.move_time(0, .5)
    # legs.rb_wrist.move_time(0, .5)
    # time.sleep(0.5)

    time.sleep(2)


if __name__ == "__main__":
    legs = Legs()
    time.sleep(1)

    while(True):
        try:
            dance(legs)
            time.sleep(30)
        except KeyboardInterrupt:
            break

    legs.stop_thread()