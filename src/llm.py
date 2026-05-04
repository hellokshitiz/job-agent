import requests

def call_llm(prompt: str) -> str:
    url = "http://localhost:11434/api/generate"
    data = {
        "model": "qwen:7b",
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json().get("response", "")
    except Exception as e:
        return f"ERROR: {str(e)}"
