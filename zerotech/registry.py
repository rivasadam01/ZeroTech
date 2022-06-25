import winreg

def get_reg(hkey,path:str,name:str):
  try:
    if hkey=="HKEY_LOCAL_MACHINE":
      registry=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,path,0,winreg.KEY_READ)
      value,regtype=winreg.QueryValueEx(registry,name)
      winreg.CloseKey(registry)
      return value
  except WindowsError as w:
    print(w)
    
