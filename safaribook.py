from bs4 import BeautifulSoup
import requests
import shutil
import os
import youtube_dl
url = 'https://www.safaribooksonline.com/library/view/python-beyond-the/9781771373609'
domain = 'https://www.safaribooksonline.com'
output_folder = './output'
#username = 'username'
#password = 'SuperSecretPassword'

req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

lessons = soup.find_all('li', class_='toc-level-1')
print(len(lessons))

def downloadvideo(url, folder):
    ydl_opts = {'outtmpl' : folder}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

shutil.rmtree(output_folder, ignore_errors=True)
os.makedirs(output_folder)
module_name = 'Module 0'
#f = open(output_folder + '/' + "safariurl.txt", "a")
for lesson in lessons:
    lesson_name = lesson.a.text
    if lesson_name.startswith('Module') and not 'Summary' in lesson_name:
        module_name = lesson_name
        os.makedirs(output_folder + '/' + module_name)
        # print(module_name)
        for index, video in enumerate(lesson.ol.find_all('a')):
            video_name = str(index) + ' - ' + video.text
            video_url = domain + video.get('href')
            video_out = output_folder + '/' + module_name + '/' + video_name + '.mp4'
            downloadvideo(video_url, video_out)

    else:
        os.makedirs(output_folder + '/' + module_name + '/' + lesson_name)
        for index, video in enumerate(lesson.ol.find_all('a')):
            video_name = str(index) + ' - ' + video.text
            video_url = domain + video.get('href')
            video_out = output_folder + '/' + module_name + '/' + lesson_name + '/' + video_name + '.mp4'
            downloadvideo(video_url, video_out)

			
