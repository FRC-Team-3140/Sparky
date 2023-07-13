# This script will connect to the PCM9685 servo controller and test the servos.

# Imports for the jetson nano and gpio pins.
import Jetson.GPIO as GPIO

# Imports for the servo controller.
import time
import board
import busio
import adafruit_pca9685


# Setup the servo controller.
i2c = busio.I2C(board.SCL, board.SDA)
pca = adafruit_pca9685.PCA9685(i2c)
pca.frequency = 50

# Setup the GPIO pins.
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(32, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)


# This class defines the servo object for a servo connected to the pca board.
class Servo:

    def __init__(self,channel_id, min_range=500, max_range=2500) -> None:
        self.servo = pca.channels[channel_id]
        self.servo.set_pulse_width_range(500, 2500)

    def set_angle(self, angle: int) -> None:
        self.servo.duty_cycle = int((angle / 180) * 65535)

