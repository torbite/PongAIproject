from flask import Flask
from flask import request
import json
from AI_Pong import AI

app = Flask(__name__)

lastAiCode = 0
AIsDict = {}

@app.route("/GetAnswer/<code>", methods = ["GET"])
def getAIAnswer(code):
    global AIsDict
    data = request.data
    inputs = json.loads(data)
    result = AIsDict[int(code)].calculateAnswer(inputs)
    return f"{result}"

@app.route("/getCode", methods = ["GET"])
def getCode():
    global lastAiCode, AIsDict
    lastAiCode += 1
    AIsDict[lastAiCode] = AI([15,7,3], 7)
    print(AIsDict[lastAiCode].Ws)
    return str(lastAiCode)

@app.route("/restart", methods = ["GET"])
def randomizeAI():
    global AIsDict
    for i in AIsDict.keys():
        AIsDict[i].randomizeAI(10)
        
    return 'done'

if __name__ == "__main__":
    app.run(debug=True)