from tkinter import *
import customtkinter as tk
tk.set_appearance_mode("dark")
tk.set_default_color_theme("green")

root = tk.CTk()
root.geometry("500*350")
root.title("FLAMES")


def name():
    x = list(M.get())
    y = list(N.get())
    if len(x) > len(y):
        return common(x,y)
    else:
        return common(y,x)
        
def common(x,y):
    for i in x[:]:
        if i in y:
            x.remove(i)
            y.remove(i)
    for j in y:
        x.append(j)
    if len(x)==0:
        pass
    else:    
        return relationship(len(x))

def relationship(x):
    flames = {0:"Friends",1:"Lovers",2:"Admirers",3:"Marriage",4:"Enemies",5:"Secret lovers"}
    m = x % 6
    re = flames[m]
    label1.configure(text=re)

M = StringVar()
N = StringVar()

##Created by AbinC7

frame = tk.CTkFrame(master = root)
frame.pack(pady= 20, padx= 60, fill="both", expand= True)

label = tk.CTkLabel(master= frame, text= "FLAMES",font=("Roboto",24))
label.pack(pady =12, padx =10)

label3 = tk.CTkLabel(master= frame, text= "Your name :",font=("Roboto",12))
label3.pack(pady =4, padx =2)


entry1 = tk.CTkEntry(master = frame, placeholder_text="Your name",textvariable = M)
entry1.pack(pady =12, padx =10)

label4 = tk.CTkLabel(master= frame, text= "Crush's name :",font=("Roboto",12))
label4.pack(pady =4, padx =2)

entry2 = tk.CTkEntry(master = frame, placeholder_text="Crush's name",textvariable = N)
entry2.pack(pady =12, padx =10)

button = tk.CTkButton(master = frame, text= "Let's Find", command= name)
button.pack(pady =12, padx =10)

label1 = tk.CTkLabel(master= frame,text="",font=("Roboto",15))
label1.pack(pady =12, padx =10)

if __name__=='__main__':
    root.mainloop()
    