# Loan Eligibility Predictor

This project is a loan eligibility predictor that utilizes FastAPI for the backend and Gradio for the frontend. It integrates with OpenAI/Gemini to provide explanations for loan eligibility predictions.

## Project Structure

```
loan-eligibility-predictor
├── backend
│   ├── app
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── routes.py
│   │   ├── services
│   │   │   ├── eligibility.py
│   │   │   └── explanation.py
│   │   └── utils.py
│   ├── requirements.txt
│   └── README.md
├── frontend
│   ├── app
│   │   ├── gradio_app.py
│   │   └── utils.py
│   ├── requirements.txt
│   └── README.md
└── README.md
```

## Backend

The backend is built using FastAPI and includes the following components:

- **main.py**: Entry point of the application, initializes the FastAPI app and sets up routes.
- **models.py**: Defines data models for user financial data and loan eligibility criteria.
- **routes.py**: Contains API route definitions for loan eligibility checks and predictions.
- **services/eligibility.py**: Logic for determining loan eligibility based on user input.
- **services/explanation.py**: Integrates with OpenAI/Gemini for providing explanations and suggestions.
- **utils.py**: Utility functions for data validation and formatting.

### Setup Instructions

1. Navigate to the `backend` directory.
2. Install the required dependencies using:
   ```
   pip install -r requirements.txt
   ```
3. Run the application:
   ```
   uvicorn app.main:app --reload
   ```

## Frontend

The frontend is built using Gradio and includes the following components:

- **gradio_app.py**: Sets up the Gradio interface and connects to the backend API.
- **utils.py**: Utility functions for data preprocessing and formatting.

### Setup Instructions

1. Navigate to the `frontend` directory.
2. Install the required dependencies using:
   ```
   pip install -r requirements.txt
   ```
3. Run the Gradio app:
   ```
   python app/gradio_app.py
   ```

## Usage

Once both the backend and frontend are running, you can access the Gradio interface in your web browser to input financial data and receive loan eligibility predictions along with explanations.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.