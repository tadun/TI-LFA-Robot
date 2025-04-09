#!/usr/bin/env python3

import time
import brickpi3
import socket
import sys
from datetime import datetime
import libmiro_new as lm

def main():
    serv = lm.sockets()
    while True:
        try:
            conn, cmd, sent_pass = lm.connection(serv)
            
            if cmd[0] == 'status':
                status = []
                for key, cable in cables.items():
                    status.append(cable.status())
                lm.send_res(conn, ['status', status], 'status')
            else:
                result = cables[int(cmd[1])].main(sent_pass, cmd[0])
                lm.send_res(conn, result, cmd[0])
        except KeyError:
            lm.send_res(conn, [1], cmd)

cables = [lm.Cable(x) for x in range(4)]

try:
    activeMotors = lm.check(cables)
    print(activeMotors)
    if activeMotors is False:
        print("No motors detected, connect motors and rerun the program")
        sys.exit()
    cables = {x: lm.Cable(x) for x in activeMotors}
except lm.SwitchedPositions:
    print("Please reurn the program. Now the positions should be set correctly.")
    sys.exit()

while True:
    try:
        BP = brickpi3.BrickPi3()
        stored_pass = "chupacabra"
        main()
    except KeyboardInterrupt:
        print("You ended the program.\n")
        sys.exit()
