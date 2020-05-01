from socket import *
from time import ctime
import uinput
from evdev import UInput, ecodes as e


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

ctrCmd = ['1','2','3','4','A','B','C','D','5','6','7','8','E','F','G','H']

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
                                        press(e.KEY_UP)
                                        print ('Up')
                                if data == ctrCmd[8]:
                                        release(e.KEY_UP)
                                if data == ctrCmd[1]:
                                        press(e.KEY_DOWN)
                                        print ('Down')
                                if data == ctrCmd[9]:
                                        release(e.KEY_DOWN)
                                if data == ctrCmd[2]:
                                        press(e.KEY_LEFT)
                                        print ('Left')
                                if data == ctrCmd[10]:
                                        release(e.KEY_LEFT)
                                if data == ctrCmd[3]:
                                        press(e.KEY_RIGHT)
                                        print ('Right')
                                if data == ctrCmd[11]:
                                        release(e.KEY_RIGHT)
                                if data == ctrCmd[4]:
                                        press(e.KEY_A)
                                        print ('btnA')
                                if data == ctrCmd[12]:
                                        release(e.KEY_A)
                                if data == ctrCmd[5]:
                                        press(e.KEY_B)
                                        print ('btnB')
                                if data == ctrCmd[13]:
                                        release(e.KEY_B)
                                if data == ctrCmd[6]:
                                        press(e.KEY_F1)
                                        print ('btnC')
                                if data == ctrCmd[14]:
                                        release(e.KEY_F1)
                                if data == ctrCmd[7]:
                                        press(e.KEY_ESC)
                                        print ('btnD')
                                if data == ctrCmd[15]:
                                        release(e.KEY_ESC)
                                break
                except KeyboardInterrupt:
                        tcpSerSock.close();
tcpSerSock.close();
