from fastapi import APIRouter
from pydantic import BaseModel
from services.eligibility import check_eligibility
from services.explanation import generate_explanation

router = APIRouter()

class LoanApplication(BaseModel):
    income: float
    credit_score: int
    current_debts: float

@router.post("/check-eligibility")
async def check_loan_eligibility(application: LoanApplication):
    eligibility_result = check_eligibility(application.income, application.credit_score, application.current_debts)
    explanation = generate_explanation(application)
    return {
        "eligibility": eligibility_result,
        "explanation": explanation
    }