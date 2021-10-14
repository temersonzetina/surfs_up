### Select Python interpreter by:
### Click View > Command Palette > Python: Select Interpret > PythonData

# Import Flask.
from flask import Flask

# Create a new Flask instance.
app = Flask(__name__)

# Create a 'root', or starting point.
@app.route('/')

# Create a function.
def name_entry():
    print('Enter your name:')
    x = input()
    print('Hello, ' + x)


