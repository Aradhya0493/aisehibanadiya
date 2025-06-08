def validate_input(data):
    # Validate the input data for loan eligibility
    required_fields = ['income', 'credit_score', 'current_debts']
    for field in required_fields:
        if field not in data:
            raise ValueError(f'Missing required field: {field}')
    
    # Additional validation rules can be added here
    if data['income'] < 0:
        raise ValueError('Income must be a positive value.')
    if data['credit_score'] < 300 or data['credit_score'] > 850:
        raise ValueError('Credit score must be between 300 and 850.')
    if data['current_debts'] < 0:
        raise ValueError('Current debts must be a positive value.')

    return True

def format_response(prediction, explanation):
    # Format the response to be returned to the frontend
    return {
        'prediction': prediction,
        'explanation': explanation
    }