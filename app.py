# Import dependencies
from flask import Flask

# Create a new Flask instance
app = Flask(__name__)

Define root
@app.route('/')
def hello_world():
   return 'Hello world!'

#@app.route('/')
#def new_func():
    #your_name = input('What is you name?')
    #message=f'{your_name} is a very nice name.'
    #return message

