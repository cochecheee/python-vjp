from flask import Flask, render_template
import requests
from datetime import datetime
from post import Post

app = Flask(__name__)
endpoint  = "https://gist.githubusercontent.com/cochecheee/1d0c69cc1693de8cbe26f7cf9928868c/raw/40bdb39af00cf1c9f01db569cf5765857b00413f/data.json"
# act as a clent: get data from external server
try:
    response = requests.get(endpoint)
    # print(response.json())  # or response.text
    data = response.json() 
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
    data = []
except Exception as err:
    print(f"An error occurred: {err}")
    data = []
posts = [Post(item) for item in data]

# act as a server: make route for our server when client sent request
@app.route('/')
def get_template():
    year = datetime.now().year
    return render_template('index.html',year=year,all_post=posts)

@app.route('/about')
def about():
    year = datetime.now().year
    return render_template('about.html',year=year)

@app.route('/contact')
def contact():
    year = datetime.now().year
    return render_template('contact.html',year=year)

@app.route("/post/<int:id>")
def post(id):
    for post in posts:
        if post.id == id:
            blog_post = post
    return render_template('post.html', post = blog_post)

if __name__ == '__main__':
    app.run(debug=True)