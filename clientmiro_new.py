#!/usr/bin/env python3

import socket
import sys
import json
import argparse

parser = argparse.ArgumentParser(description=
"""You can send commmands to a TI-LFA robot using this program.""")
parser.add_argument('--pass', type=str, default="chupacabra", dest="password",
    help="Password to gain acces to the robot. (default: chupacabra)")

parser.add_argument('-i', action='store_true', default=False, dest="cmd_in",
    help="set command to in (default: out)")
parser.add_argument('-o', action='store_false', default=False, dest="cmd_in",
    help="set command to out (default: out)")

parser.add_argument('-s', action="store_true", default=False, dest="status",
    help="Find out the current status of all the motors.")


parser.add_argument('-p', default="a", dest="port",
    help="On what port is the motor. You can choose out of these options: a, b, c, d. (default: a)")

args = parser.parse_args()

cmd = 'in' if args.cmd_in else 'out'
cmd = 'status' if args.status else cmd

password = args.password
portDic = {"a": 0, "b": 1, "c": 2, "d": 3}

commands = ["in", "out", "status"]
ports = ["a", "b", "c", "d"]

if cmd in commands:
    if args.port in ports:
        cmd = cmd
        port = str(args.port).lower()
        if port in ["a", "b", "c", "d"]:
            port = portDic[port]
        #add = "193.179.31.173"
        add = "192.168.1.150"

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((add, 9999))
        send_json = json.dumps([password, cmd, port])
        client.send(send_json.encode())

        from_server = client.recv(4096)
        answer = from_server.decode()
        print(answer)
        client.close()
    else:
        print("This is an invalid port.")
else:
    print("Please enter a valid command.")
