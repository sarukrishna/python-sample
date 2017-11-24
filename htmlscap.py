#Download the webpage
#read the contents
#get the list of links from the content
#for each link in links
#    open the link
#    read the link
#    get the image file from the link
#    download the image file into a folder 
import os
import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import logging

logging.baseContex
base_url = "https://apod.nasa.gov/apod/archivepix.html"
base_dir = "images"
content = urllib.request.urlopen(base_url).read()
links = BeautifulSoup(content, 'lxml').findAll("a")
for link in links:
    print("follwing link " + str(link))
    link_url = urljoin(base_url, link["href"])
    content = urllib.request.urlopen(link_url).read()
    images = BeautifulSoup(content, 'lxml').findAll("img")
    for img in images:
        image_url = urljoin(link_url, img["src"])
        image_name = image_url.split('/')[-1]
        print("Downloading the image " + image_url)
        urllib.request.urlretrieve(image_url, os.path.join(base_dir, image_name))
		
		
    




