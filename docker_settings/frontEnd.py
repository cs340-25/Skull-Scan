import streamlit as st
from PIL import Image
import os
import subprocess
import tempfile
import json

# run with this command
# streamlit run frontEnd.py --server.port=8502
# -------------------------------
# Streamlit Config
# -------------------------------
st.set_page_config(page_title="Skull Scan", page_icon="💀", layout="wide")
st.markdown("""
    <style>
        .stButton > button {
            background-color: #4CAF50;
            color: white;
        }
        .stSpinner {
            font-size: 1.2rem;
        }
    </style>
""", unsafe_allow_html=True)

# -------------------------------
# Sidebar
# -------------------------------
st.sidebar.header("About This App")
st.sidebar.markdown("""
This tool uses a ML classifier to detect skulls in images.

**How to Use**:
- Upload a `.jpg`, `.jpeg`, or `.png` image.
- The app will return the result.
""")

# -------------------------------
# Main Interface
# -------------------------------
st.title("Skull Scan Classifier")
st.write("Upload an image to determine if it contains a skull.")

uploaded_file = st.file_uploader("📁 Upload Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file).convert("RGB")

        # Save the uploaded file to a temporary location
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp_file:
            temp_path = tmp_file.name
            image.save(temp_path)

        # Run your script with the image path
        with st.spinner("Analyzing..."):
            result = subprocess.run(
                ["python", "/app/classify_image.py", "--model", "/app/model", temp_path],
                capture_output=True, text=True
            )

            if result.returncode != 0:
                raise RuntimeError(result.stderr)

            output = result.stdout.strip()
            try:
                parsed = json.loads(output.replace("'", '"'))  # crude JSON-safe
                top = parsed[0]
                label = top["label"]
                confidence = top["score"] * 100
            except:
                raise RuntimeError("Could not parse model output")

        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(image, caption="Uploaded Image", width=250)

        with col2:
            icon = "✅" if "skull" in label.lower() else "❌"
            st.success(f"{icon} Prediction: **{label}**")
            st.progress(int(confidence))
            st.info(f"Confidence: **{confidence:.2f}%**")

        os.unlink(temp_path)  # clean up temp file

    except Exception as e:
        st.error("⚠️ Could not classify the image.")
        st.exception(e)
