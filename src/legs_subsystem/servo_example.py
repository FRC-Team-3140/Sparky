# Check the connection to the servo board
# i2cdetect -y -r 1

# Jetson Nano Connections
# 3.3v -> VCC
# GND -> GND
# PIN3 -> SDA
# PIN5 -> SCL
# 5v/6v -> V+

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
        

lb_shoulder = Servo(0,90,False)
lb_elbow = Servo(1,140)
lb_wrist = Servo(2,0)

lf_shoulder = Servo(4,90,True)
lf_elbow = Servo(5,140)
lf_wrist = Servo(6,0)

rf_shoulder = Servo(8,90,False)
rf_elbow = Servo(9,120,True)
rf_wrist = Servo(10,0,True)

rb_shoulder = Servo(12,90,True)
rb_elbow = Servo(13,120,True)
rb_wrist = Servo(14,0,True)

servo_id = 6
servo_angle = 90

myKit.servo[servo_id].angle=servo_angle

print("Servo ID: ", servo_id, " set to ", servo_angle, " degrees")

time.sleep(1)
