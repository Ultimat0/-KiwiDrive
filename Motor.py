class Motor(object):

    def __init__(self, pin):
        self.pin = pin

    def set_speed(self, speed):
        if speed > 1: speed = 1
        elif speed < -1: speed = -1
        print('not ready')
        # wait for io

    def get_position(self):
        print('not ready')
        #wait for encoder info