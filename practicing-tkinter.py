from tkinter import *

root = Tk() # create a root widget
root.title('Basic GUI Layout')
root.maxsize(900,600)
root.configure(background="white")

# Create Frame widget
left_frame = Frame(root, width=200, height=400, bg='grey')
left_frame.grid(row=0, column=0, padx=10, pady=5)

right_frame = Frame(root, width=650, height=400, bg='grey')
right_frame.grid(row=0, column=1, padx=10, pady=5)

# Create frames + labels in left_frame
Label(left_frame, text="original image").grid(row=0, column=0, padx=5, pady=5)

# load image to be "edited"
image = PhotoImage(file="./images/pic1.gif")
original_image = image.subsample(3,3) # resize image using "subsampple"
Label(left_frame, image=original_image).grid(row=1, column=0, padx=5, pady=5)

# Display image in right_frame
Label(right_frame, image=image).grid(row=0,column=0, padx=5, pady=5)

#Create tool bar frame
tool_bar = Frame(left_frame, width=180, height=185)
tool_bar.grid(row=2, column=0, padx=5, pady=5)

# example labels that serve as placeholders for other widgets
Label(tool_bar, text="Tools", relief=RAISED).grid(row=0, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
Label(tool_bar, text="Filters", relief=RAISED).grid(row=0, column=1, padx=5, pady=3, ipadx=10)

# example labels that could be displayed under the "Tool" menu
Label(tool_bar, text="Select").grid(row=1, column=0, padx=5, pady=5)
Label(tool_bar, text="Crop").grid(row=2, column=0, padx=5, pady=5)
Label(tool_bar, text="Rotate & Flip").grid(row=3, column=0, padx=5, pady=5)
Label(tool_bar, text="Resize").grid(row=4, column=0, padx=5, pady=5)
Label(tool_bar, text="Exposure").grid(row=5, column=0, padx=5, pady=5)


root.mainloop()
