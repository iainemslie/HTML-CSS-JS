import os, re, shutil
import requests
from bs4 import BeautifulSoup as bs

'''
Deletes unused images from the /images directory
'''

# Get all img files referenced in index.html
HTMLFile = open('index.html', encoding='utf8')

index = HTMLFile.read()

soup = bs(index, features='html.parser')

img_tags = soup.find_all('img')

imgs_used = []
for img in img_tags:
    imgs_used.append(img['src'])

# Copy images used to a new directory
if not os.path.isdir('./img'):
    os.mkdir('./img')

for img in imgs_used:
    shutil.copyfile(img, f'./img/{img.split("/")[1]}')
