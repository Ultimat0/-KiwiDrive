import socket


class Client (object):

    def __init__(self):
        self.s = socket.socket()
        self.port = 6969

    def start(self):
        self.s.connect(('10.0.0.18', self.port))

    def receive(self):
        return self.s.recv(1024)

    def parse_data(self, data):
        values = data.split(',')
        return float(values[0]), float(values[1]), float(values[2])