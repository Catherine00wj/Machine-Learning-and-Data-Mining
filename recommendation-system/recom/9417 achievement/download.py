# -*- coding: utf-8 -*-
import urllib
import re
import urllib.request
import os


def getHtml(url):
    request = url
    response = urllib.request.urlopen(request)
    return response.read()


def trimempty(n):
    return len(n) > 12


def download_pic(name):
    url = 'https://www.imdb.com/find?ref_=nv_sr_fn&q='
    name=name.strip().replace(" ","")
    url=url+name
    print(url)
    data = getHtml(url)
    # imgs= re.findall(r'<a\s+.*href=\'([^\']*)\'\s+.*>.*<\/a>',data)
    #print(type(data))
    data=str(data, encoding = "utf-8")
    #print(data)
    imgs = re.findall(r'<img\s+.*src=\"([^\"]*)\"\s+.*>', data)
    if len(imgs) > 50:
        imgs = imgs[0:50]
    else:
        imgs = imgs

    imgs = filter(trimempty, imgs)
    #print(imgs)
    index = 0
    name=name.replace(":","")
    folder = os.getcwd()+'/img/'+name
    print(folder)
    if not os.path.exists(folder):
        os.makedirs(folder)
    output=[]
    for i in imgs:
        extArr = re.findall(r'.*\.(\w+)$', i)
        if (len(extArr) > 0):
            ext = extArr[0]
        else:
            ext = 'jpg'
        path = './img/'+name+'/%s.%s' % (index, ext)
        print(path)
        f = open(path, 'wb')
        #print(type(getHtml(i)))
        #string1=str(getHtml(i), encoding = "utf-8")
        f.write(getHtml(i))
        f.close()
        if index==1:
            output.append(path)
        index = index + 1
    return output

#download_pic('Unforgiven(1992)')