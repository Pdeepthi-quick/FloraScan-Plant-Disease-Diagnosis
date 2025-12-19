from flask import Flask, request, jsonify, render_template, send_file
import numpy as np
from PIL import Image
import io
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.vgg19 import preprocess_input
from tensorflow.keras.models import load_model
from fpdf import FPDF
import os
from datetime import datetime

app = Flask(__name__)

# Load model
MODEL_PATH = "florascan_modelvgg19.h5"
model = load_model(MODEL_PATH)
print("✅ Model loaded successfully!")

# Class index mapping
ref = {
    0: "Apple___Apple_scab", 1: "Apple___Black_rot", 2: "Apple___Cedar_apple_rust", 3: "Apple___healthy",
    4: "Blueberry___healthy", 5: "Cherry_(including_sour)__Powdery_mildew", 6: "Cherry_(including_sour)__healthy",
    7: "Corn_(maize)__Cercospora_leaf_spot Gray_leaf_spot", 8: "Corn_(maize)__Common_rust",
    9: "Corn_(maize)__Northern_Leaf_Blight", 10: "Corn_(maize)__healthy", 11: "Grape___Black_rot",
    12: "Grape___Esca_(Black_Measles)", 13: "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)", 14: "Grape___healthy",
    15: "Orange___Haunglongbing_(Citrus_greening)", 16: "Peach___Bacterial_spot", 17: "Peach___healthy",
    18: "Pepper,_bell___Bacterial_spot", 19: "Pepper,_bell___healthy", 20: "Potato___Early_blight",
    21: "Potato___Late_blight", 22: "Potato___healthy", 23: "Raspberry___healthy", 24: "Soybean___healthy",
    25: "Squash___Powdery_mildew", 26: "Strawberry___Leaf_scorch", 27: "Strawberry___healthy",
    28: "Tomato___Bacterial_spot", 29: "Tomato___Early_blight", 30: "Tomato___Late_blight",
    31: "Tomato___Leaf_Mold", 32: "Tomato___Septoria_leaf_spot", 33: "Tomato___Spider_mites Two-spotted_spider_mite",
    34: "Tomato___Target_Spot", 35: "Tomato___Tomato_Yellow_Leaf_Curl_Virus", 36: "Tomato___Tomato_mosaic_virus",
    37: "Tomato___healthy"
}

# Load disease info
from disease_info import disease_info  # Dictionary with symptoms/remedies

# Image preprocessing
def preprocess_image(image_bytes):
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    image = image.resize((256, 256))
    image_array = img_to_array(image)
    image_array = preprocess_input(image_array)
    image_array = np.expand_dims(image_array, axis=0)
    return image_array

# Generate PDF
def generate_pdf(disease, symptoms, remedies, image_path, pdf_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="FloraScan - Plant Disease Diagnosis Report", ln=True, align="C")
    pdf.ln(10)

    if image_path and os.path.exists(image_path):
        pdf.image(image_path, x=60, w=90)
        pdf.ln(10)

    pdf.set_font("Arial", 'B', 12)
    pdf.cell(40, 10, "Disease:")
    pdf.set_font("Arial", size=12)
    pdf.cell(100, 10, txt=disease, ln=True)

    pdf.set_font("Arial", 'B', 12)
    pdf.cell(40, 10, "Symptoms:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=symptoms)

    pdf.set_font("Arial", 'B', 12)
    pdf.cell(40, 10, "Remedies:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=remedies)

    pdf.output(pdf_path)

# Routes
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/upload", methods=["GET"])
def upload():
    return render_template("upload.html")

@app.route("/privacy")
def privacy():
    return render_template("privacy.html")

@app.route("/faq")
def faq():
    return render_template("faq.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/signin")
def signin():
    return render_template("signin.html")

@app.route("/disease-info")
def dinfo():
    return render_template("Dinfo.html")

# Predict & Save
@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"success": False, "error": "No image uploaded"}), 400

    file = request.files["image"]
    if not file:
        return jsonify({"success": False, "error": "Empty file"}), 400

    try:
        img_bytes = file.read()
        processed_image = preprocess_image(img_bytes)
        preds = model.predict(processed_image)
        pred_class_idx = np.argmax(preds, axis=1)[0]
        disease = ref[pred_class_idx]

        info = disease_info.get(disease, {
            "symptoms": "Information not available.",
            "remedy": "Information not available."
        })

        # Create permanent folders (only once)
        image_folder = os.path.join("static", "results", "images")
        report_folder = os.path.join("static", "results", "reports")
        os.makedirs(image_folder, exist_ok=True)
        os.makedirs(report_folder, exist_ok=True)

        # Timestamped filenames
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        image_filename = f"input_{timestamp}.jpg"
        pdf_filename = f"report_{timestamp}.pdf"

        # Save image
        img = Image.open(io.BytesIO(img_bytes)).convert("RGB")
        image_path = os.path.join(image_folder, image_filename)
        img.save(image_path)

        # Save PDF
        pdf_path = os.path.join(report_folder, pdf_filename)
        generate_pdf(disease, info["symptoms"], info["remedy"], image_path, pdf_path)

        # Prepare response
        response = {
            "disease": disease,
            "symptoms": info["symptoms"],
            "remedies": info["remedy"],
            "image_path": f"/{image_path}",
            "report_url": f"/{pdf_path}"
        }

        return jsonify({
            "success": True,
            "prediction": response
        })

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

# Report download route
@app.route("/download-report/<path:filename>")
def download_report(filename):
    filepath = os.path.join("static", "results", "reports", filename)
    if os.path.exists(filepath):
        return send_file(filepath, as_attachment=True)
    else:
        return "File not found", 404

if __name__ == "__main__":
    app.run(debug=True)
