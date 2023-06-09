import requests # request img from web
import shutil # save img locally
from bs4 import BeautifulSoup # parse html
from tkinter import *
from tkinter import ttk

#check
def is_string_an_url(url_string):
    try:
        res = requests.get(url_string)
        return res
    except:
        print('Not a link')
        return ''

def is_url_image(image_url):
   image_formats = ("image/png", "image/jpeg", "image/jpg")
   r = requests.head(image_url)
   if r.headers["content-type"] in image_formats:
      return True
   return False


#IMAGES:
def download_img(url, file_name):
	#downloads localy
    res = requests.get(url, stream = True)

    if res.status_code == 200:
        with open(file_name,'wb') as f:
            shutil.copyfileobj(res.raw, f)
        print('Image sucessfully Downloaded: ',file_name)
    else:
        print('Image Couldn\'t be retrieved')

def get_img_urls(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    image_data = []

    images = soup.select('img')
    for image in images:
        image_data.append(image.get('src'))
        
    return image_data

def download_all_imgs(url):
    img_urls = get_img_urls(url)
    for img_url in img_urls:
        file_name = img_url.split('/')[-1]
        if(img_url[0] == '/'):
            img_url = url + img_url
        download_img(img_url, file_name)

#TEXT:
def get_text(url):
    #get all text from a webpage
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup.get_text()
    
    
#LINKS:
def get_links(url):
    all_links = []
    
    page = requests.get(url)    
    data = page.text
    soup = BeautifulSoup(data,"html.parser")

    for linktag in soup.find_all('a'):
        link = linktag.get('href')
        
        # check if link is not empty and starts with http
        if(link != None and link[0] == 'h'):
            all_links.append(link)
    
    return all_links


def print_text():
    url = entry.get()
    if is_string_an_url(url) != '':
        print(get_text(url))
  
    
def print_links():
    url = entry.get()
    if is_string_an_url(url) != '':
        print(get_links(url))


def print_image():
    url = entry.get()
    if is_string_an_url(url) != '' and is_url_image(url) == True:
        download_all_imgs(url)
    else:
        print("This is not a image")


root = Tk()
root.title("Vot project")
root.config(bg = 'yellow')
root.geometry("500x500")


style = ttk.Style()
style.theme_use("default")


style.configure('elder.TButton', 
                foreground = "white",
                background = "#003066",
                font =("Arial",18),
                padding=[10,10,10,10])


style.map('elder.TButton', 
          background=[('active', '#004ea5')]
        )


lable = Label(root,text="You must paste the link here!",padx= 40, pady= 20,anchor= "center", font=("Arial", 25),bg='yellow')
lable.pack()


entry = Entry(root,width=50,font=("Arial", 15),justify='center')
entry.pack()

ImageButton = ttk.Button(root, text="Image", command=print_image,style = "elder.TButton")
ImageButton.place(relx=0.2, rely=0.5, anchor='center')

TextButton = ttk.Button(root, text="Text", command=print_text,style = "elder.TButton")
TextButton.place(relx=0.5, rely=0.5, anchor='center') 

LinksButton = ttk.Button(root, text="Links", command=print_links,style = "elder.TButton")
LinksButton.place(relx=0.8, rely=0.5, anchor='center')

#lable = Label(root,text="When you press the button, image must be download in our website!",padx= 40, pady= 20,anchor= "center", font=("Arial", 20),bg='yellow')
#lable.place()

root.mainloop()
