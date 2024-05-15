from flask import Flask
from flask import request
import json
from AI_Pong import AI
import copy

app = Flask(__name__)

lastAiCode = 0
AIsDict = {}

@app.route("/GetAnswer/<code>", methods = ["POST"])
def getAIAnswer(code):
    global AIsDict
    data = request.data
    inputs = json.loads(data)
    result = AIsDict[int(code)][0].calculateAnswer(inputs)
    return f"{result}"

@app.route("/getCode", methods = ["GET"])
def getCode():
    global lastAiCode, AIsDict
    lastAiCode += 1
    AIsDict[lastAiCode] = [AI([15,7,3], 7), 0]
    print(AIsDict[lastAiCode].Ws)
    return str(lastAiCode)

@app.route("/restart", methods = ["GET"])
def randomizeAI():
    global AIsDict
    best = AIsDict[1][1]
    bestAI = AIsDict[1][0]
    for i in AIsDict.keys():
        if AIsDict[i][1] > best:
            bestAI = AIsDict[i][0]
            best = AIsDict[i][1]
    
    for i in AIsDict.keys():
        AIsDict[i][0] = copy.deepCopy(bestAI)
        AIsDict[i][1] = 0
        AIsDict[i][0].randomizeAI(10)
        
    return 'done'

if __name__ == "__main__":
    app.run(debug=True)
