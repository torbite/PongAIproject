from flask import Flask

app = Flask(__name__)

lastCode = 0

@app.route("/", methods = ["POST"])
def hello_world():
    return "134"

@app.route("/getCode", methods = ["GET"])
def getCode():
    lastCode += 1
    return str(lastCode)

if __name__ == "__main__":
    app.run(debug=True)