import os, re
import requests
from bs4 import BeautifulSoup as bs

"""
Gets all the image tags from AD and downloads the href image
Some image paths are relative so we prepend them
"""

r = requests.get('https://www.fosterandpartners.com/')
soup = bs(r.content, features='html.parser')

img_tags = soup.find_all("img");


for img_tag in img_tags:
    img_url = img_tag['src']

    head, img_name = os.path.split(img_url)

    img_name = img_name.split('&')[0]

    print(img_name)
    
    img_data = requests.get(img_url).content
    with open(f'Foster+Partners/images/{img_name}', 'wb') as handler:
        handler.write(img_data)




