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
        

lb_shoulder = Servo(0,90,False) #
lb_elbow = Servo(1,120)
lb_wrist = Servo(2,180)

lf_shoulder = Servo(4,80,True)
lf_elbow = Servo(5,120)
lf_wrist = Servo(6,90)

rf_shoulder = Servo(8,97,False) 
rf_elbow = Servo(9,100,True)
rf_wrist = Servo(10,90,True)

rb_shoulder = Servo(12,90,True) # 
rb_elbow = Servo(13,100,True)
rb_wrist = Servo(14,180,True)

# Animate the limbs
rf_elbow = Servo(9,30,True)

time.sleep(1)
rf_shoulder = Servo(8,97-20,False) 
rf_elbow = Servo(9,30,True)
rf_wrist = Servo(10,90+10,True)
lb_elbow = Servo(1,120)
rb_elbow = Servo(13,100-20,True)
rb_wrist = Servo(14,100,True)
lb_wrist = Servo(2,180)
time.sleep(1)
rf_shoulder = Servo(8,97+ 10,False) 
rf_elbow = Servo(9,30-20,True)
rf_wrist = Servo(10,90-10,True)
lb_elbow = Servo(1,120-20)
rb_elbow = Servo(13,100,True)
rb_wrist = Servo(14,180,True)
lb_wrist = Servo(2,100)
time.sleep(1)
rf_shoulder = Servo(8,97-20,False) 
rf_elbow = Servo(9,30,True)
rf_wrist = Servo(10,90+10,True)
lb_elbow = Servo(1,120)
rb_elbow = Servo(13,100-20,True)
rb_wrist = Servo(14,100,True)
lb_wrist = Servo(2,180)
time.sleep(1)
rf_shoulder = Servo(8,97+ 10,False) 
rf_elbow = Servo(9,30-20,True)
rf_wrist = Servo(10,90-10,True)
lb_elbow = Servo(1,120-20)
rb_elbow = Servo(13,100,True)
rb_wrist = Servo(14,180,True)
lb_wrist = Servo(2,100)
time.sleep(1)
rf_shoulder = Servo(8,97-20,False) 
rf_elbow = Servo(9,30,True)
rf_wrist = Servo(10,90+10,True)
lb_elbow = Servo(1,120)
rb_elbow = Servo(13,100-20,True)
rb_wrist = Servo(14,100,True)
lb_wrist = Servo(2,180)
time.sleep(1)
rf_shoulder = Servo(8,97+ 10,False) 
rf_elbow = Servo(9,30-20,True)
rf_wrist = Servo(10,90-10,True)
lb_elbow = Servo(1,120-20)
rb_elbow = Servo(13,100,True)
rb_wrist = Servo(14,180,True)
lb_wrist = Servo(2,100)
time.sleep(1)
rf_shoulder = Servo(8,97-20,False) 
rf_elbow = Servo(9,30,True)
rf_wrist = Servo(10,90+10,True)
lb_elbow = Servo(1,120)
rb_elbow = Servo(13,100-20,True)
rb_wrist = Servo(14,100,True)
lb_wrist = Servo(2,180)
time.sleep(1)
rf_shoulder = Servo(8,97+ 10,False) 
rf_elbow = Servo(9,30-20,True)
rf_wrist = Servo(10,90-10,True)
lb_elbow = Servo(1,120-20)
rb_elbow = Servo(13,100,True)
rb_wrist = Servo(14,180,True)
lb_wrist = Servo(2,100)



