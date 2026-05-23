import streamlit as st
import requests
import base64

st.title("LaTeX OCR")
st.write("Upload an image containing LaTeX code, and the OCR will extract the LaTeX code for you.") 

upload = st.file_uploader("Choose an image file", type=["png", "jpg", "jpeg"])

if upload:
    st.image(upload)
    image_data = upload.read()
    encoder = base64.b64encode(image_data).decode("utf-8")

    if st.button("Extract LaTeX"):
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llava",
                "prompt" : """
You are a LaTeX OCR engine.

Rules:
- Return ONLY pure LaTeX
- No explanations
- No markdown
- No code fences
- No extra text

Convert the equation image into LaTeX.
""",
                "stream": False,
                "images": [encoder]
            }
        )

        data = response.json()
        st.subheader("Extracted LaTeX Code:")
        st.code(data)
        st.subheader("Rendered Equation")
        st.latex(data)