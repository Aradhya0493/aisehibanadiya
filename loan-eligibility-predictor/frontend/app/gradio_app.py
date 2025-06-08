from gradio import Interface, inputs, outputs
import requests

def predict_eligibility(income, credit_score, current_debts):
    response = requests.post("http://localhost:8000/predict", json={
        "income": income,
        "credit_score": credit_score,
        "current_debts": current_debts
    })
    return response.json()

def explain_eligibility(income, credit_score, current_debts):
    response = requests.post("http://localhost:8000/explain", json={
        "income": income,
        "credit_score": credit_score,
        "current_debts": current_debts
    })
    return response.json()

inputs = [
    inputs.Number(label="Income"),
    inputs.Number(label="Credit Score"),
    inputs.Number(label="Current Debts")
]

outputs = [
    outputs.JSON(label="Eligibility Prediction"),
    outputs.JSON(label="Explanation")
]

interface = Interface(
    fn=lambda income, credit_score, current_debts: (predict_eligibility(income, credit_score, current_debts), explain_eligibility(income, credit_score, current_debts)),
    inputs=inputs,
    outputs=outputs,
    title="Loan Eligibility Predictor",
    description="Enter your financial details to check loan eligibility and get explanations."
)

if __name__ == "__main__":
    interface.launch()