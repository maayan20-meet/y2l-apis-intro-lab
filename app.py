import json
import requests
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

############################
### Lab Part 1: JSON 
############################

@app.route('/movie')
def movies():
    json_string = """
                    {
                    "title" : "Black Panther", 
                    "releaseDate" : "2/16/2018",
                    "image_url": "https://ksassets.timeincuk.net/wp/uploads/sites/55/2018/02/KXC1W2-920x584.jpg"
                    }
                    """

    parsed_json = json.loads(json_string)
    return render_template('movie.html', movie=parsed_json)


@app.route('/tvshows')
def tv_shows():
    json_string = """
    [{
    "url":"http://www.tvmaze.com/shows/2705/narcos",
    "name":"Narcos",
    "language":"English",
    "genres":[  
      "Drama",
      "Crime"
    ]},
    {  
    "url":"http://www.tvmaze.com/shows/305/black-mirror",
    "name":"Black Mirror",
    "language":"English",
    "genres":[  
        "Drama",
        "Science-Fiction",
        "Thriller"
   ]},
   {  
    "url":"http://www.tvmaze.com/shows/305/black-mirror",
    "name":"Black Mirror",
    "type":"Scripted",
    "language":"English",
    "genres":[  
        "Drama",
        "Science-Fiction",
        "Thriller"
    ]
    }]    
    """
    parsed_json = json.loads(json_string)


    return render_template('tv_shows.html', shows=parsed_json)


############################
### Lab Part 2: API requests
############################
@app.route('/dogs')
def dog_breeds():
    """
    If you visit https://dog.ceo/api/breeds/list/all 
    a list of all dog breeds is returned. Try this in your browser! (Chrome/firefox)

    Using the `requests` library (as shown in the slides)
    Do a GET request to the link above to get all dog breeds and return them
    to them as a list to the user as a bullet pointed list
    """

    response = requests.get("https://dog.ceo/api/breeds/list/all")

    parsed_content = json.loads(response.content)

    return render_template('dogs.html', breeds=parsed_content['message'])

@app.route('/dogpic', methods=['GET', 'POST'])
def dogpic():

	if request.method == 'GET':
		return render_template('dogpic.html', pic=0)

	else:

		response = requests.get("https://dog.ceo/api/breed/%s/images/random" % request.form['breed'])
		parsed_content = json.loads(response.content)
		print(parsed_content)

		return render_template('dogpic.html', pic=parsed_content)

if __name__ == '__main__':
    app.run(debug=True)