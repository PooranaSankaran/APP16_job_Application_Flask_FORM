# To do Flask web application we need two main directoryy
#static (if you have images, csv file javascrip file must have to insert in static folder)
# templates(and inside templates index.html)(must)
#this html will be the frontend

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy #To store data in db

app = Flask(__name__) #To start app
app.config['SECRET_KEY'] = 'myapp' # protecting from hackers
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db" # name of our file data.db
db = SQLAlchemy(app)

#creating database
#it will create a database in the name of db and store the user enters data into it
class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.string(80))
    last_name = db.Column(db.string(80))
    email = db.Column(db.string(80))
    date = db.Column(db.Date)
    occupation = db.Column(db.string(80))


#step 3
#
@app.route('/',methods=['GET','POST'])#this will handel both get and post request in url
def index():
    #When the user press submit button it will Post
    if request.method == 'POST':#the user enters the url it will be get
        first_name = request.form['first_name']#get the first_name when user submit it
        last_name = request.form['last_name']
        email = request.form['email']# the form['email'] should be as in html file
        date = request.form['date']
        occupation = request.form['occupation']

        #inserting value to the database after user enters in ui
        form = Form(first_name=first_name, last_name=last_name,
                    email = email, date= date, occupation=occupation)
        #inserting
        db.session.add(form)
        db.session.commit()
    return render_template('index.html') #this render_template used to read the html file to retrun in ui

if __name__ == '__main__': #if name = main.py it will work
    #it will create db
    with app.app_context():
        db.create_all()


        app.run(debug=True, port=5001)#port any number
#step 1:http://127.0.0.1:5001/ this is url we get
#step 2: http://127.0.0.1:5001/my_page for eg: i have written my page to go load that page..so, we need to write code
#to move to my page using the above url

#Note : if you need to send mail to the user use before developed app code to send mail after submit

















