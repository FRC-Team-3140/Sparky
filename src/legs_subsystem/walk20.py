import threading
import time
from servo import Servo
from legs import Legs
import math
# These are some of the lengths of the bot
# a is the length of the "elbow", alpha is the angle opposite to a
# b is the length of the "wrist", beta is the angle opposite to b 
# c is the distance between the ground and the torso; c is variable, theta is the angle opposite to c

def y_movement(leg, leg2, c):
    a = 5
    b = 5
    c = c 
    beta = math.acos((pow(a, 2) + pow(c,2) - pow(b, 2))/(2*a*c)) * (180/math.pi)
    theta = math.acos((pow(b, 2) + pow(a,2) - pow(c, 2))/(2*b*a)) * (180/math.pi)
    print("beta: ", beta)
    print("theta: ", theta)

    # if theta/2 - 40 < 0: theta = abs(theta - 40)
    # elif theta/2 -40 > 0: theta += 40    
    leg.move_time(beta-10, .05)
    leg2.move_time(-(theta/2 + 30), .05)

def x_movement(leg, leg2, x):
    time.sleep(1)

if __name__ == "__main__":
    legs = Legs()
    time.sleep(1)

    while(True):
        try:
            y_movement(legs.lf_elbow,   legs.lf_wrist, 9)
            time.sleep(1)
        except KeyboardInterrupt:
            break

    legs.stop_thread()