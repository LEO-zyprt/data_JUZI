import os

myObject = {}

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, "env.txt"),'r') as f:
  for line in f.readlines():
    if '=' in line:
        key, value = line.rstrip("\n").split("=")
        myObject[key] = value

TOKEN = myObject['TOKEN']