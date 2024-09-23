from flask import Flask, request, render_template
from model import Model
from input_processing import format_model_inputs

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        model = Model()

        request_data = request.form
        parameters = format_model_inputs(request_data) 
    
        prediction = model.predict(parameters)
        if prediction == 0:
            prediction = "will likely not churn"
        elif prediction == 1:
            prediction = "will likely churn"
        
        percentyeschurn = round(model.predict_proba(parameters)[1]*100, 2)
        percentnochurn = round(model.predict_proba(parameters)[0]*100, 2)
        
        return render_template('home.html', prediction=prediction, 
                               percentyeschurn=percentyeschurn, 
                               percentnochurn=percentnochurn
                               )
        
    return render_template('home.html', age=30, zip_code=90001, contract_type="One Year", 
                           has_internet_service="yes", total_monthly_fee=20.00, 
                           payment_method="Credit Card", tenure_months=12, num_referrals=0)

if __name__ == "__main__":
    app.run(debug=True) # default host: localhost, default port: 5000


# can't seem to get dynamic fields to work using input_processing. Works only with HTML rendering
# @app.route("/", methods=['GET', 'POST'])
# def home():
#     if request.method == 'POST':
#         model = Model()

#         request_data = request.form
#         extracted_data = format_model_inputs(request_data) 
    
#         parameters = extracted_data['model_inputs']
#         form_data = extracted_data['form_data']
        
#         prediction = model.predict(parameters)
#         if prediction == 0:
#             prediction = "will likely not churn"
#         elif prediction == 1:
#             prediction = "will likely churn"
        
#         percentyeschurn = round(model.predict_proba(parameters)[1]*100, 2)
#         percentnochurn = round(model.predict_proba(parameters)[0]*100, 2)
        
#         return render_template('home.html', prediction=prediction, 
#                                percentyeschurn=percentyeschurn, 
#                                percentnochurn=percentnochurn,
#                                **form_data)
        
#     return render_template('home.html', age=30, zip_code=90001, contract_type="One Year", 
#                            has_internet_service="yes", total_monthly_fee=20.00, 
#                            payment_method="Credit Card", tenure_months=12, num_referrals=0)

# Completed HTML rendering method, with dynamic fields
# @app.route("/", methods=['GET', 'POST'])
# def home():
#     if request.method == 'POST':
#         model = Model()
        
#         age = int(request.form['age']) # MIN - 19 MAX - 80
#         zip_code = int(request.form['zip_code']) # MIN - 90001 MAX - 96150
        
#         contract_type_text = request.form['contract_type'] #Month-to-Month-0, One Year-1, Two Year-2
#         if contract_type_text == "Month-to-Month":
#             contract_type = 0
#         elif contract_type_text == "One year":
#             contract_type = 1
#         else:
#             contract_type = 2
            
#         internet_service_text = request.form['has_internet_service'] # No Yes
#         if internet_service_text == "No":
#             has_internet_service = 0
#         else:
#             has_internet_service = 1
            
#         total_monthly_fee = float(request.form['total_monthly_fee'])  # MIN - 18.25 MAX - 118.75
       
#         payment_method_text = request.form['payment_method'] # Bank Withdrawal, Credit Card, Mailed Check
#         if payment_method_text == "Mailed Check":
#             payment_method = 0 
#         elif payment_method_text == "Bank Withdrawal":
#             payment_method = 1
#         else:
#             payment_method = 2 

#         tenure_months = int(request.form['tenure_months']) # MIN - 1 MAX - 72
#         num_referrals = int(request.form['num_referrals']) # MIN - 0 MAX - 11
    
#         parameters = [age, zip_code, contract_type, has_internet_service, total_monthly_fee, 
#                       payment_method, tenure_months, num_referrals]
        
#         prediction = model.predict(parameters)
#         if prediction == 0:
#             prediction = "will likely not churn"
#         elif prediction == 1:
#             prediction = "will likely churn"
        
#         percentyeschurn = round(model.predict_proba(parameters)[1]*100, 2)
#         percentnochurn = round(model.predict_proba(parameters)[0]*100, 2)
        
#         return render_template('home.html', prediction=prediction, 
#                                percentyeschurn=percentyeschurn, 
#                                percentnochurn=percentnochurn,
#                                age=age, zip_code=zip_code, contract_type=contract_type_text, 
#                                has_internet_service=internet_service_text, total_monthly_fee=total_monthly_fee, 
#                                payment_method=payment_method_text, tenure_months=tenure_months, 
#                                num_referrals=num_referrals)
        
#     return render_template('home.html', age=30, zip_code=90001, contract_type="One Year", 
#                            has_internet_service="yes", total_monthly_fee=20.00, 
#                            payment_method="Credit Card", tenure_months=12, num_referrals=0)


# attempted JSON method now, but something is wrong... 
# @app.route('/api/predict', methods=['POST'])
# def predict():
#     request_data = request.get_json()
    
#     model_inputs = format_model_inputs(request_data)
    
#     prediction = Model().predict(model_inputs)
    
#     if prediction == 0:
#         prediction = "will likely not churn"
#     elif prediction == 1:
#         prediction = "will likely churn"
        
#     percentyeschurn = round(Model().predict_proba(model_inputs)[1]*100, 2)
#     percentnochurn = round(Model().predict_proba(model_inputs)[0]*100, 2)

#     return {'prediction': prediction, 'percentyeschurn': percentyeschurn,
#             'percentnochurn': percentnochurn}
