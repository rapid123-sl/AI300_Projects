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
    
        prediction = model.predict(parameters['model_inputs'])
        if prediction == 0:
            prediction = "will likely not churn"
        elif prediction == 1:
            prediction = "will likely churn"
        
        return render_template('home.html', prediction=prediction)
        
    return render_template('home.html', age=30, zip_code=90001, contract_type="One Year", 
                           has_internet_service="yes", total_monthly_fee=20.00, 
                           payment_method="Credit Card", tenure_months=12, num_referrals=0)

if __name__ == "__main__":
    app.run(debug=True) # default host: localhost, default port: 5000

