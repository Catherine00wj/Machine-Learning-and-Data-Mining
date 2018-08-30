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
    kk=kk+1
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
    kk=kk+1
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

# print(dicmovie)
error1=[]
for tft in range(nman):
    person=tft
    now={}
    hasrate=[]
    for i in range(nmovie):
        s=0
        ratenow=0
        if rating[person][i]!=0:
            hasrate.append(i)
            for j in range(len(zz[person])):
                s=s+rating[person][zz[person][j]]*corr[i][zz[person][j]]
                ratenow=ratenow+corr[i][zz[person][j]]

            now[i]=s/ratenow

    error=0
    total=0
    for i in range(len(hasrate)):
        for j in range(i+1,len(hasrate)):
            # print(rating[person][hasrate[j]])
            total=total+1
            if (rating[person][hasrate[i]]-rating[person][hasrate[j]])*(now[hasrate[i]]-now[hasrate[j]])<0:
                error=error+1
    print(tft,"       error rate=",error/total)
    error1.append(error/total)
    # k=sorted(now.items(), key=lambda item: item[1], reverse=True)
    # print('person '+str(per)+' has rate the movie with movieid: ')
    #
    # for i in range(len(hasrate)):
    #     print(newmovie[hasrate[i]],end='  ')
    # print()
    # print('The next 10 movie we recommand for him is: ')
    # for i in range(min(10,len(k))):
    #     print('id:  '+newmovie[k[i][0]],'      /////////name:   '+movie[newmovie[k[i][0]]])
    # print()
    # print("input -100 to finish recommand or input another person id")
    # per=input()

file=open("errorrate.txt",'w')
for i in range(len(error1)):
    file.write(str(error1[i])+'\n')




