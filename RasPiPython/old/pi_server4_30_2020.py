import InputProgram

from socket import *
from time import ctime
import uinput
from evdev import UInput, ecodes as e

InputProgram.setup()

device = uinput.Device([uinput.KEY_E])
ui = UInput()

def press(key):
        ui.write(e.EV_KEY, key, 1)
        ui.syn()
        return 0
def release(key):
        ui.write(e.EV_KEY, key, 0)
        ui.syn()
        return 0

ctrCmd = ['1','2','3','4','A','B','C','D']

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

Address = ['1']

while True:
        print ('Waiting for connection')
        tcpCliSock,addr = tcpSerSock.accept()
        hostIP, port = tcpCliSock.getpeername()
        print(hostIP)
        print ('...connected from :', addr)
        for add in Address:
                if hostIP not in Address:
                        Address.append(hostIP)
                try:
                        data = ''
                        data = tcpCliSock.recv(BUFSIZE)
                        data = data.decode('utf-8')
                        print (data)
                        while True:
                                if not data:
                                        break
                                if data == ctrCmd[0]:
                                        InputProgram.InputUp()
                                        print ('Up')
                                if data == ctrCmd[1]:
                                        InputProgram.InputDown()
                                        print ('Down')
                                if data == ctrCmd[2]:
                                        InputProgram.InputLeft()
                                        print ('Left')
                                if data == ctrCmd[3]:
                                        InputProgram.InputRight()
                                        print ('Right')
                                if data == ctrCmd[4]:
                                        InputProgram.InputA()
                                        print ('btnA')
                                if data == ctrCmd[5]:
                                        InputProgram.InputB()
                                        print ('btnB')
                                if data == ctrCmd[6]:
                                        InputProgram.InputC()
                                        print ('btnC')
                                if data == ctrCmd[7]:
                                        InputProgram.InputD()
                                        print ('btnD')
                                break
                except KeyboardInterrupt:
                        InputProgram.close()
tcpSerSock.close();
