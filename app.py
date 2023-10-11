from flask import Flask, render_template,request 
from flask import Flask, render_template, request
from flask import Flask, render_template
import matplotlib.pyplot as plt
import matplotlib
from io import BytesIO
matplotlib.use('Agg')
import networkx as nx 
from flask import *


 
app = Flask(__name__)

@app.route('/')
def gg():
    return render_template("index.html")

@app.route('/equ5',methods = ['POST','GET'])
def index():
   
    FielName="csvv.txt"
    Graphtype=nx.DiGraph()   

   
    G = nx.read_edgelist(
        FielName, 
        create_using=Graphtype,
        nodetype=int,
        data=(('weight',float),)
    )

   
    for x in G.nodes():
        print(
            "Node: ", x, " has total #degree: ",G.degree(x),
            " , In_degree: ", G.out_degree(x),
            " and out_degree: ", G.in_degree(x)
        )

    
    for u,v in G.edges():
        print ("Weight of Edge ("+str(u)+","+str(v)+")", G.get_edge_data(u,v))
        
    
    nx.draw(G,with_labels=True)

    img = BytesIO()  
    plt.savefig(img)  
    plt.savefig("static/img.jpg")
    return render_template('indexx.html')


@app.route("/", methods=['POST'])
 
 
@app.route('/helpp',methods=['POST'])
def my_form():
    temp =  request.form.get("text")
    

    try:
        with open('csvv.txt', 'w') as gfg:
            gfg.write(temp)
    except Exception as e:
        print("There is a Problem", str(e))
    return render_template("help.html")

@app.route('/equ3')
def mmy_form():
    return render_template("help.html")

     

    

@app.route(('/home'))
def home():    
    return render_template("index.html")
 

@app.route(("/equ"),methods = ['POST','GET'])
def equ():   
    anss=""
    return render_template("index.html",name = anss)        


@app.route(("/equ2"),methods = ['POST','GET'])
def equ2():   
    import random
    import numpy as np

    output = request.form.to_dict()
    arg0 = int(output["arg0"])
     
    nodes=arg0
    G = nx.complete_graph(nodes)
    nx.draw(G)

    img = BytesIO() # file-like object for the image
    plt.savefig(img) # save the image to the stream
    plt.savefig("static/img.jpg")
    # img.seek(0) # writing moved the cursor to the end of the file, reset
    # plt.switch_backend('agg')
    plt.clf() # clear pyplot
    del nodes
    del img
    del G
    # session.clear()    
    
    
    return render_template("indexx.html")        

@app.route(("/equ3"),methods = ['POST','GET'])
def equ3():   
    
    return render_template("help.html")    

@app.route(("/equ4"),methods = ['POST','GET'])
def equ4():   
    import random
    import numpy as np

    return render_template("index.html")        


if __name__ == '__main__':
    host_name = 'localhost'
    port_num = 5000
    app.run(debug=True, host=host_name, port=port_num)
