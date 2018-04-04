from gtts import gTTS
from pygame import mixer
from random import randrange
import pronouncing
rhymes=pronouncing.rhymes("climbing")
print(rhymes)

mixer.init()

rap=""
file=open("raplines2.txt",'r')
x=file.readlines()
for i in range(0,len(x)):
    x[i]=x[i][0:-1]
start=int(input("Enter the index of first line"))
y=x[start].split()
word1=y[-1].strip('!').strip('"').strip('.').strip('?')
#print(word1)
rhymes=pronouncing.rhymes(word1)
#print(rhymes)
print(x[start])
rap=rap+" "+x[start]+", "
count=1
flag=0
j=0
while count<35:
    j=0
    while j<len(x):
        lines=x[j]
        y=lines.split()
        word1=y[-1].strip('!').strip('"').strip('.').strip('?')
        if count%2==1:
            if word1 in rhymes:
                #print(word1)
                rhymes=pronouncing.rhymes(word1)
                #print(rhymes)
                print(lines)
                rap=rap+" "+lines+", "
                count+=1
                flag=1
                break
        elif count%2==0:
            i=randrange(0,len(x))
            y = x[i].split()
            rap=rap+" "+x[i]+", "
            word1 = y[-1].strip('!').strip('"').strip('.').strip('?')
            rhymes = pronouncing.rhymes(word1)
            print(x[i])
            count+=1
            flag=1
            break

        j+=1
        if j==len(x):
            flag=0
            break
    if flag==0:
        i = randrange(0, len(x))
        y = x[i].split()
        word1 = y[-1].strip('!').strip('"').strip('.').strip('?')
        rhymes = pronouncing.rhymes(word1)
        print(x[i])
        rap = rap + " " + x[i]+", "
        count += 1
        flag=1




#while True:
#    x[start]
print(rap)



#my_tts = "Text you want to process"
tts = gTTS(text=rap, lang='en')
tts.save(str(randrange(1,10000))+".mp3")
