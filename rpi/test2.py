import time
from adafruit_servokit import ServoKit

MIN_IMP = 500
MAX_IMP = 2400

NUMBER_OF_SERVOS = 16

# Servo configuration
#                 0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15
SERVO_ENABLED = [ 1,  1,  0,  1,  1,  1,  0,  1,  1,  1,  0,  1,  1,  1,  0,  1]
SERVO_K       = [ 1, -1,  1,  1, -1,  1,  1, -1, -1,  1,  1, -1,  1, -1,  1,  1]
SERVO_N       = [90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]

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

pca = ServoKit(channels=NUMBER_OF_SERVOS)

def set_servo(i, angle):
    pca.servo[i].angle = SERVO_K[i]*angle + SERVO_N[i]
    servo_at[i] = angle

def move_servos():
    moved = False
    for i in range(NUMBER_OF_SERVOS):
        if SERVO_ENABLED[i]:
            #servo_spd[i] = (10*servo_spd[i] + (servo_to[i] - servo_at[i])) / 11
            if servo_at[i] < servo_to[i]:
                #set_servo(i, servo_at[i] + max(round(servo_spd[i] / 10), 1))
                set_servo(i, servo_at[i] + 1)
                moved = True
            elif servo_at[i] > servo_to[i]:
                #set_servo(i, servo_at[i] + min(round(servo_spd[i] / 10), -1))
                set_servo(i, servo_at[i] - 1)
                moved = True
    return moved

def move():
    while move_servos():
        time.sleep(0.05)

def init():
    for i in range(NUMBER_OF_SERVOS):
        if SERVO_ENABLED[i]:
            pca.servo[i].set_pulse_width_range(MIN_IMP, MAX_IMP)
            set_servo(i, 0)

def reset():
    for i in range(NUMBER_OF_SERVOS):
        servo_to[i] = 0
    move()
    for i in range(NUMBER_OF_SERVOS):
        if SERVO_ENABLED[i]:
            pca.servo[i].angle = None

def rise():
    for i in [FR_HAND, FL_HAND, RR_HAND, RL_HAND]:
        servo_to[i] = -20 # -40
    move()
    for i in [FR_ARM, FL_ARM, RR_ARM, RL_ARM]:
        servo_to[i] = -20 # -20
    for i in [FR_HAND, FL_HAND, RR_HAND, RL_HAND]:
        servo_to[i] = 0
    move()

def rise_legs():
    for i in [FR_ARM, FL_ARM, RR_ARM, RL_ARM]:
        servo_to[i] = 70
    for i in [FR_HAND, FL_HAND, RR_HAND, RL_HAND]:
        servo_to[i] = -70
    move()
    
    
def step_fw():
    servo_to[FR_HAND] = 30
    servo_to[RL_HAND] = 30
    servo_to[FR_SHOULDER] =  40
    servo_to[RL_SHOULDER] = -40
    move()
    
    servo_to[FR_HAND] = 0
    servo_to[RL_HAND] = 0
    move()
    
    servo_to[FR_SHOULDER] = 0
    servo_to[FR_HAND] = -30
    servo_to[RL_SHOULDER] = -10
    servo_to[RL_HAND] = -30
    move()
    
    
   
    servo_to[FL_HAND] = 30
    servo_to[RR_HAND] = 30
    servo_to[FL_SHOULDER] = 40
    servo_to[RR_SHOULDER] = -40
    move()
    
    servo_to[FL_HAND] = 0
    servo_to[RR_HAND] = 0
    move()
    
    servo_to[FL_SHOULDER] = 0
    servo_to[FL_HAND] = -30
    servo_to[RR_SHOULDER] = -10
    servo_to[RR_HAND] = -30
    move()
    
    
   # servo_to[FR_HAND] = 30
   # servo_to[RL_HAND] = 30
   # servo_to[FR_SHOULDER] =  40
   # servo_to[RL_SHOULDER] = -40
   # move()
    
   # servo_to[FR_HAND] = -40
   # servo_to[RL_HAND] = -30
   # servo_to[FR_SHOULDER] =  40
   # servo_to[RL_SHOULDER] = -40
   # move()

  
    
        


def stretch_rr():
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
    
def move_leg():
    for i in [FR_SHOULDER, FR_ARM, FR_HAND]:
        servo_to[i] = 30
        move()
        time.sleep(1)
        
        servo_to[FR_SHOULDER] = 50
        servo_to[FR_ARM] = 40
        move()
        time.sleep(1)

def turn_right():
    servo_to[FR_HAND] = 30
    servo_to[RL_HAND] = 30
    move()
    
    servo_to[FR_HAND] = 0
    servo_to[RL_HAND] = 0
    move()
    
  
    servo_to[FR_HAND] = -30
    servo_to[RL_HAND] = -30
 #   move()
    move()
    for i in [FR_SHOULDER, RL_SHOULDER]:
        servo_to[i] = -50
        move()
    
        servo_to[FL_HAND] = -30
        servo_to[RR_HAND] = -30
        
    for i in [FL_SHOULDER, RR_SHOULDER]:
        servo_to[i] = 50
        move()
    for i in [FR_SHOULDER, RL_SHOULDER]:
        servo_to[i] = -50
        move()
    servo_to[FL_SHOULDER] = 90
    move()
    servo_to[RL_SHOULDER] = -90
    move()
    
def main():
    #rise_legs()
    rise()
    time.sleep(1)
    #turn_right()
    #time.sleep(1)
    step_fw()
    time.sleep(1)

if __name__ == '__main__':
    init()
    try:
        main()
    finally:
        reset()
