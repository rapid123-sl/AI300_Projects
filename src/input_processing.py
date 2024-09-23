def format_model_inputs(input_dict):
    age = int(input_dict['age']) # MIN - 19 MAX - 80
    zip_code = int(input_dict['zip_code']) # MIN - 90001 MAX - 96150
    
    contract_type_text = input_dict['contract_type'] #Month-to-Month-0, One Year-1, Two Year-2
    if contract_type_text == "Month-to-Month":
        contract_type = 0
    elif contract_type_text == "One year":
        contract_type = 1
    else:
        contract_type = 2
        
    internet_service_text = input_dict['has_internet_service'] # No Yes
    if internet_service_text == "No":
        has_internet_service = 0
    else:
        has_internet_service = 1
        
    total_monthly_fee = float(input_dict['total_monthly_fee'])  # MIN - 18.25 MAX - 118.75
    
    payment_method_text = input_dict['payment_method'] # Bank Withdrawal, Credit Card, Mailed Check
    if payment_method_text == "Mailed Check":
        payment_method = 0 
    elif payment_method_text == "Bank Withdrawal":
        payment_method = 1
    else:
        payment_method = 2 

    tenure_months = int(input_dict['tenure_months']) # MIN - 1 MAX - 72
    num_referrals = int(input_dict['num_referrals']) # MIN - 0 MAX - 11

    return [age, zip_code, contract_type, has_internet_service, total_monthly_fee, 
                    payment_method, tenure_months, num_referrals]