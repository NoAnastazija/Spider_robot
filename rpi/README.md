# Spider Robot Raspberry Pi Sample Code

This folder contains sample Raspberry Pi Python code for the Spider Robot project.

## Requirements

1. Raspberry Pi 2 or later
2. Raspberry Pi power supply
3. Adafruit PCA9685 PWM driver
4. 5 V, 3500 mA power supply
5. Spider Robot

## Wiring

Raspberry Pi and PCA9685 communicate using I2C.

| Raspberry Pi GPIO | PCA9685 |
| ----------------- | ------- |
| pin 1 3.3V        | VCC     |
| pin 3 SDA.1       | SDA     |
| pin 5 SCL.1       | SCL     |
| pin 9 0V          | GND     |

Servos need a lot of power. To prevent the PWM driver from overload, PCA9685 has a dedicated power connector.

| 5 V, 3500 mA power supply | PCA9685 dedicated power connector |
| ------------------------- | --------------------------------- |
| +                         | V+                                |
| -                         | GND                               |

See _Leg to servo mapping_ in [test2.py](test2.py), which servo to connect to which PCA9685 PWM port.

## Enable I2C on Raspberry Pi

```sh
sudo raspi-config
```

Then follow the GUI to enable Interface Options → I2C.

## Align Servos at 90°

1. Unscrew and remove servo arms to make Spider Robot servos rotate freely.
2. Run [inicialization.py](inicialization.py) to move all servos to 90°.
3. Move each Spider Robot joint to the neutral position. Neutral position is the middle of the joint movement range.
4. Reattach servo arms with screws.

## Development

The work-in-progress code is in [test2.py](test2.py).
