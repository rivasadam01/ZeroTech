import tkinter as tk
from tkinter import filedialog
from zerotech import pc_info
from threading import Thread

root=tk.Tk()
root.title("ZeroTech")
root.minsize(width=600,height=500)

text_font=("Helvetica",15)

company_info=tk.Label(root,text="0development")
company_info.place(relx=0.5,rely=0.95,anchor="n")

pc_serial_label=tk.Label(root)
pc_serial_label.config(font=text_font)
pc_serial_label.place(relx=0.05,rely=0.05)

pc_bitlock_active_label=tk.Label(root,text="Bitlocker: Getting status...")
pc_bitlock_active_label.config(font=text_font,fg="gray")
pc_bitlock_active_label.place(relx=0.05,rely=0.10)

pc_bitlock_recovery_key=tk.Label(root,text="Bitlocker Recovery key: NOT YET IMPLEMENTED")
pc_bitlock_recovery_key.config(font=text_font,fg="gray")
pc_bitlock_recovery_key.place(relx=0.05,rely=0.15)

estimated_user_data_usage_label=tk.Label(root,text="User Data Size: Calculating....")
estimated_user_data_usage_label.config(font=text_font,fg="gray")
estimated_user_data_usage_label.place(relx=0.05,rely=0.20)

def save_info(*labels):
  file_name=filedialog.asksaveasfilename(title="Save PC Info",initialdir=".",filetypes=(("Text File","*.txt"),))
  if file_name=="":
    return
  final_text=""
  for label in labels:
    final_text+=f"{label['text']}\n"
  with open(f"{file_name}.txt","w") as f:
    f.write(final_text)


button_save_info=tk.Button(root)
button_save_info.config(font=text_font,text="Save PC Info",
  command=lambda:save_info(pc_serial_label,pc_bitlock_active_label,
  estimated_user_data_usage_label))
button_save_info.place(relx=0.05,rely=0.30)

def user_data_usage_callback(usage):
  estimated_user_data_usage_label['text']=f"User Data Size: {usage}GB"
  estimated_user_data_usage_label.config(fg="black")

def bitlocker_active_callback(status):
  pc_bitlock_active_label['text']=f"Bitlocker: {status}"
  if(status=="ON!"):
    pc_bitlock_active_label.config(fg="red")
  else:
    pc_bitlock_active_label.config(fg="black")

pc_serial_label['text']=f"Serial: {pc_info.get_serial_number()}"

bitlocker_active_thread=Thread(target=pc_info.get_bitlock_info,args=[bitlocker_active_callback])
bitlocker_active_thread.start()

user_data_usage_thread=Thread(target=pc_info.get_user_size,args=[user_data_usage_callback])
user_data_usage_thread.start()
