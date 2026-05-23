import streamlit as st

st.title("LaTeX OCR")
st.write("Upload an image containing LaTeX code, and the OCR will extract the LaTeX code for you.")

upload = st.file_uploader("Choose an image file", type=["png", "jpg", "jpeg"])

if upload:
    st.image(upload, caption="Uploaded Image", use_column_width=True)