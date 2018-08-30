import csv
import numpy as np


def processing():
    print("now processing the model")
    dataset = csv.reader(open('./moviedata/movies.csv', encoding='utf-8'))
    movie = {}
    kk = 0
    for row in dataset:
        if kk == 0:
            kk = kk + 1
            continue
        za = row[0]
        zb = row[1]
        movie[za] = zb
    dataset = csv.reader(open('./moviedata/ratings.csv', encoding='utf-8'))
    nmovie = 0
    nman = 0
    kk = 0
    dicman = {}
    dicmovie = {}
    for row in dataset:
        if kk == 0:
            kk = kk + 1
            continue
        if row[0] not in dicman:
            dicman[row[0]] = nman
            nman = nman + 1
        if row[1] not in dicmovie:
            dicmovie[row[1]] = nmovie
            nmovie = nmovie + 1
    rating = [[0 for i in range(nmovie)] for j in range(nman)]

    kk = 0
    dataset = csv.reader(open('./moviedata/ratings.csv', encoding='utf-8'))
    zz = [[] for i in range(nman)]
    for row in dataset:
        if kk == 0:
            kk = kk + 1
            continue
        za = dicman[row[0]]
        zb = dicmovie[row[1]]
        dd = float(row[2])
        rating[za][zb] = dd
        zz[za].append(zb)
    rating = np.array(rating)
    corr = np.corrcoef(rating, rowvar=0)
    corr = 0.5 + corr * 0.5
    return zz,dicman,dicmovie,nmovie,rating,corr,movie



def processing1(input,zz,dicman,dicmovie,nmovie,rating,corr,movie):
    newman = {v: k for k, v in dicman.items()}
    newmovie = {v: k for k, v in dicmovie.items()}
    #print("model completed!,input your id")
    per = str(input)
    # print(dicmovie)
    #while int(per) != -100:
    #print(dicman)
    person = dicman[per]
    now = {}
    hasrate = []
    for i in range(nmovie):
        s=0
        ratenow = 0
        if rating[person][i]!=0:
            hasrate.append(i)
        else:
            for j in range(len(zz[person])):
                s=s+rating[person][zz[person][j]]*corr[i][zz[person][j]]
                ratenow=ratenow+corr[i][zz[person][j]]
        if ratenow!=0:
            now[i]=s/ratenow
        else:
            now[i]=0
    k = sorted(now.items(), key=lambda item: item[1], reverse=True)
    print('person ' + str(per) + ' has rate the movie with movieid: ')
    rate_list=[]
    for i in range(len(hasrate)):
        print(newmovie[hasrate[i]], end='  ')
        rate_list.append(newmovie[hasrate[i]])
    print()
    print('The next 10 movie we recommand for him is: ')
    id_list=[]
    name_list=[]
    for i in range(min(10, len(k))):
        print('id:  ' + newmovie[k[i][0]], '      /////////name:   ' + movie[newmovie[k[i][0]]])
        id_list.append('id is '+newmovie[k[i][0]]+' and expected rating is '+str(round(k[i][1],3)))
        name_list.append(movie[newmovie[k[i][0]]])
    print()
    print("input -100 to finish recommand or input another person id")
    #per = input()
    return rate_list,id_list,name_list


#zz,dicman,dicmovie,nmovie,rating,corr,movie=processing()

print('-------------')
#processing1(2,zz,dicman,dicmovie,nmovie,rating,corr,movie)
print('-------------')
#processing1(3,zz,dicman,dicmovie,nmovie,rating,corr,movie)