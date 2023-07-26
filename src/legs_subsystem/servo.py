from adafruit_servokit import ServoKit
import time

print("Connecting to servo board...")
PCA9685 = ServoKit(channels=16)
print("    connected.")

# This class manages a servo connected to the PCA9685 servo controller.
class Servo:

    def __init__(self, servo_id, home_angle=100, reverse=False, min_angle=0, max_angle=180) -> None:
        self.servo = PCA9685.servo[servo_id]
        self.servo.set_pulse_width_range(500, 2500) #500 to 2500

        self.name = "Servo " + str(servo_id)

        # absolute angles
        self.home_angle = home_angle
        self.min_angle = min_angle
        self.max_angle = max_angle

        self.reverse = reverse

        # Movement variables
        # Relative angles
        self.target_angle = 0.0
        self.start_angle = 0.0
        self.current_angle = 0.0
        self.curent_speed = 0
        self.start_time = time.time()
        self.stop_time = time.time()


        self.set_angle(0.0)

    def set_name(self, name: str) -> None:
        '''
        Set the name of the servo.
        '''
        self.name = name

    def configure(self, min_angle: float, home_angle: float, max_angle: float, default_speed: float) -> None:
        '''
        Configure the servo's min, home, and max angles, and default speed in deg/second.
        '''
        self.min_angle = min_angle
        self.home_angle = home_angle
        self.max_angle = max_angle
        self.default_speed = default_speed


    def set_angle(self, rel_angle: int) -> None:
        '''
        rel_angle is the angle relative to the home angle.
        '''
        angle = self.home_angle + rel_angle

        if angle < self.min_angle:
            angle = self.min_angle
        elif angle > self.max_angle:
            angle = self.max_angle
        
        if self.reverse:
            angle = 180 - angle

        self.servo.angle = angle

    def periodic(self) -> None:
        '''
        This function should be called periodically to update the servo's position.
        '''
        current_time = time.time()


        # Calculate the new angle
        delta_angle = self.target_angle - self.start_angle
        delta_time = current_time - self.start_time
        move_time = self.stop_time - self.start_time
        
        new_angle = self.start_angle + delta_angle*( delta_time / move_time)

        #print('time',current_time, self.start_time, self.stop_time, delta_time)
        #print("angle",self.start_angle, self.target_angle, new_angle)

        # Update the current angle
        self.current_angle = new_angle

        # Check if we've reached the end of the movement
        if current_time >= self.stop_time:
            self.current_angle = self.target_angle
            self.curent_speed = 0.0

        # Set the new angle
        self.set_angle(self.current_angle)

    def move_speed(self, angle: int, speed: float) -> None:
        '''
        Move the servo to the specified angle at the specified speed.
        '''
        # Calculate the time to reach the new angle
        delta_angle = angle - self.current_angle
        delta_time = abs(delta_angle / speed)

        # Set the new movement variables
        self.target_angle = angle
        self.start_angle = self.current_angle
        self.curent_speed = speed
        self.start_time = time.time()
        self.stop_time = self.start_time + delta_time
        print("moving_speed",self.start_time, self.stop_time, delta_time, self.current_angle, self.target_angle)

    def move_time(self, angle: int, delta_time: float) -> None:
        '''
        Move the servo to the specified angle in the specified time.
        '''
        # Calculate the speed to reach the new angle
        delta_angle = angle - self.current_angle
        speed = delta_angle / delta_time

        # Set the new movement variables
        self.target_angle = angle
        self.start_angle = self.current_angle
        self.curent_speed = speed
        self.start_time = time.time()
        self.stop_time = self.start_time + delta_time
        print("move_time",self.start_time, self.stop_time, delta_time, self.current_angle, self.target_angle)

