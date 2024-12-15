from tkinter import *

root = Tk()

def volumeUp():
    print("Volume Increase +1")

def volumeDown():
    print('Volume Decrease -1')

def turnOnTV():
    window = Toplevel(root)
    window.title("TV")
    pika = PhotoImage(file="pic1.gif")

    original_image = Label(window, image=pika)
    original_image.image = pika
    original_image.pack()





turn_on = Button(root, text="ON", command=turnOnTV)
turn_on.pack()

turn_off = Button(root, text="OFF", command=root.quit)
turn_off.pack()

volume = Label(root, text="VOLUME")
volume.pack()

vol_up = Button(root, text="+", command=volumeUp)
vol_up.pack()

vol_down = Button(root, text="-", command=volumeDown)
vol_down.pack()

root.mainloop()