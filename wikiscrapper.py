#Read the txt file and find the links
#open the each link
#read the content inside the link
#write into a new file
#

import urllib.request
from bs4 import BeautifulSoup
import os

def webscrap(filepath):
    filecontent = open(filepath, "r", encoding='utf-8').readlines()
    link = "<http://xmlns.com/foaf/0.1/name>"
    wikilinks = set()
    for line in filecontent:
        if line.startswith('#'):
            continue
        if link in line:
            wiki = line.split()[-2].strip('<').split('?')[0]
            wikilinks.add(wiki)
    for url in wikilinks:
        crawl(url)
    filecontent.close()        

def crawl(url):
    urlobj = urllib.request.urlopen(url)
    html = urlobj.read()
    tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'p', 'li']
    soup = BeautifulSoup(html, "lxml")
    dirname = "images"
    filename = url.split("/")[-1] + ".txt"
    filename = os.path.join(dirname, filename)
    for tag in soup.findAll(tags):
        paragragph =  tag.get_text()
        with open(filename, "a", encoding='utf-8') as f:
            f.write(paragragph + "\n\n")
    urlobj.close()
if __name__ == "__main__":
    webscrap("Sample_Peoples_Data.txt")
    
    
	