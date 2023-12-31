# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "lekha"
    age = "16"
    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/My Father info")
def father_webpage():

# define the route to mother webpage
    @app.route("/My Mother info")
    def mother_webpage():

# define the route to friends webpage
        @app.route("/My Friend info")
        def friend_webpage():

# run the file
            
          if __name__  ==  '__main__':
           app.run(debug=True)
