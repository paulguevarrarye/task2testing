#flask/bin/python
import math
from flask import Flask,jsonify, send_file
app = Flask (__name__)
measurements = [
    {
        'shape': 'circle',
        'radius': 5,
        'objects': 'orange, pizza, tire, steering wheel, pie'
    },
    {
        'shape': 'square',
        'side': 5,
        'objects': 'spongebob, poloroid, canvas, crt-tv'

    }
]

@app.route('/io', methods=['GET'])
def get_measurements():
    return jsonify({'measurements': measurements})

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/getcircle')
def get_circle():
    radius, circumference = calculate_circle()
    return "The circumference of a circle with a radius of {} is {}".format(radius,circumference)

@app.route('/getsquare')
def get_square():
    side, perimeter = calculate_square()
    return "The perimeter of a square with sides of {} is {}".format(side,perimeter)

def calculate_circle():
    num = getinput()
    return (num,2*num*math.pi)

def calculate_square():
    num=getinput()
    return (num, num*4)

def getinput():
    return(5)

if __name__ == '__main__':
    app.run(debug=True)