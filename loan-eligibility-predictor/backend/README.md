# Loan Eligibility Predictor Backend

This project is a loan eligibility predictor built using FastAPI (or Flask) for the backend and Gradio for the frontend. The application predicts loan eligibility based on user financial data and provides explanations for the predictions using OpenAI/Gemini.

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd loan-eligibility-predictor/backend
   ```

2. **Install dependencies:**
   Use pip to install the required packages listed in `requirements.txt`.
   ```
   pip install -r requirements.txt
   ```

3. **Run the application:**
   To start the FastAPI (or Flask) server, run:
   ```
   python app/main.py
   ```

## API Endpoints

- **POST /predict**
  - Description: Predict loan eligibility based on user financial data.
  - Request Body: JSON object containing user data (income, credit score, current debts).
  - Response: JSON object with loan eligibility prediction.

- **GET /explain**
  - Description: Get explanations for the loan eligibility prediction.
  - Request Parameters: Prediction ID.
  - Response: JSON object with suggestions for improving eligibility.

## Usage Examples

### Predict Loan Eligibility
```bash
curl -X POST "http://localhost:8000/predict" -H "Content-Type: application/json" -d '{"income": 50000, "credit_score": 700, "current_debts": 10000}'
```

### Get Explanation
```bash
curl -X GET "http://localhost:8000/explain?prediction_id=12345"
```

## Folder Structure

- `app/`: Contains the main application code.
  - `main.py`: Entry point of the application.
  - `models.py`: Data models for user financial data and eligibility criteria.
  - `routes.py`: API route definitions.
  - `services/`: Contains business logic for eligibility and explanations.
    - `eligibility.py`: Logic for determining loan eligibility.
    - `explanation.py`: Integration with OpenAI/Gemini for explanations.
  - `utils.py`: Utility functions for data validation and formatting.

## License
This project is licensed under the MIT License. See the LICENSE file for details.