import os
from dotenv import load_dotenv
import requests

load_dotenv()  # Load .env file

API_KEY = os.getenv("OPENROUTER_API_KEY")  # Correct: fetch using the variable name

# def ask_jarvis(prompt):
#     url = "https://openrouter.ai/api/v1/chat/completions"
#     headers = {
#         "Authorization": f"Bearer {API_KEY}",
#         "Content-Type": "application/json"
#     }

#     data = {
#         "model": "mistralai/mistral-7b-instruct",
#         "messages": [
#             {"role": "user", "content": prompt}
#         ],
#         "max_tokens": 256,
#         "temperature": 0.7
#     }

#     try:
#         response = requests.post(url, headers=headers, json=data)
#         if response.status_code == 200:
#             result = response.json()
#             return result['choices'][0]['message']['content']
#         else:
#             print(f"Error: {response.status_code}", response.text)
#             return "Sorry, I couldn't fetch the response."
#     except Exception as e:
#         print(f"Exception: {e}")
#         return "Sorry, something went wrong."









def ask_jarvis(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "deepseek/deepseek-chat",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are Jarvis, a smart assistant with personality. "
                    "Answer naturally and realistically like a human. "
                    "No summaries — give only the next relevant response. "
                    "Be clear, brief, and helpful."
                    "You are developed by Gokul s nair"
                )
            },
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        return response.json()['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"[Jarvis Error: {e}]"

