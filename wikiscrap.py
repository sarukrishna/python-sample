#Read the txt file and find the links
#open the each link
#read the content inside the link
#write into a new file
#

import urllib.request
from bs4 import BeautifulSoup
import os
import threading
import time
import shutil
import wikipedia
import re

output_folder = './images'
shutil.rmtree(output_folder, ignore_errors=True)
os.makedirs(output_folder)

def webscrap(filepath):
    filecontent = open(filepath, "r", encoding='utf-8').readlines()
    wikilinks = set()
    for line in filecontent:
        if line.startswith('#'):
            continue
        if line in filecontent:
            wiki = line.split()[-2].strip('<>').split('?')[0]
            #wiki = line
            wikilinks.add(wiki)
    for url in wikilinks:
        filename = url.strip().split("/")[-1].replace('_', ' ')
        t1 = threading.Thread(target=wikiread, args=(filename,))
        t2 = threading.Thread(target=info_box, args=(url,))
        t1.start()
        t2.start()

def wikiread(name):
    try:
        page = wikipedia.page(name)
        content = page.content
        filename = os.path.join(output_folder, name+".txt")
        with open(filename, "w", encoding='utf-8') as f:
            f.write(content)
    except Exception as e:
        print("Exception occured while reading %s" %(e) + str(page.url))

def info_box(url):
    try:
        urlobj = urllib.request.urlopen(url)
        html = urlobj.read()
        soup = BeautifulSoup(html, "lxml")
        table = soup.find('table', {'class' : re.compile("infobox.*")})
        time_string = soup.find('li', id='footer-info-lastmod')
        time_list = time_string.get_text().split(" ")
        modified_date = ' '.join(time_list[7:10])
        print (modified_date)
        tags = ['th', 'td']
        dirname = "images"
        filename = url.strip().split("/")[-1] + "_info.txt"
        filename = os.path.join(dirname, filename)
        for tag in table.findAll(tags):
            paragragph =  tag.get_text()
            with open(filename, "a", encoding='utf-8') as f:
                f.write(paragragph + "\n")
        with open(filename, "a") as f:
            f.write("\n" + time_string.get_text() + "\n")

        urlobj.close()
    except Exception as e:
        print("Exception occured %s" %(e) + str(filename))

if __name__ == "__main__":
    start = time.time()
    webscrap("Sample_Peoples_Data.txt")
    final = time.time()
    total = final - start
    print("total time of execution is " + str(total))