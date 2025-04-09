#!/usr/bin/env python3

import socket
import sys

password = "chupacabra"
portDic = {"a": 0, "b": 1, "c": 2, "d": 3}

commands = ["in", "out"]
ports = ["a", "b", "c", "d"]

if len(sys.argv) < 3:
    print("Missing argument.")
elif sys.argv[1] in commands:
    if sys.argv[2] in ports:
        cmd = sys.argv[1]
        port = str(sys.argv[2]).lower()
        if port in ["a", "b", "c", "d"]:
            port = portDic[port]
        #add = "193.179.31.173"
        add = "192.168.1.150"

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((add, 9999))
        send_list = "{password},{cmd},{port}".format(password=password, cmd=cmd, port=port)
        client.send(send_list.encode())

        from_server = client.recv(4096)
        answer = from_server.decode()
        print(answer)
        client.close()
    else:
        print("This is an invalid port.")
else:
    print("Please enter a valid command.")
