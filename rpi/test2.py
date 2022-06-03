import time
from adafruit_servokit import ServoKit

MIN_IMP = 500
MAX_IMP = 2400

NUMER_OF_SERVOS = 16

# Angle mappings of each servo
#           0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15
SERVO_K = [ 1, -1,  1,  1, -1,  1,  1, -1,  1,  1,  1, -1, -1, -1,  1,  1]
SERVO_N = [90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]

# Current and desired positions of each servo
servo_at = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
servo_to = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#servo_spd = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Leg to servo mapping
FR_SHOULDER = 0
FL_SHOULDER = 4
RR_SHOULDER = 8
RL_SHOULDER = 12
FR_ARM = 1
FL_ARM = 5
RR_ARM = 9
RL_ARM = 13
FR_HAND = 3
FL_HAND = 7
RR_HAND = 11
RL_HAND = 15

pca = ServoKit(channels=NUMER_OF_SERVOS)

def set_servo(i, angle):
    pca.servo[i].angle = SERVO_K[i]*angle + SERVO_N[i]
    servo_at[i] = angle

def move_servos():
    moved = False
    for i in range(NUMER_OF_SERVOS):
        #servo_spd[i] = (10*servo_spd[i] + (servo_to[i] - servo_at[i])) / 11
        if servo_at[i] < servo_to[i]:
            #set_servo(i, servo_at[i] + max(round(servo_spd[i] / 10), 1))
            set_servo(i, servo_at[i] + 1)
            moved = True
        elif servo_at[i] > servo_to[i]:
            #set_servo(i, servo_at[i] + min(round(servo_spd[i] / 10), -1))
            set_servo(i, servo_at[i] - 1)
            moved = True
        else:
            pca.servo[i].angle = None
    return moved

def move():
    while move_servos():
        time.sleep(0.02)

def init():
    for i in range(NUMER_OF_SERVOS):
        pca.servo[i].set_pulse_width_range(MIN_IMP, MAX_IMP)
        set_servo(i, 0)
        time.sleep(0.2)

def reset():
    for i in range(NUMER_OF_SERVOS):
        servo_to[i] = 0
    move()

def main():
    for i in [RR_SHOULDER, RR_ARM, RR_HAND]:
        servo_to[i] = 30
        move()
    time.sleep(1)
    for i in [RR_SHOULDER, RR_ARM, RR_HAND]:
        servo_to[i] = -30
        move()
    time.sleep(1)
    for i in [RR_SHOULDER, RR_ARM, RR_HAND]:
        servo_to[i] = 0
        move()
    time.sleep(1)

if __name__ == '__main__':
    init()
    try:
        main()
    finally:
        reset()
