#!/usr/bin/env python3

import time
import brickpi3
import socket
import json
from datetime import datetime

BP = brickpi3.BrickPi3()
stored_pass = "chupacabra"

class SwitchedPositions(Exception):
    pass

def check(cables):
    activeMotors = []
    ok = 0
    for cable in cables:
        temp = cable.reset()
        ok += temp[0]
        if temp[0] == 1:
            activeMotors.append(temp[1])

if ok > 0:
    print("Ready to go!")
    print("============")
    return activeMotors
    elif ok < 0:
        raise SwitchedPositions
    else:
        print("Could not find any cables.")
        return False


def sockets():
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serv.bind(('0.0.0.0', 9999))
    serv.listen(5)
    time.sleep(0.11)
    print("\nSocket is ready.")
    return serv


def connection(serv):
    while True:
        conn, addr = serv.accept()
        received_json = conn.recv(4096).decode()
        sent_pass, cmd, port = json.loads(received_json)
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print("\n-------------------")
        print(dt_string)
        print("Received:", str(received_json))
        return conn, (cmd, port), sent_pass

class Cable(object):
    motor = None
    sensor = None
    cmd = None
    value = None
    returnValue = None
    
    def __init__(self, index):
        if index == 0:
            self.motor = BP.PORT_A
            self.sensor = BP.PORT_1
            self.portName = 'a'
        elif index == 1:
            self.motor = BP.PORT_B
            self.sensor = BP.PORT_2
            self.portName = 'b'
        elif index == 2:
            self.motor = BP.PORT_C
            self.sensor = BP.PORT_3
            self.portName = 'c'
        elif index == 3:
            self.motor = BP.PORT_D
            self.sensor = BP.PORT_4
            self.portName = 'd'

def sense(self):
    BP.set_sensor_type(self.sensor, BP.SENSOR_TYPE.TOUCH)
    time.sleep(0.11)
    self.value = BP.get_sensor(self.sensor)
    
    def command(self):
        print("Command:", self.cmd)
        print("Sensor:", self.value)
        if self.cmd == 'in':
            if self.value == 0:
                BP.set_motor_position(self.motor, 0); print("=> Motor rotated to position in.")
                self.returnValue.append(0)
            else:
                self.returnValue.append(-1)
    
        elif self.cmd == 'out':
            if self.value == 1:
                BP.set_motor_position(self.motor, 180); print("=> Motor rotated to position out.")
                self.returnValue.append(0)
            else:
                self.returnValue.append(-1)

else:
    raise IndexError
        time.sleep(0.02)
        return

    def reset(self):
        BP.set_sensor_type(self.sensor, BP.SENSOR_TYPE.TOUCH)
        time.sleep(0.11)
        value = BP.get_sensor(self.sensor)
        ports = {1:"A", 2:"B", 4:"C", 8:"D"}
        smartPorts = {1:0, 2:1, 4:2, 8:3}
        print("Checking cable on port ", ports[self.motor],":", sep='')
        print(" Sensor value:", value)
        if value == 1:
            print(" This cable was already connected.")
            return [1, smartPorts[self.motor]]
        elif value == 0:
            BP.set_motor_position(self.motor, 180)
            time.sleep(0.2)
            value = BP.get_sensor(self.sensor)
            if value == 0:
                print(" There is no cable on this port.")
                return [0]
            elif value == 1:
                print("   => Cable was reset to position in")
                print(" This cable was disconnected, when turned on.")
                return [-100]

def main(self, sent_pass, cmd):
    self.cmd = cmd
        self.returnValue = []
        if stored_pass == sent_pass:
            self.returnValue.append(0)
            self.sense()
            self.command()
    else:
        self.returnValue.append(403)
        print("access denied")
        return self.returnValue

def status(self):
    self.sense()
    pos = 'in' if self.value == 1 else 'out'
        return "port {port}: {pos}".format(port=self.portName, pos=pos)

def send_res(conn, results, cmd):
    if results[0] == 0:
        if results[1] == 0:
            statusMSG = "Command executed. The cable is now {cmd}.".format(cmd=cmd)
        elif results[1] == -1:
            statusMSG = "Already done. The cable is now {cmd}.".format(cmd=cmd)
        else:
            statusMSG = "Unexpected error while executing the command."
    elif results[0] == 403:
        statusMSG = "Incorrect password!!!"
    elif results[0] == 1:
        statusMSG = "This cable does not exist."
    elif results[0] == 'status':
        statusMSG = "\n".join(["status:", *results[1]])
    else:
        statusMSG = "Unexpected error while logging in."
    
    conn.send(statusMSG.encode())
    print(statusMSG)
