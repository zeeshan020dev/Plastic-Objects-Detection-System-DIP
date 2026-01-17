import streamlit as st
from ultralytics import YOLO
import cv2
import numpy as np
from PIL import Image

# ----------------------------------
# PAGE CONFIG
# ----------------------------------
st.set_page_config(page_title="Plastic Detection", layout="wide")

# ----------------------------------
# CUSTOM CSS
# ----------------------------------
st.markdown("""
    <style>
        .main { background-color: #111827; color: white; }
        h1, h2, h3, h4 { color: white; }
        .stButton button {
            border-radius: 10px;
            padding: 0.6rem 1.2rem;
            font-size: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# ----------------------------------
# LOAD YOLO MODEL
# ----------------------------------
model = YOLO("best.pt")

# ----------------------------------
# APP TITLE
# ----------------------------------
st.title("♻️ Plastic Object Detection (Image + Real-Time Webcam)")


# ----------------------------------
# SIDEBAR SETTINGS
# ----------------------------------
st.sidebar.header("⚙️ Settings")
mode = st.sidebar.radio("Select Mode:", ["Image Upload", "Real-Time Webcam"])
conf = st.sidebar.slider("Confidence Threshold", 0.1, 1.0, 0.5)


# ----------------------------------
# IMAGE UPLOAD MODE
# ----------------------------------
if mode == "Image Upload":
    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        img = Image.open(uploaded_file)
        st.image(img, caption="Original Image", use_column_width=True)

        with st.spinner("Detecting objects..."):
            results = model.predict(img, conf=conf)
            result_img = results[0].plot()

        st.image(result_img, caption="Detection Result", use_column_width=True)



# ----------------------------------
# REAL-TIME WEBCAM MODE
# ----------------------------------
elif mode == "Real-Time Webcam":

    st.subheader("📸 Live Camera Detection")
    start_cam = st.checkbox("Start Live Camera")

    FRAME_WINDOW = st.image([])

    if start_cam:
        cap = cv2.VideoCapture(0)

        while start_cam:
            ret, frame = cap.read()
            if not ret:
                st.warning("⚠️ Unable to access camera")
                break

            # YOLO detection
            results = model(frame, conf=conf)
            frame = results[0].plot()

            # Convert BGR → RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Display frame
            FRAME_WINDOW.image(frame)

            # Check checkbox state (to stop loop)
            start_cam = st.session_state.get("Start Live Camera", True)

        cap.release()
        st.info("Camera stopped.")
