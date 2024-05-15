import numpy as np
import copy
import math
import random
class AI():
    def __init__(self, hidden_layers : list, inputs : int):
        Ws, bs= self.createLayers(inputs, hidden_layers)
        self.Ws = Ws
        self.bs = bs
        
        for i in range(10):
            self.randomizeAI(10)    
        print(self.calculateAnswer([1,1]))

# Layer Newral network creation process: -------------------------------------------
    def createLayers(self, inputs, hidden_layers):
        Ws = []
        bs = []
        for i in range(len(hidden_layers)):
            if(i == 0):
                Ws.append(self.createLayer(inputs,hidden_layers[i]))
                
                
            else:
                Ws.append(self.createLayer(hidden_layers[i-1],hidden_layers[i]))
            bs.append(np.zeros(hidden_layers[i]))
               
        
        return Ws, bs

    def createLayer(self, x,y):
        return(np.zeros((x,y)))
# ------------------------------------------- : -------------------------------------------

# AI Thinking goes here : -------------------------------------------------------

    def calculateAnswer(self, inputs):
        n = len(self.Ws)
        answ = inputs
        for i in range(n):
            if(i == n -1):
                answ = self.Dense(answ, self.Ws[i], self.bs[i], True)
            else:
                answ = self.Dense(answ, self.Ws[i], self.bs[i], False)
        return answ
        #print(answ)

    def Dense(self,a_in, W, b, lastLayer : bool):
        units = W.shape[1]
        a_out = np.zeros(units)
        
        for j in range(units):
            
            w = W[:,j]
            
            z = np.dot(w,a_in) + b[j]
            if(lastLayer):
                a_out[j] = z 
            else:
                a_out[j] = self.relu(z)
        if(lastLayer):
            # Subtracting the maximum value for numerical stability
            a_out -= np.max(a_out)
            exp_values = np.exp(a_out)
            # Apply softmax function
            a_out = exp_values / np.sum(exp_values)
            print('FUCK YWEA')
        

        return a_out

    def relu(self,z):
        return(max(z,0))
    


#------------------------------------------------------- : -------------------------------------------------------

    def randomizeAI(self, ramdomness : float):
        for i in range(len(self.Ws)):
            for j in range(len(self.Ws[i])):
                for k in range(len(self.Ws[i][j])):
                    self.Ws[i][j][k] += random.uniform(-ramdomness,  ramdomness)
        for i in range(len(self.bs)):
            for j in range(len(self.bs[i])):
                self.bs[i][j] += random.uniform(-ramdomness, +ramdomness)
a = AI([3, 2, 10], 2)