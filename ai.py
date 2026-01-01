import google.generativeai as genai

API_KEY = ""
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

def ask_ai(prompt: str):
    response = chat.send_message(prompt)

    return response.text
