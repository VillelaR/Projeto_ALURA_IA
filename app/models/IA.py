import flet as ft
import google.generativeai as genai

genai. configure(api_key='GET_API_KEY')

for m in genai.list_models():
    if "generateContent" in m.supported_generation_methods:
        print(m.name)

generation_config = {
    "candidate_count": 1,
    "temperature": 0.8,
}

safety_settings = {
    "HARASSMENT": "BLOCK_NONE",
    "HATE": "BLOCK_NONE",
    "SEXUAL": "BLOCK_NONE",
    "DANGEROUS": "BLOCK_NONE",
}

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

chat = model.start_chat(history=[])
