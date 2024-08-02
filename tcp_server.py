#******************************************************************************
# File Name:   tcp_server.py
#
# Description: A simple "tcp server" for demonstrating TCP usage.
# The server sends LED ON/OFF commands to the connected TCP client
# and receives acknowledgement from the client.
#
#
#******************************************************************************
# Copyright 2019-2024, Cypress Semiconductor Corporation (an Infineon company) or
# an affiliate of Cypress Semiconductor Corporation.  All rights reserved.
#
# This software, including source code, documentation and related
# materials ("Software") is owned by Cypress Semiconductor Corporation
# or one of its affiliates ("Cypress") and is protected by and subject to
# worldwide patent protection (United States and foreign),
# United States copyright laws and international treaty provisions.
# Therefore, you may use this Software only as provided in the license
# agreement accompanying the software package from which you
# obtained this Software ("EULA").
# If no EULA applies, Cypress hereby grants you a personal, non-exclusive,
# non-transferable license to copy, modify, and compile the Software
# source code solely for use in connection with Cypress's
# integrated circuit products.  Any reproduction, modification, translation,
# compilation, or representation of this Software except as specified
# above is prohibited without the express written permission of Cypress.
#
# Disclaimer: THIS SOFTWARE IS PROVIDED AS-IS, WITH NO WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, NONINFRINGEMENT, IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. Cypress
# reserves the right to make changes to the Software without notice. Cypress
# does not assume any liability arising out of the application or use of the
# Software or any product or circuit described in the Software. Cypress does
# not authorize its products for use in any products where a malfunction or
# failure of the Cypress product may reasonably be expected to result in
# significant property damage, injury or death ("High Risk Product"). By
# including Cypress's product in a High Risk Product, the manufacturer
# of such system or application assumes all risk of such use and in doing
# so agrees to indemnify Cypress against all liability.
#******************************************************************************

#!/usr/bin/python

import socket
import optparse
import time
import sys
import threading

host = socket.gethostbyname(socket.gethostname())  # IP address of the TCP server
port = 50007                                       # Arbitrary non-privileged port
RECV_BUFF_SIZE = 4096                              # Receive buffer size
DEFAULT_KEEP_ALIVE = 1                             # TCP Keep Alive: 1 - Enable, 0 - Disable

print("==========================")
print("TCP Server")
print("==========================")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# set TCP Keepalive parameters
s.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, 10)
s.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, 1)
s.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPCNT, 2)
s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, DEFAULT_KEEP_ALIVE)

# variable to identify if there is an active client connection
is_client_connected = False

class KeyboardThread(threading.Thread):

    def __init__(self, input_cbk = None, name='keyboard-input-thread'):
        self.input_cbk = input_cbk
        super(KeyboardThread, self).__init__(name=name)
        self.start()

    def run(self):
        while True:
            self.input_cbk(input()) #waits to get input + Return

def read_user_data(inp):
    #evaluate the keyboard input
    if(is_client_connected == True):
        if(inp == ""):
            print("No option entered!")
            print("Enter your option: '1' to turn ON LED, 0 to turn"\
                            " OFF LED and Press the 'Enter' key: ")
        else:
            conn.send(inp.encode())
    else:
        print("No active client connection. Command not send")

#start the Keyboard thread
kthread = KeyboardThread(read_user_data)

# Bind the socket to host IP address and port
try:
    s.bind((host, port))
    s.listen(1)
except socket.error as msg:
    print("ERROR: ", msg)
    s.close()
    s = None

if s is None:
    sys.exit(1)

while True:    
    try:
        is_client_connected = False;
        print("Listening on: IPv4 Address: %s Port: %d"%(host, port))
        conn, addr = s.accept()
        is_client_connected = True
           
    except KeyboardInterrupt:
        print("Closing Connection")
        s.close()
        s = None
        sys.exit(1)

    print('Incoming connection accepted: ', addr)

    while True:
        try:
            print("Enter your option: '1' to turn ON LED, 0 to turn"\
                        " OFF LED and Press the 'Enter' key: ")
            
            data = conn.recv(RECV_BUFF_SIZE)
            if not data: break
            print("Acknowledgement from TCP Client:", data.decode('utf-8'))
            print("")
            
        except socket.error:
            print("Timeout Error! TCP Client connection closed")
            break
            
        except KeyboardInterrupt:
            print("Closing Connection")
            s.close()
            s = None
            sys.exit(1)    

# [] END OF FILE
