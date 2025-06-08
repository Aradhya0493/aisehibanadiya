def check_eligibility(user_data):
    # Example eligibility criteria
    income_threshold = 30000
    credit_score_threshold = 650
    current_debts_threshold = 20000

    income = user_data.get('income', 0)
    credit_score = user_data.get('credit_score', 0)
    current_debts = user_data.get('current_debts', 0)

    if income >= income_threshold and credit_score >= credit_score_threshold and current_debts <= current_debts_threshold:
        return {"eligible": True, "message": "Loan eligibility criteria met."}
    else:
        return {"eligible": False, "message": "Loan eligibility criteria not met."}