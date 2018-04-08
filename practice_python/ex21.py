# Use the BeautifulSoup and requests 
# Python packages to print out a list of all the article titles on the New York Times homepage.


import requests
from bs4 import BeautifulSoup


url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text


# some requests code here for getting r_html 

soup = BeautifulSoup(r_html, "lxml")

open_file = open('file_to_save.txt', 'w')


for story_heading in soup.find_all(class_="story-heading"): 
    if story_heading.a: 
        open_file.write(str(story_heading.a.text.replace("\n\n", " ").encode('utf-8').strip()))
    else: 
        open_file.write(str(story_heading.contents[0].encode('utf-8').strip()))

    open_file.write("\n")

open_file.close()
