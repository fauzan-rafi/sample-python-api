from flask import Flask

app = Flask(__name__)
@app.route("/")
def helloworld():
    return "Hello its test for update"
@app.route("/get_data")
def getdata():
    return "Your data"
if __name__ == "__main__":
    app.run()
