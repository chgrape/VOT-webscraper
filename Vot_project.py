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




from tkinter import *
from tkinter import ttk



def print_text():
    text = entry.get()
    print(text)

root = Tk()
root.title("Vot project")
root.config(bg = 'yellow')
root.geometry("350x275")

style = ttk.Style()
style.theme_use("default")

style.configure('elder.TButton', 
                foreground = "white",
                background = "#003066",
                font =("Arial",18),
                padding=[10,10,10,10])

style.map('elder.TButton', background=[('active', '#004ea5')])

lable = Label(root,text="You must paste the link here!",padx= 40, pady= 20,anchor= "center", font=("Arial", 25),bg='yellow')
lable.pack()



entry = Entry(root,width=50,font=("Arial", 15),justify='center')
entry.pack()

ImageButton = ttk.Button(root, text="Image", command=print_text,style = "elder.TButton")
ImageButton.place(relx=0.2, rely=0.5, anchor='center')
TextButton = ttk.Button(root, text="Text", command=print_text,style = "elder.TButton")
TextButton.place(relx=0.5, rely=0.5, anchor='center') 
LinksButton = ttk.Button(root, text="Links", command=print_text,style = "elder.TButton")
LinksButton.place(relx=0.8, rely=0.5, anchor='center') 

#lable = Label(root,text="When you press the button, image must be download in our website!",padx= 40, pady= 20,anchor= "center", font=("Arial", 20),bg='yellow')
#lable.place()

root.mainloop()
