from typing import Any, Dict
import openai

def generate_explanation(prediction: str, user_data: Dict[str, Any]) -> str:
    """
    Generates an explanation for the loan eligibility prediction using OpenAI/Gemini.

    Args:
        prediction (str): The prediction result (e.g., "Approved" or "Denied").
        user_data (Dict[str, Any]): The user's financial data used for the prediction.

    Returns:
        str: A detailed explanation of the prediction and suggestions for improvement.
    """
    prompt = f"Based on the following user data: {user_data}, the loan eligibility prediction is '{prediction}'. " \
             "Please provide an explanation for this prediction and suggest ways to improve eligibility."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or the appropriate model name
        messages=[{"role": "user", "content": prompt}]
    )

    explanation = response.choices[0].message['content']
    return explanation.strip()