from tkinter import *
from tkinter import filedialog

root = Tk()
root.title('Notepad')
root.geometry('500x500')



def clear():
    entry_box.delete("1.0", END)

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, 'w') as file:
            file.write(entry_box.get("1.0", END))

def open_file():
    file = filedialog.askopenfile(mode='r',filetypes=[('text files','*.txt')])
    if file is not None:
        data = file.read()
    entry_box.insert(INSERT,data)


lbl = Label(root, text='Notepad', font=('Arial', 15), fg='blue')
lbl.place(x=300, y=0)

clear_btn = Button(root, text='Clear', width=10,command=clear)
clear_btn.place(x=0, y=0)

save_btn = Button(root, text='Save file', width=10, command=save_file)
save_btn.place(x=80, y=0)

open_btn = Button(root, text='Open file', width=10,command=open_file)
open_btn.place(x=160, y=0)

entry_box = Text(root, font=('Arial'),height=55, width=300)
entry_box.place(x=0,y=25)

mainloop()
