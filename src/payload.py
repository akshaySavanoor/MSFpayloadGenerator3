from src.genPay import gen
import pyfiglet
import colorama
from colorama import Fore
from termcolor import colored
from pyfiglet import Figlet
from tkinter import *
f=Figlet(font='standard')
print(colored(f.renderText('Payload'),'blue'))
print(colored(f.renderText('Generator'),'red'))
root=Tk()
root.title('Metasploit Payload Generater')
root.geometry("700x400")
# frame = Frame(root, width=800, height=400)
# frame.pack()
# frame.place(anchor='center', relx=0.5, rely=0.5)
# img = ImageTk.PhotoImage(Image.open("backg1.jfif"))
# label = Label(frame, image = img)
# label.pack()
Label(text="Metasploit Payload Generator",font='lucida 25').grid(row=0,column=2,pady=25)
def get_val():
      gen(apk_val.get(),lhost_val.get(),lport_val.get())

apk_label=Label(root,text="Enter payload name",font="courier 15").grid(row=3,column=1)
lhost_label=Label(root,text="Enter LHOST",font="courier 15").grid(row=4,column=1)
lport_label=Label(root,text="Enter LPORT",font="courier 15").grid(row=5,column=1)
apk_val = StringVar()
lhost_val= StringVar()
lport_val = IntVar()

lport_val.set(4444)
apk_entry= Entry(root,textvariable=apk_val).grid(row=3,column=2)
lhost_entry=Entry(root,textvariable=lhost_val).grid(row=4,column=2)
lport_entry=Entry(root,textvariable=lport_val).grid(row=5,column=2)
Button(root,text="Generate",command=get_val).grid(row=7,column=2)
# root.configure(bg='blue')
root.mainloop()
# text=pyfiglet.figlet_format(" website ping")
# print(text)
# a=input("Enter a IP Address :")
# subprocess.call("ping "+ a,shell=True)
