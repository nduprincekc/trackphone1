import tkinter as tk
from tkinter import *
import phonenumbers

from phonenumbers import geodata, geocoder, carrier

root = tk.Tk()
root.geometry('300x400')
root.title('phone number tracker')


# code for clearing the textarea and entry_box
def clear():
    ent_1.delete(0, END)
    tex_area1.delete(1.0, END)


def check():
    ch = phonenumbers.parse(ent_1, 'EN')
    p = (geocoder.description_for_number(ch, 'eo'))
    print(len(p))
    service_name = phonenumbers.parse(ent_1, 'we')
    tex_area1.get(carrier.name_for_number(service_name, 'ru'))


lab_1 = Label(root, text='ENTER THE PHONE NUMBER(+...) ', bg='red', fg='white')
lab_1.place(x=44, y=10)

# entry for inputing the phone number
ent_1 = Entry(root)
ent_1.place(x=55, y=40)

# text_area for showing the information required
tex_area1 = Text(root, height=10, width=20)
tex_area1.place(x=55, y=125)

lab_1 = Label(root, text='THE INFORMATION WILL BE DISPLAY BELOW: ', bg='red', fg='white')
lab_1.place(x=44, y=100)

# CLEAR BUTTON
cle_1 = Button(root, text='clear', bg='blue', fg='whitesmoke', command=clear)
cle_1.place(x=44, y=310)

# exit BUTTON
exit_1 = Button(root, text='Exit', bg='blue', fg='whitesmoke')
exit_1.place(x=84, y=310)

# Check BUTTON
chk_1 = Button(root, text='Check', bg='blue', fg='whitesmoke', command=check)
chk_1.place(x=124, y=310)

root.mainloop()
