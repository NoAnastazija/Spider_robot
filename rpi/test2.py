import time
from adafruit_servokit import ServoKit

MIN_IMP = 500
MAX_IMP = 2400

NUMER_OF_LEGS = 4

# Initial and final positions of joints
SHOULDER_INIT = [90, 90, 90, 90]
SHOULDER_FINAL = [90, 90, 90, 90]
ARM_INIT = [90, 90, 90, 90]
ARM_FINAL = [90, 90, 90, 90]
HAND_INIT = [90, 90, 90, 90]
HAND_FINAL = [90, 90, 90, 90]

# Servomotor to port mapping
SHOULDER_SERVO = [0, 4, 8, 12]
ARM_SERVO = [1, 5, 9, 13]
HAND_SERVO = [2, 6, 10, 14]

# Current position of a joint
shoulder = SHOULDER_INIT.copy()
arm = ARM_INIT.copy()
hand = HAND_INIT.copy()

# Desired position of a joint
shoulder_to = SHOULDER_INIT.copy()
arm_to = ARM_INIT.copy()
hand_to = HAND_INIT.copy()

pca = ServoKit(channels=16)

def set_shoulder(leg, angle):
    pca.servo[SHOULDER_SERVO[leg]].angle = angle
    shoulder[leg] = angle
    
def set_arm(leg, angle):
    pca.servo[ARM_SERVO[leg]].angle = angle
    arm[leg] = angle

def set_hand(leg, angle):
    pca.servo[HAND_SERVO[leg]].angle = angle
    hand[leg] = angle

def move_legs():
    moved = False
    for leg in range(NUMER_OF_LEGS):
        if shoulder[leg] < shoulder_to[leg]:
            set_shoulder(leg, shoulder[leg] + 1)
            moved = True
        elif shoulder_to[leg] < shoulder[leg]:
            set_shoulder(leg, shoulder[leg] - 1)
            moved = True
        else:
            pca.servo[SHOULDER_SERVO[leg]].angle = None

        if arm[leg] < arm_to[leg]:
            set_arm(leg, arm[leg] + 1)
            moved = True
        elif arm_to[leg] < arm[leg]:
            set_arm(leg, arm[leg] - 1)
            moved = True
        else:
            pca.servo[ARM_SERVO[leg]].angle = None

        if hand[leg] < hand_to[leg]:
            set_hand(leg, hand[leg] + 1)
            moved = True
        elif hand_to[leg] < hand[leg]:
            set_hand(leg, hand[leg] - 1)
            moved = True
        else:
            pca.servo[HAND_SERVO[leg]].angle = None

    return moved

def move():
    while move_legs():
        time.sleep(0.02)

def init():
    for leg in range(NUMER_OF_LEGS):
        pca.servo[SHOULDER_SERVO[leg]].set_pulse_width_range(MIN_IMP, MAX_IMP)
        pca.servo[ARM_SERVO[leg]].set_pulse_width_range(MIN_IMP, MAX_IMP)
        pca.servo[HAND_SERVO[leg]].set_pulse_width_range(MIN_IMP, MAX_IMP)
        set_shoulder(leg, SHOULDER_INIT[leg])
        set_arm(leg, ARM_INIT[leg])
        set_hand(leg, HAND_INIT[leg])

def reset():
    for leg in range(NUMER_OF_LEGS):
        shoulder_to[leg] = SHOULDER_FINAL[leg]
        arm_to[leg] = ARM_FINAL[leg]
        hand_to[leg] = HAND_FINAL[leg]
    move()

def main():
    move()

if __name__ == '__main__':
    init()
    try:
        main()
    finally:
        reset()
