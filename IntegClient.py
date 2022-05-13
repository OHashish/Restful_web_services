import requests
from flask import Flask, render_template,request,url_for,redirect
import time

app = Flask(__name__)
#This route takes quote from the html page as input and uses the first web service to search for
#the director and movie.Then, the director name is then sent the second route.
@app.route('/' ,methods=['GET', 'POST'])
def index():
    movie=''
    director=''

    if request.method == 'POST':
        quote=request.form.get("quote_attribute")
        if quote=="": #Check if no quote entered 
            return redirect('/')
        #start=time.time()
        response3= requests.get("http://localhost:9100/service1/quote/"+quote)
        #end=time.time()
        #print((end-start)*1000)
        result=response3.content.decode('utf-8')
        if result!='None': #Check if no quote is found
            result = result.split(',,')
            movie=result[0]
            director=result[1]
            flag=True
        else:
            return redirect('/')

        return render_template('web1.html',movie=movie,director=director)
    
    return render_template('index.html',movie=movie,director=director)

#This route takes director name as input and then uses the second web service to seach for all movies directed
#by the inputted director name
@app.route('/web2/<string:director_name>' ,methods=['GET', 'POST'])
def web2(director_name):
    #start=time.time()
    response= requests.get("http://localhost:9999/two/director/"+director_name)
    #end=time.time()
    #print((end-start)*1000)
    movies=response.content.decode('utf-8')
    movies=movies.split(',,')
    return render_template('web2.html',movies=movies,director_name=director_name)


#This route takes in a a movie title and use the third(external service:YOUTUBE api) to seach for trailers 
#which then it return 3 youtube links
@app.route('/web3/<string:movie_name>' ,methods=['GET', 'POST'])
def web3(movie_name):
    links=[]
    #start=time.time()
    response2= requests.get("http://127.0.0.1:5001/Trailer/"+movie_name+" trailer")
    #end=time.time()
    #print((end-start)*1000)
    items=response2.json().get('items')
    #parse JSON file and get video id then add it to a link
    for item in items:
        id=item['id']
        videoId=id['videoId']
        links.append("https://www.youtube.com/embed/"+videoId)
        
    return render_template('web3.html',links=links)


if __name__=='__main__':
    app.run(debug=True)
