#Download the webpage
#read the contents
#get the list of links from the content
#for each link in links
#    open the link
#    read the link
#    get the image file from the link
#    download the image file into a folder 
#extract the links from each link
	#check if the link is already visited or not 
	#download images from each link

import os
import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import logging

base_url = "http://www.rgukt.in/"
base_dir = "images"
to_visit = set((base_url,))
visited = set()
while to_visit:
    #open and read the content from each link
    current_page = to_visit.pop()
    visited.add(current_page)
    content = urllib.request.urlopen(current_page).read()
    for link in BeautifulSoup(content, "lxml").findAll("a"):
        absolute_url = urljoin(current_page, link["href"])
        if absolute_url not in visited:
	        to_visit.add(absolute_url)
        else:
            print("Already visited... ", absolute_url)
    for img in BeautifulSoup(content, "lxml").findAll("img"):
        imag_link = urljoin(current_page, img["src"])
        print("Downloading the image .....", imag_link)
        imag_name = imag_link.split("/")[-1]
        urllib.request.urlretrieve(imag_link, os.path.join(base_dir, imag_name))
	


