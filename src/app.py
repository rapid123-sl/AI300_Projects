from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        model = joblib.load('model/capstone_catboost_model.pkl')
        
        age = int(request.form['age']) # MIN - 19 MAX - 80
        zip_code = int(request.form['zip_code']) # MIN - 90001 MAX - 96150
        contract_type = request.form['contract_type'] #Month-to-Month, One Year, Two Year
        has_internet_service = request.form['has_internet_service'] # No Yes
        total_monthly_fee = float(request.form['total_monthly_fee'])  # MIN - 18.25 MAX - 118.75
        payment_method = request.form['payment_method'] # Bank Withdrawal, Credit Card, Mailed Check
        tenure_months = int(request.form['tenure_months']) # MIN - 1 MAX - 72
        num_of_referrals = int(request.form['num_referrals']) # MIN - 0 MAX - 11
    
        parameters = [age, zip_code, contract_type, has_internet_service, total_monthly_fee, 
                      payment_method, tenure_months, num_of_referrals]
        
        prediction = model.predict(parameters)
        
        return render_template('home.html', prediction=prediction)
        
    return render_template('home.html')

@app.route("/predict")
def predict():
    return "Give me a prediction of the outcome"

if __name__ == "__main__":
    app.run(debug=True) # default host: localhost, default port: 5000