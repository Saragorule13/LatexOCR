import requests
import base64

with open("test.png", "rb") as f:
    image_data = f.read()
    encoder = base64.b64encode(image_data).decode("utf-8")

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llava",
        "prompt": "convert the image to latex, return only the latex code without any explanation",
        "stream": False,
        "images": [encoder]
    }
)

data = response.json()
print(data)