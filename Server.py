import socket
import pygame


pygame.joystick.init()

joystick = pygame.joystick.Joystick(0)
joystick.init()

while True:
    print joystick.get_axis(1)

"""s = socket.socket()
port = 6969

s.bind(('', port))
s.listen(5)

while True:
    c, addr = s.accept()
    c.send('0.3,0.3,0.2')"""