from os import system
from time import sleep
import sys
system('title mdrrrrrrrrrrrrrrrrrrrrrr Krystal#6960')
system('mode 120, 100')
count=1
with open('mdr.txt', 'r') as f:
    lines = f.readlines()
while True:
    for line in lines:
        print(line)
        system("color 0"+str(count))
        count = count+1
        if count == 9:
            count =1
        sleep(0.05)
        