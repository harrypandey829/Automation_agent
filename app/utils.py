import openai

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIxZjMwMDIxMTJAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.UkLKD3UztSeb6g9vGLd3ylUFE1mJdjNuezl0Qk66af8"


def query_llm(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": prompt}],
        api_key=API_TOKEN
    )
    return response["choices"][0]["message"]["content"].strip()