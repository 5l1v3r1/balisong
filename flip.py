import os
import sys
import socket
import random

W = '\033[1m'
R = '\033[31m'
N = '\033[0m'
G = '\033[32m'
B = '\033[34m'
Y = '\033[33m'

# Code time ##################
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
##############################
 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
os.system("clear")

print R+"exit"
print G+"green"
print R+"red"
print N+"white"
print B+"blue"
print Y+"yellow"

choice = raw_input(N+'what color knife >>>') 

if choice == "green" : print G+"""
 ___________
|___________|____________
 _________(_+___________/
|___________|
"""

if choice == "red" : print R+"""
 ___________
|___________|____________
 _________(_+___________/
|___________|
"""
if choice == "white" : print N+"""
 ___________
|___________|____________
 _________(_+___________/
|___________|
"""
if choice == "blue" : print B+"""
 ___________
|___________|____________
 _________(_+___________/
|___________|
"""
if choice == "yellow" : print Y+"""
 ___________
|___________|____________
 _________(_+___________/
|___________|
"""
if choice == "exit" : sys.exit()

choice = raw_input('type action :#')

if choice == "basic open" : print """
 __________
|          |
| clank!!! |
|__________|
           \
            \
              _
            |\ | _
            || |  _
    _______ || | _
   / | | | \|| |
 _|() () ()||| |
|_|________|||_|
            \/

                              ______________
                             |              |
                             |   smack!!!   |
                             |______________|
                     |       /
 __________        |   |    /
|_|        ||____________
 _|() () ()|+___________/
|_|_|_|_|_|||

"""