import math
import os,sys
from subprocess import Popen,PIPE
import re
from typing import Callable

class NoSupportedOs(Exception):
  ''''''


def get_os():
  os_type=sys.platform.lower()
  if 'win' in os_type:
    return "windows"
  if 'darwin' in os_type:
    return "mac"
  if 'linux' in os_type:
    return "linux"

def get_serial_number():
  if get_os() =="windows":
    serial_number_process=Popen(['wmic','bios','get','serialnumber'],stdout=PIPE,shell=True)
    serial_number,err=serial_number_process.communicate()
    return serial_number.decode().replace("\r"," ").rstrip().lstrip().split("\n")[1]
  return "Incompatible OS"

def get_bitlock_info(callback:Callable=lambda b:...):
  if get_os()=="windows":
    bitlock_encrypted=Popen(['manage-bde','-status',"c:"],stdout=PIPE)
    bitlock_encrypted_info,bitlock_encrypted_error=bitlock_encrypted.communicate()

    status=re.findall("Protection Status:.*",bitlock_encrypted_info.decode())
    if(len(status)==0):
      callback("NO INFO. ADMIN?")
      return "NO INFO. ADMIN?"
    if(status[0].split(':')[1].lstrip().rstrip()=="Protection On"):
      callback("ON!")
      return "ON!"
    else:
      callback("OFF")
      return "OFF"
  
  callback("Os not supported.")
  return "OS not supported."

def get_bitlock_recovery_key():
  # To be implemented
  ...

def get_user_size(callback:Callable=lambda u:...):
  user_dir=""
  if get_os()=="windows":
    user_dir='c:\\Users'
    print(user_dir)
  else:
    raise NoSupportedOs
  dir_size_process=Popen(['dir','/s',user_dir],stdout=PIPE,stderr=PIPE,shell=True)
  dir_size_output,dir_size_error=dir_size_process.communicate()
  result=round(float(dir_size_output.decode().strip().split('Total Files Listed:')[1]\
      .lstrip().rstrip().split('bytes')[0].split('File(s)')[1].lstrip().rstrip()\
      .replace(',',""))/math.pow(1024,3),3)
  
  callback(result)

  return f"{result}GB"
