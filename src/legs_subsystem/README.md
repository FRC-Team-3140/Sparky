Setup jetson IO

https://jetsonhacks.com/2020/05/04/spi-on-jetson-using-jetson-io/

 * Setup the rasberry pi v2 camera as Sony IMX219
 * Enable the GPIO 
   * Configure 40 pin header
     * Configure pins manually
 * Save and reboot

```
ls /dev/i2c* /dev/spi*


```

```
  =================== Jetson Expansion Header Tool ===================
 |                                                                    |
 |                                                                    |
 |                      3.3V (  1) .. (  2) 5V                        |
 |                      i2c2 (  3) .. (  4) 5V                        |
 |                      i2c2 (  5) .. (  6) GND                       |
 |                    unused (  7) .. (  8) uartb                     |
 |                       GND (  9) .. ( 10) uartb                     |
 |                    unused ( 11) .. ( 12) unused                    |
 |                    unused ( 13) .. ( 14) GND                       |
 |                        NA ( 15) .. ( 16) unused                    |
 |                      3.3V ( 17) .. ( 18) unused                    |
 |                 spi1_dout ( 19) .. ( 20) GND                       |
 |                  spi1_din ( 21) .. ( 22) unused                    |
 |                  spi1_sck ( 23) .. ( 24) spi1_cs0                  |
 |                       GND ( 25) .. ( 26) spi1_cs1                  |
 |                      i2c1 ( 27) .. ( 28) i2c1                      |
 |                        NA ( 29) .. ( 30) GND                       |
 |                        NA ( 31) .. ( 32) unused                    |
 |                    unused ( 33) .. ( 34) GND                       |
 |                    unused ( 35) .. ( 36) unused                    |
 |                    unused ( 37) .. ( 38) unused                    |
 |                       GND ( 39) .. ( 40) unused                    |
 |                                                                    |
```

Install python 3.7

sudo apt install python3.7-dev

Install circuitpython under python3.7

sudo python3.7 -m pip install adafruit-circuitpython-servokit

conda install --channel "RoboStack" package
