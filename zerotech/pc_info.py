import os,sys
from subprocess import Popen,PIPE
import re


sample_bit_lock="""
BitLocker Drive Encryption: Configuration Tool version 10.0.22000
Copyright (C) 2013 Microsoft Corporation. All rights reserved.

Disk volumes that can be protected with
BitLocker Drive Encryption:
Volume C: [OS]
[OS Volume]

    Size:                 930.77 GB
    BitLocker Version:    None
    Conversion Status:    Fully Decrypted
    Percentage Encrypted: 0.0%
    Encryption Method:    None
    Protection Status:    Protection Off
    Lock Status:          Unlocked
    Identification Field: None
    Key Protectors:       None Found


None
"""

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
    serial_number_process=Popen(['wmic','bios','get','serialnumber'],stdout=PIPE)
    serial_number,err=serial_number_process.communicate()
    return serial_number.decode().replace("\r"," ").rstrip().lstrip().split("\n")[1]
  return "Incompatible OS"

def get_bitlock_info():
  if get_os()=="windows":
    bitlock_encrypted=Popen(['manage-bde','-status',"c:"],stdout=PIPE)
    bitlock_encrypted_info,bitlock_encrypted_error=bitlock_encrypted.communicate()

    status=re.findall("Protection Status:.*",bitlock_encrypted_info.decode())
    if(len(status)==0):
      return "NO INFO. ADMIN?"
    if(status[0].split(':')[1].lstrip().rstrip()=="Protection On"):
      return "ON!"
    else:
      return "OFF"
  return "OS not supported."