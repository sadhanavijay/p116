# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Sadhana vijay" # write your name
    age = "16" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
def father_webpage():
    relation='father'
    f_name='vijay'
    f_age='nil'
    return render_template('father.html',relation=relation,father=f_name,father_age=f_age)

# define the route to mother webpage
def mother_webpage():
    relation='mother'
    m_name='yamini'
    m_age='45'
    return render_template('mother.html',relation=relation,mother=m_name,mother_age=m_age)

# define the route to friends webpage
def friend_webpage():
    relation='friend'
    fr_name='varshana'
    fr_age='13'
    return render_template('friend.html',relation=relation,friend=fr_name,friend_age=fr_age)

# add other routes, if you want

# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
