import os, re
import requests
from bs4 import BeautifulSoup as bs

r = requests.get('https://www.architecturaldigest.com/')
soup = bs(r.content, features='html.parser')

img_tags = soup.find_all("img");

for img_tag in img_tags:
    img_url = img_tag['src']

    if (re.match('^.verso', img_url)):
        pre_string = "https://www.architecturaldigest.com/"
        img_url = os.path.join(pre_string, img_url[1:])
    
    head, img_name = os.path.split(img_url)
    
    img_data = requests.get(img_url).content
    with open(f'ArchitecturalDigest/images/{img_name}', 'wb') as handler:
        handler.write(img_data)




