# Check the connection to the servo board
# i2cdetect -y -r 1

# Jetson Nano Connections
# 3.3v -> VCC
# GND -> GND
# PIN3 -> SDA
# PIN5 -> SCL
# 5v/6v -> V+

from servo import Servo
import time
        

lb_shoulder = Servo(0,90,False) #
lb_elbow = Servo(1,140)
lb_wrist = Servo(2,110)

lf_shoulder = Servo(4,80,True)
lf_elbow = Servo(5,120)
lf_wrist = Servo(6,110)

rf_shoulder = Servo(8,97,False) 
rf_elbow = Servo(9,100,True)
rf_wrist = Servo(10,110,True)

rb_shoulder = Servo(12,90,True) # 
rb_elbow = Servo(13,120,True)
rb_wrist = Servo(14,110,True)


time.sleep(1)

lf_elbow.move_time(-20, .5)
lf_wrist.move_time(-20, .5)
tmp_time = time.time()
while time.time() - tmp_time < .5:
    #print("moving",time.time(),lf_elbow.current_angle,lf_elbow.target_angle)
    lf_elbow.periodic()
    lf_wrist.periodic()
    time.sleep(0.01)

lf_elbow.move_time(30, .5)
lf_wrist.move_time(30, .5)
tmp_time = time.time()
while time.time() - tmp_time < .5:
    #print("moving",time.time(),lf_elbow.current_angle,lf_elbow.target_angle)
    lf_elbow.periodic()
    lf_wrist.periodic()
    time.sleep(0.01)

lf_elbow.move_time(0, .5)
lf_wrist.move_time(0, .5)
tmp_time = time.time()
while time.time() - tmp_time < 2:
    #print("moving",time.time(),lf_elbow.current_angle,lf_elbow.target_angle)
    lf_elbow.periodic()
    lf_wrist.periodic()
    time.sleep(0.01)