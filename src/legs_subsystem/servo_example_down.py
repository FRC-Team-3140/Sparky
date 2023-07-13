# Check the connection to the servo board
# i2cdetect -y -r 1

# Jetson Nano Connections
# 3.3v -> VCC
# GND -> GND
# PIN3 -> SDA
# PIN5 -> SCL
# 5v/6v -> V+

from typing import Any
from adafruit_servokit import ServoKit
import time

print("Connecting to servo board...")
PCA9685 = ServoKit(channels=16)
print("    connected.")

# This class manages a servo connected to the PCA9685 servo controller.
class Servo:
    def __init__(self, servo_id, home_angle=100, reverse=False, min_angle=0, max_angle=180) -> None:
        self.servo = PCA9685.servo[servo_id]
        self.servo.set_pulse_width_range(500, 2500)
        self.home_angle = home_angle
        self.min_angle = min_angle
        self.max_angle = max_angle
        self.reverse = reverse

        self.set_angle(home_angle)

    def set_angle(self, angle: int) -> None:
        if angle < self.min_angle:
            angle = self.min_angle
        elif angle > self.max_angle:
            angle = self.max_angle
        
        if self.reverse:
            angle = 180 - angle

        self.servo.angle = angle

    def get_angle(self) -> int:
        return self.servo.angle
        

    

lb_shoulder = Servo(0,90,False) #
lb_elbow = Servo(1,120)
lb_wrist = Servo(2,90)

lf_shoulder = Servo(4,80,True)
lf_elbow = Servo(5,120)
lf_wrist = Servo(6,90)

rf_shoulder = Servo(8,97,False) 
rf_elbow = Servo(9,100,True)
rf_wrist = Servo(10,90,True)

rb_shoulder = Servo(12,90,True) # 
rb_elbow = Servo(13,100,True)
rb_wrist = Servo(14,90,True)


def print_servo_status():
    global lb_shoulder, lb_elbow, lb_wrist, lf_shoulder, lf_elbow, lf_wrist, rf_shoulder, rf_elbow, rf_wrist, rb_shoulder, rb_elbow, rb_wrist
    print("lb_shoulder: ", lb_shoulder.get_angle())
    print("lb_elbow: ", lb_elbow.get_angle())
    print("lb_wrist: ", lb_wrist.get_angle())
    print("lf_shoulder: ", lf_shoulder.get_angle())
    print("lf_elbow: ", lf_elbow.get_angle())
    print("lf_wrist: ", lf_wrist.get_angle())
    print("rf_shoulder: ", rf_shoulder.get_angle())
    print("rf_elbow: ", rf_elbow.get_angle())
    print("rf_wrist: ", rf_wrist.get_angle())
    print("rb_shoulder: ", rb_shoulder.get_angle())
    print("rb_elbow: ", rb_elbow.get_angle())
    print("rb_wrist: ", rb_wrist.get_angle())
    print("")

print_servo_status()

time.sleep(2)

lb_wrist.set_angle(0)
lf_wrist.set_angle(0)
rf_wrist.set_angle(0)
rb_wrist.set_angle(0)


print_servo_status()


time.sleep(2)
lb_elbow.set_angle(145)
lf_elbow.set_angle(145)
rf_elbow.set_angle(135)
rb_elbow.set_angle(135)

print_servo_status()

time.sleep(2)
lb_wrist.set_angle(10)
lf_wrist.set_angle(10)
rf_wrist.set_angle(10)
rb_wrist.set_angle(10)

print_servo_status()
