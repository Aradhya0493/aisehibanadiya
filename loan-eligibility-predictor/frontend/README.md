# Loan Eligibility Predictor Frontend

This project is a frontend application for the Loan Eligibility Predictor, built using Gradio. It connects to a backend service that provides loan eligibility predictions based on user financial data.

## Project Structure

- `app/gradio_app.py`: The main file that sets up the Gradio interface for user interaction.
- `app/utils.py`: Contains utility functions for data preprocessing and formatting.
- `requirements.txt`: Lists the dependencies required for the frontend.

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd loan-eligibility-predictor/frontend
   ```

2. **Install Dependencies**
   It is recommended to use a virtual environment. You can create one using:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
   Then install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   Start the Gradio app by running:
   ```bash
   python app/gradio_app.py
   ```

4. **Access the Interface**
   Open your web browser and go to `http://localhost:7860` to access the loan eligibility predictor interface.

## Usage Examples

- Input your financial data such as income, credit score, and current debts.
- Click on the "Predict" button to see if you are eligible for a loan.
- The application will also provide suggestions for improving your eligibility based on the predictions.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.