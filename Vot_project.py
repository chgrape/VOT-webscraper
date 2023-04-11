#from tkinter import *
#import tkinter as tk

#root = tk.Tk()

#root.title("Vot project")

#label1 = tk.Label(root, text= "Paste the link in the box!",font=('Arial',18))

#textbox = tk.Text(root,height=1, font=('Arial',20))
#textbox.pack(padx=20)

#def myClick():
    #label2 = Label(root,text="You clicked a button")
    #label2.pack()


#button = Button(root,text= "Download",padx= 50,pady= 30,command=myClick)
#button.pack()


#root.mainloop()


import tkinter as tk

def print_text():
    text = entry.get()
    print(text)

root = tk.Tk()
root.title("Vot project")
root.config(bg = 'yellow')


lable = tk.Label(root,text="You must paste the link here!",padx= 40, pady= 20,anchor= "center", font=("Arial", 25),bg='yellow')
lable.pack()



entry = tk.Entry(root,width=50,font=("Arial", 15),justify='center')
entry.pack(padx=10, pady=10)

button = tk.Button(root, text="Print Text", command=print_text,padx= 20,pady=10)
button.pack()

lable = tk.Label(root,text="When you press the button, image must be download in our website!",padx= 40, pady= 20,anchor= "center", font=("Arial", 20),bg='yellow')
lable.pack()

root.mainloop()
