import os 
from os import environ
a= os.getenv('username')
b= os.environ.get('password')
c= os.environ.get('middle')
print(a,b,c)
print(os.environ)
print(os.getenv('username'))
