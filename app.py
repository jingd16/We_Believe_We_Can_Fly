from flask import Flask, render_template, request, redirect
import numpy as np
import joblib

deafault_dict = {"Gender": 1, 
           "Customer Type": 0, 
           "Age": 40,
           "Type of Travel": 0, 
           "Class": 1,
           "Seat comfort": 3, 
           "Departure/Arrival time convenient": 3, 
           "Food and drink": 3,
           "Gate location": 3, 
           "Inflight wifi service": 3, 
           "Inflight entertainment": 3,
           "Online support": 3, 
           "Ease of Online booking": 3, 
           "On-board service": 3, 
           "Leg room service": 3, 
           "Baggage handling": 3,
           "Checkin service": 3, 
           "Cleanliness": 3, 
           "Online boarding": 3}


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index_customer1')
def customer1():
    return render_template('index_customer1.html')

@app.route('/index_customer2')
def customer2():
    return render_template('index_customer2.html')

@app.route('/index_customer3')
def customer3():
    return render_template('index_customer3.html')

@app.route('/index_customer4')
def customer4():
    return render_template('index_customer4.html')

@app.route('/index_predict')
def predict_page():
    return render_template('index_predict.html', anchor="Top")

@app.route('/predict', methods=['GET','POST'])
def predict():
    global deafault_dict

    # if request.method == "POST":
    int_features = [int(x) for x in request.form.values()]

    deafault_dict["Gender"] = int_features[0]
    deafault_dict["Customer Type"] = int_features[1]
    deafault_dict["Age"] = int_features[2]
    deafault_dict["Type of Travel"] = int_features[3]
    deafault_dict["Class"] = int_features[4]
    deafault_dict["Inflight entertainment"] = int_features[5]
    deafault_dict["Seat comfort"] = int_features[6]
    deafault_dict["On-board service"] = int_features[7]
    deafault_dict["Checkin service"] = int_features[8] 
 
    new_data = np.array([*deafault_dict.values()])
    new_data = new_data.reshape(1, -1)

    # Gender = request.form.values()

    print(int_features)
    print(new_data)
    
    #open file
    file = open("ML_random_forest_200.pkl","rb")
    
    #load trained model
    trained_model = joblib.load(file)
    
    #predict
    prediction = trained_model.predict(new_data)

    try:
        if (prediction[0] == "satisfied"):
            display_color = "#47b28d"
        elif (prediction[0] == "dissatisfied"):
            display_color = "#f0735a"

    except:
        pass

    return render_template('index_predict.html', prediction = prediction[0], 
    color=display_color, 
    dd0=deafault_dict["Gender"],
    dd1=deafault_dict["Customer Type"],
    dd2=deafault_dict["Age"],
    dd3=deafault_dict["Type of Travel"],
    dd4=deafault_dict["Class"],
    dd5=deafault_dict["Inflight entertainment"],
    dd6=deafault_dict["Seat comfort"],
    dd7=deafault_dict["On-board service"],
    dd8=deafault_dict["Checkin service"],
    anchor="TagIWantToLoadTo")
    
if __name__ == '__main__':
    app.run(debug=True)
