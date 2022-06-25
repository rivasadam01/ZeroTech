import tkinter as tk
import zerotech.pc_info

root=tk.Tk()
root.title("ZeroTech")
root.minsize(width=600,height=500)

text_font=("Helvetica",15)

company_info=tk.Label(root,text="0development")
company_info.place(relx=0.5,rely=0.95,anchor="n")

pc_serial_label=tk.Label(root)
pc_serial_label.config(font=text_font)
pc_serial_label.place(relx=0.05,rely=0.05)

pc_bitlock_active=tk.Label(root)
pc_bitlock_active.config(font=text_font)
pc_bitlock_active.place(relx=0.05,rely=0.10)

pc_serial_label['text']=f"Serial: {zerotech.pc_info.get_serial_number()}"
pc_bitlock_active['text']=f"Bitlocker: {zerotech.pc_info.get_bitlock_info()}"