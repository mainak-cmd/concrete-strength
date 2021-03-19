from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('cons.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    Strength = 0
    if request.method == 'POST':
        Cement= float(request.form['Cement'])
        Blast_Furnace_Slag=float(request.form[' Blast Furnace Slag '])
        Water=int(request.form['Water'])
        Superplasticizer=int(request.form['Superplasticizer'])
        Coarse_Aggregate=int(request.form["Coarse Aggregate"])
        Fine_Aggregate=int(request.form['Fine Aggregate'])
        Age=int(request.form['Age'])
        
        prediction=final_model.predict([[Cement,Blast_Furnace_Slag,Water,Superplasticizer,Coarse_Aggregate,Fine_Aggregate,Age]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('index.html',prediction_text="You Can Sell The Car at {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)




