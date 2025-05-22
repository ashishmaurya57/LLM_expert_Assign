import requests
from app.config import GROQ_API_KEY, GROQ_MODEL

def generate_response(query, context_chunks):
    prompt = (
        "Answer the question using only the context below:\n\n"
        + "\n".join(context_chunks) +
        f"\n\nQuestion: {query}\nAnswer:"
    )

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": GROQ_MODEL,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post("https://api.groq.com/openai/v1/chat/completions",
                             headers=headers, json=payload)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]
