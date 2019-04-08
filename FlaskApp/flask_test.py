# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
    
from flask import Flask
from flask import render_template
app = Flask(__name__)
posts= [
        {
                'author':'mukesh',
                'title':'Twitter API',
                'content':'Testing',
                },
         {
                'author':'Vikrant1',
                'title':'Spotify API',
                'content':'Testing'
                }
        ]
#@app.route('/')
@app.route('/home')
def home():
  # Link to test page
  return render_template('home.html',title='Home', posts=posts, user="mukesh")#'open the URL To see the test route go to /test'
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)
#    return '''
#<html>
#    <head>
#        <title>Home Page - Microblog</title>
#    </head>
 #   <body>
#        <h1>Hello, ''' + user['username'] + '''!</h1>
#    </body>
#</html>'''
@app.route('/about')
def about():
  return render_template('about.html',title='Home', user="mukesh")

@app.route('/test')
def testing():
  return 'You got to the testing route!'
@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello1 '+ name + '!'
def factors(num):
    return [x for x in range(1, num+1) if num%x==0]
@app.route('/factors/<int:num>')
def factors_route(num):
    return "The factors of {} are {}".format(num, factors(num))
print(factors(30))  #[1,2,3,5,6,10,15,30]
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
  