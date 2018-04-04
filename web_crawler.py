from gtts import gTTS
from pygame import mixer
#import bs4.*
import http
import urllib.request
#from bs4 import BeautifulSoup
from bs4 import *
from urllib.request import Request,urlopen
from pprint import *

import re
import xlwt

#convert("$200 million")
file=open('raplines.txt','w')
print("Connecting...")
req = Request('https://www.rappad.co/explore?mod=week&sort=top', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
print("Connected")
#content=urllib.request.urlopen("https://www.rappad.co/explore?mod=week&sort=top");
soup=BeautifulSoup(webpage,"html.parser")
tag=soup.find_all('a',class_="explore-rap-entry")
print(tag[0]['href'])
#book=xlwt.Workbook(encoding="utf-8")
#sheet1 = book.add_sheet("Country Values of World Bank")
#sheet1.write(0, 0, "Country")
#sheet1.write(0, 1, "IBRD/IDA")
count=int(input("enter the start: "))
inc=int(input("Enter the inc: "))
flag=0
hero=input("Enter the star: ")
author="My name is "+hero+". "
#print(soup.get_text)
text_sent=[]
for line in tag[:]:
    story_link="https://www.rappad.co"+line['href']
    req = Request(story_link, headers={'User-Agent': 'Mozilla/5.0'})
    story_page = urlopen(req).read()
    #story_page=urllib.request.urlopen(story_link)
    story = BeautifulSoup(story_page, "html.parser")
    text=story.find_all("div", class_="line")
    print(text)

    for sent in text[:]:
        print(sent.contents[0])
        text_sent.append(sent.contents[0])


for verse in text_sent:
    striped=str(verse).strip('/').strip('"').strip()
    if striped !='':
        file.write(striped+ "\n")

print(text_sent)
file.close()
#mixer.init()

#my_tts = author
#tts = gTTS(text=my_tts, lang='en')
#file_loc="C:\\Users\Karan\Desktop\Karan\RapBot\\"+hero+".mp3"
#tts.save(file_loc)

