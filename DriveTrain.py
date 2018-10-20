import math
from Motor import Motor

class DriveTrain(object):

    def __init__(self):
        self.motor_a = Motor(1)
        self.motor_b = Motor(2)
        self.motor_c = Motor(3)

    def standard_drive (self, y, x, turn):
        self.motor_a.setSpeed((-0.5 * x) - ((math.sqrt(3)/2) * y) + turn)
        self.motor_b.setSpeed((-0.5 * x) + ((math.sqrt(3)/2) * y) + turn)
        self.motor_c.setSpeed(x + turn)