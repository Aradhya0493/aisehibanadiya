from pydantic import BaseModel

class UserFinancialData(BaseModel):
    income: float
    credit_score: int
    current_debts: float

class LoanEligibilityCriteria(BaseModel):
    min_income: float
    min_credit_score: int
    max_debts: float

class LoanEligibilityResponse(BaseModel):
    eligible: bool
    reason: str
    suggestions: list[str]