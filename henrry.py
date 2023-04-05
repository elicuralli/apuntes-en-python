from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hola():
    return {
        "status": "success",
        "message":"hola"
    }

@app.route("/ctm", methods = ["POST"])
def ctm():
    body = request.json
    return body 

if __name__=='__main__':
    app.run(host='0.0.0.0', debug =True)