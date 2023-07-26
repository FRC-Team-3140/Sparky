import threading
import time
from servo import Servo
from legs import Legs
import math
# These are some of the lengths of the bot
# a is the length of the "elbow", alpha is the angle opposite to a
# b is the length of the "wrist", beta is the angle opposite to b 
# c is the distance between the ground and the torso; c is variable, theta is the angle opposite to c

def y_movement(leg, leg2, leg3, leg4, c):
    c = c
    a = 5
    b= 5
    max = 9.5
    min = 2
    alpha = math.acos((pow(b, 2) + pow(c,2) - pow(a, 2))/(2*b*c)) * (180/math.pi)
    beta = math.acos((pow(a, 2) + pow(c,2) - pow(b, 2))/(2*a*c)) * (180/math.pi)
    theta = math.acos((pow(b, 2) + pow(a,2) - pow(c, 2))/(2*b*a)) * (180/math.pi)
    print(alpha, " ", beta, " ", theta)
    if c >= 6:
        leg.move_time(beta, .05)
        
        leg2.move_time(-(theta/2), .05)
        leg3.move_time(beta, .05)
        leg4.move_time(-(theta/2), .05)
    elif c < 6:
        leg.move_time(90-beta, .05)
        leg2.move_time(-(90-theta/2), .05)
        leg3.move_time(90-beta, .05)
        leg4.move_time(-(90-theta/2), .05)

def x_movement(leg, leg2, x):
    a = 5
    b = 5
    c = 7.07
    x = -x
    beta = math.atan(x/c) * (180/ math.pi)
    print(beta)
    leg.move_time(beta, .05)
    leg2.move_time(beta, .05)
    time.sleep(.05)


def fun_semi_circle(leg, leg2, leg3, leg4, leg5, leg6):
    for i in range(4, 6):
        x = math.sqrt(4- pow((i-5), 2))
        y_movement(leg, leg2, leg3, leg4, 10-x)
    for i in range(1, 3):
        x_movement(leg, leg3, i) 
    time.sleep(.05)
    x_movement(leg, leg3, -3)
    time.sleep(.05)
    leg.move_time(0, .05)
    leg2.move_time(0, .05)
    leg3.move_time(0, .05)
    leg4.move_time(0, .05)

if __name__ == "__main__":
    legs = Legs()
    time.sleep(1)

    while(True):
        try:
            # fun_semi_circle(legs.rb_elbow, legs.rb_wrist, legs.lf_elbow, legs.lf_wrist, legs.rb_shoulder, legs.lf_shoulder)
            # time.sleep(.5)
            # fun_semi_circle(legs.lb_elbow, legs.lb_wrist, legs.rf_elbow, legs.rf_wrist, legs.rf_shoulder, legs.lb_shoulder)
            time.sleep(.5)
        except KeyboardInterrupt:
            break

    legs.stop_thread()