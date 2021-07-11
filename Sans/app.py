from flask import Flask, render_template, request
import numpy as np
import joblib
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict/', methods=['GET','POST'])
def predict():
    
    if request.method == "POST":
        #get form data
        Gender = request.form.get('Gender')
        Customer_Type = request.form.get('Customer_Type')
        Age = request.form.get('Age')
        Type_Travel = request.form.get('Type_Travel')
        Class = request.form.get('Class')
        Flight_Distance = request.form.get('Flight_Distance')
        Seat_Comfort = request.form.get('Seat_Comfort')
        Dep_Arri_Time = request.form.get('Dep_Arri_Time')
        Food_Drink = request.form.get('Food_Drink')
        Gate_Location = request.form.get('Gate_Location')
        Wifi = request.form.get('Wifi')
        Inflight_Entertaiment = request.form.get('Inflight_Entertaiment')
        Online_Support = request.form.get('Online_Support')
        Ease_Booking = request.form.get('Ease_Booking')
        Onboard_Service = request.form.get('Onboard_Service')
        Leg_Room = request.form.get('Leg_Room')
        Beg_Handle = request.form.get('Beg_Handle')
        Checkin = request.form.get('Checkin')
        Cleanliness = request.form.get('Cleanliness')
        Online_Boarding = request.form.get('Online_Boarding')
        Dep_Delay = request.form.get('Dep_Delay')
        Arri_Delay = request.form.get('Arri_Delay')
        Eco_plus = request.form.get('Eco_plus')

        #call preprocessDataAndPredict and pass inputs
      
        prediction = preprocessDataAndPredict(Gender, 
                                                Customer_Type,
                                                Age,
                                                Type_Travel,
                                                Class,
                                                Flight_Distance,
                                                Seat_Comfort,
                                                Dep_Arri_Time,
                                                Food_Drink,
                                                Gate_Location,
                                                Wifi,
                                                Inflight_Entertaiment,
                                                Online_Support,
                                                Ease_Booking,
                                                Onboard_Service,
                                                Leg_Room,
                                                Beg_Handle,
                                                Checkin,
                                                Cleanliness,
                                                Online_Boarding,
                                                Dep_Delay,
                                                Arri_Delay,
                                                Eco_plus)
        #pass prediction to template
        return render_template('predict.html', prediction = prediction)
   
        
  
      

def preprocessDataAndPredict(Gender,
                            Customer_Type,
                            Age,
                            Type_Travel,
                            Class,
                            Flight_Distance,
                            Seat_Comfort,
                            Dep_Arri_Time,
                            Food_Drink,
                            Gate_Location,
                            Wifi,
                            Inflight_Entertaiment,
                            Online_Support,
                            Ease_Booking,
                            Onboard_Service,
                            Leg_Room,
                            Beg_Handle,
                            Checkin,
                            Cleanliness,
                            Online_Boarding,
                            Dep_Delay,
                            Arri_Delay,
                            Eco_plus):
    
    #keep all inputs in array
    test_data = [Gender,
                Customer_Type,
                Age,
                Type_Travel,
                Class,
                Flight_Distance,
                Seat_Comfort,
                Dep_Arri_Time,
                Food_Drink,
                Gate_Location,
                Wifi,
                Inflight_Entertaiment,
                Online_Support,
                Ease_Booking,
                Onboard_Service,
                Leg_Room,
                Beg_Handle,
                Checkin,
                Cleanliness,
                Online_Boarding,
                Dep_Delay,
                Arri_Delay,
                Eco_plus]
                
   #print(test_data)

    test_data = [0 if val is None else val for val in test_data]
    print(test_data)

    file = open("imputer.pkl","rb")
    
    #load trained model
    #imputer = joblib.load(file)
    
    #test_data = imputer.transform(test_data)
    
    #convert value data into numpy array
    test_data = np.array(test_data)
    
    #reshape array
    test_data = test_data.reshape(1,-1)
    test_data = test_data.astype(np.float64)
    print(test_data)
    
    #open file
    file = open("Pickle_RL_Model.pkl","rb")
    
    #load trained model
    trained_model = joblib.load(file)
    
    #predict
    prediction = trained_model.predict(test_data)
    
    return prediction
    
    pass

    
if __name__ == '__main__':
    app.run(debug=True)