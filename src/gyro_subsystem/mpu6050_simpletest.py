# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_mpu6050

i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
time.sleep(1)
mpu = adafruit_mpu6050.MPU6050(i2c)
time.sleep(1)

gyro_x = []
gyro_y = []
gyro_z = []
# time.sleep(1)
while True:
    # time.sleep(1)
    # print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (mpu.acceleration))
    # print("Gyro X:%.2f, Y: %.2f, Z: %.2f rad/s" % (mpu.gyro))
    # print("Temperature: %.2f C" % mpu.temperature)
    # print("")

    gyro_x.append(mpu.gyro[0])
    gyro_y.append(mpu.gyro[2])
    # gyro_z.append(mpu.gyro[3])
    print(gyro_x)
    time.sleep(1)



