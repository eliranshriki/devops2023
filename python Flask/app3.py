# JSON in FLASK
# accept post massage with postman

from flask import Flask, jsonify, request
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

@app.route('/add_num', methods=["POST","GET"])
def add_num():
    #get x,y fromthe posted data
    datadict = request.get_json()
    x=datadict["x"]
    y=datadict["y"]
    #add 2 numbers
    z=x+y

    #preper a json, "z":z
    retJson={
        "z":z
    }
    # return jsonify(map_prepared)
    return jsonify(retJson), 200

if __name__=="__main__":
    app.run(debug=True)


'''
terminal cmd:
## export FLASK_APP=app3.py
## flask run
'''
