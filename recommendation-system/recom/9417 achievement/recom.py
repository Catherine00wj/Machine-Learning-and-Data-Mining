import csv
import numpy as np
print("now processing the model")
dataset=csv.reader(open('./moviedata/movies.csv',encoding='utf-8'))
movie={}
kk=0
for row in dataset:
    if kk==0:
        kk=kk+1
        continue
    za=row[0]
    zb=row[1]
    movie[za]=zb
dataset=csv.reader(open('./moviedata/ratings.csv',encoding='utf-8'))
nmovie=0
nman=0
kk=0
dicman={}
dicmovie={}
for row in dataset:
    if kk==0:
        kk=kk+1
        continue
    if row[0] not in dicman:
        dicman[row[0]]=nman
        nman=nman+1
    if row[1] not in dicmovie:
        dicmovie[row[1]]=nmovie
        nmovie=nmovie+1
rating=[[0 for i in range(nmovie)] for j in range(nman)]

kk=0
dataset=csv.reader(open('./moviedata/ratings.csv',encoding='utf-8'))
zz=[[] for i in range(nman)]
for row in dataset:
    if kk==0:
        kk=kk+1
        continue
    za=dicman[row[0]]
    zb=dicmovie[row[1]]
    dd=float(row[2])
    rating[za][zb]=dd
    zz[za].append(zb)
rating=np.array(rating)
corr=np.corrcoef(rating,rowvar=0)
corr=0.5+corr*0.5

newman= {v:k for k,v in dicman.items()}
newmovie= {v:k for k,v in dicmovie.items()}
print("model completed!,input your id")
per=input()
# print(dicmovie)
while int(per)!=-100:
    person=dicman[per]
    now={}
    hasrate=[]
    for i in range(nmovie):
        s=0
        if rating[person][i]!=0:
            hasrate.append(i)
        else:
            for j in range(len(zz[person])):
                s=s+rating[person][zz[person][j]]*corr[i][zz[person][j]]
        now[i]=s

    k=sorted(now.items(), key=lambda item: item[1], reverse=True)
    print('person '+str(per)+' has rate the movie with movieid: ')

    for i in range(len(hasrate)):
        print(newmovie[hasrate[i]],end='  ')
    print()
    print('The next 10 movie we recommand for him is: ')
    for i in range(min(10,len(k))):
        print('id:  '+newmovie[k[i][0]],'      /////////name:   '+movie[newmovie[k[i][0]]])
    print()
    print("input -100 to finish recommand or input another person id")
    per=input()






