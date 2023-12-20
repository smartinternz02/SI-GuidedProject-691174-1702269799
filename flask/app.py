from flask import Flask,render_template,request
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np
app=Flask(__name__)
model=pickle.load(open("lifestyle_change_due_to_covid_dtc_model.pkl",'rb'))
#scaler=pickle.load(open("lifestyle_change_due_to_covid_ss.pkl.pkl",'rb'))
@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')


@app.route('/submit',methods=['POST','GET'])
def submit():
    age=float(request.form['age'])
    gender=float(request.form['gender'])
    occupation=float(request.form['occupation'])
    line_of_work=float(request.form['line_of_work'])
    prefer=float(request.form['prefer'])
    certaindays_hw=float(request.form['certaindays_hw'])
    time_bp=float(request.form['time_bp'])
    time_dp=float(request.form['time_dp'])
    travel_time=float(request.form['travel_time'])
    easeof_online=float(request.form['easeof_online'])
    hm=float(request.form['hm'])
    prod_inc=float(request.form['prod_inc'])
    sleep_bal=float(request.form['sleep_bal'])
    new_skill=float(request.form['new_skill'])
    fam_connect=float(request.form['fam_connect'])
    relaxed=float(request.form['relaxed']) 
    self_time=float(request.form['self_time'])
    like_hw=float(request.form['like_hw'])
    dislike_hw=float(request.form['dislike_hw'])
    
    #validate that the input values are not empty
    if '' in[age,gender,occupation,line_of_work,prefer,certaindays_hw]:
        return render_template('index.html',predict="Please fill in all fields.")

    result=model.predict([[age,gender,occupation,line_of_work,prefer,certaindays_hw,time_bp,time_dp,
                           travel_time,easeof_online,hm,prod_inc,sleep_bal,new_skill,fam_connect,relaxed,self_time,
                           like_hw,dislike_hw]])
    
    res=""
    if result==0:
        res="LIFE STYLE NOT CHANGED"
    else:
        res="LIFE STYLE CHANGED"
    
    return render_template('submit.html',result=res)

    

if __name__=='__main__':
    app.run(debug=True,port=1111)




