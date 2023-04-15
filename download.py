import requests # request img from web
import shutil # save img locally
from bs4 import BeautifulSoup # parse html

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
        download_img(img_url, file_name)


#TEXT:
def get_text(url):
    #get all text from a webpage
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup.get_text()
    
    
    # Print the body content in list form
    # print(soup.body.contents[0])
    # Print the first found div on html page
    # print(soup.find('div'))
    # Print the all divs on html page in list form
    # print(soup.find_all('div'))
    # Print the element with 'required_element_id' id
    # print(soup.find(id='required_element_id'))
    # Print the all html elements in list form that matches the selectors
    # print(soup.select(required_css_selectors))
    # Print the attribute value in list form
    # print(soup.find(id='someid').get("attribute-name"))
    # You can also break your one large query into multiple queries
    # parent = soup.find(id='someid')
    # getText() return the text between opening and closing tag
    # print(parent.select(".some-class")[0].getText())

    
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
