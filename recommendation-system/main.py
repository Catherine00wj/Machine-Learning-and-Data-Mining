from recommendation import *
from flask import Flask, render_template,session,request,url_for
from flask import jsonify
from flask_restful import reqparse
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer)
from flask_cors import CORS
import numpy as np
from download import *


app = Flask(__name__)
CORS(app)

@app.route('/recommendation/<id>', methods=['GET'])
def recommendation(id):
    #print(id)
    try:
        id=int(id)
    except:
        id=id
    #print(type(id))
    if type(id) is not int or id>671 or id <1:
        message = {'message': 'Please input an integer from 1 to 671!'}
        return jsonify(message), 200
    rate_list, id_list, name_list = processing1(id, zz, dicman, dicmovie, nmovie, rating, corr, movie)
    rate_list1=[False]+rate_list
    string1="person "+str(id)+" has rate the movie with movieid:"
    string2=rate_list1[1]
    for i in range(2,len(rate_list1)):
        if i%10==0:
            string2=string2+" "+rate_list1[i]
        else:
            string2 = string2 + " "+rate_list1[i]
    string3="The next 10 movie we recommand for him is:"
    list1=[]
    string4=""
    string5=""
    for i in range(len(id_list)):
        url="https://www.google.com.au/search?q="+name_list[i]
        #url='< a href = "'+url +'" target = "_blank" > '+url+ " < / a >"
        list1.append([id_list[i],name_list[i],url])
        output=download_pic(name_list[i])
        name=name_list[i].strip().replace(" ","")
        name=name.replace(":","")
        string4=string4+'<a href="https://www.imdb.com/find?ref_=nv_sr_fn&q='+name+'" target=blank>'+name+'</a>  '
        if len(output)>0:
            string5=string5+'<img src="'+output[0]+'">      '
        print(output)
    output={}
    output.update({'string1':string1,'list1':list1,'string2':string2,'string3':string3,'string4':string4,'string5':string5})
    #print(string1)
    #print(list1)
    #print(output)
    return jsonify(output), 200
    #print(rate_list1,id_list,name_list)


















if __name__ == "__main__":
    zz, dicman, dicmovie, nmovie, rating, corr, movie = processing()
    app.run()
