from flask import Flask, request

app = Flask(__name__)
@app.route("/")
def helloworld():
    return "Hello its test for update"

# Test for python post
@app.route("/get_data",methods = ['POST'])
def getdata():
    data = request.form['data']
    return data


if __name__ == "__main__":
    app.run()
