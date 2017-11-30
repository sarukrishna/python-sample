#Read the txt file and find the links
#open the each link
#read the content inside the link
#write into a new file
#

import os
import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from bs4.element import Comment
import re

filecontent = open("Sample_Peoples_Data.txt", "r", encoding='utf-8').readlines()
link = "<http://xmlns.com/foaf/0.1/name>"
wikilinks = []
for line in filecontent:
    if line.startswith('#'):
        continue
    if link in line:
        wiki = line.split()[-2].strip('<').split('?')[0]
        wikilinks.append(wiki)

url = urllib.request.urlopen("https://en.wikipedia.org/wiki/Chiranjeevi")
content = url.read()
texts = BeautifulSoup(content, "lxml").findAll("p")
