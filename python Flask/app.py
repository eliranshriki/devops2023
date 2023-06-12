from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello world! this is a test"

@app.route('/hey')
def hey_route():
    return "this is a test for new page"

if __name__=="__main__":
    app.run(host="127.0.0.1",port=80)


'''
terminal cmd:
## export FLASK_APP=app.py
## flask run
'''
