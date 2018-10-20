from DriveTrain import DriveTrain
from Client import Client

class Robot(object):

    def __init__(self):
        self.drive_train = DriveTrain()
        self.client = Client()
        self.client.start()

    def run(self):
        while True:
            y, x, turn = self.client.parse_data(self.client.receive())
            # self.drive_train.standard_drive(y, x, turn)
            print (x + y + turn)


r = Robot()
r.run()