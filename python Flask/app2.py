# JSON in FLASK

from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello world! this is a second test"

@app.route('/hey')
def hey_route():
    return "this is a test for second new page"

@app.route('/bye')
def bye():
    retJson = {

        'name':'Eliran Shriki',
        'age':37 ,
        "emails":[
            {
                "google mail": "eliranMail@gmail.com",
                "usage mail": "for personal email only"
            },
            {
                "hotmail mail": "eliranhotmail.com",
                "usage mail": "for work email only"
            }

        ]
    }
    return jsonify(retJson)


if __name__=="__main__":
    app.run(debug=True)


'''
terminal cmd:
## export FLASK_APP=app2.py
## flask run
'''
