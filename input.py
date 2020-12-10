import os 
from os import environ
a= os.getenv('username')
b= os.environ.get('password')
c= os.environ['middle']
print(a,b,c)
