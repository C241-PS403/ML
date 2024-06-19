from flask import Flask, request, jsonify
import numpy as np
from keras.models import load_model
from keras.preprocessing import image
import tempfile
import os

app = Flask(__name__)

# Memuat model
model = load_model("model.h5")
print("Loaded model from disk")

# Informasi motif batik
motif_info = {
    0: {"name": "Motif Geblek Renteng"},
    1: {"name": "Motif Gentongan"},
    2: {"name": "Motif Liong"},
    3: {"name": "Motif Mega Mendung"},
    4: {"name": "Motif Parang"},
    5: {"name": "Motif Sekar Jagad"},
    6: {"name": "Motif Sidomukti"},
    7: {"name": "Motif Tambal"},
    8: {"name": "Motif Truntum"},
    9: {"name": "Motif Tujuh Rupa"}
    # Tambahkan motif lainnya sesuai dengan kebutuhan
}

# Fungsi untuk memprediksi gambar
def model_predict(img_path, model):
    img = image.load_img(img_path, target_size=(224, 224))  # Sesuaikan ukuran target dengan model Anda
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalisasi jika diperlukan oleh model

    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions, axis=1)[0]
    confidence = float(predictions[0][predicted_class])  # Akurasi atau confidence dari prediksi

    return predicted_class, confidence

@app.route('/', methods=['GET'])
def index():
    return "Flask app is running"

@app.route('/predict', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"})
    if file:
        # Simpan file ke direktori sementara
        with tempfile.NamedTemporaryFile(delete=False) as temp:
            file.save(temp.name)
            temp_path = temp.name

        predicted_class, confidence = model_predict(temp_path, model)
        result = motif_info.get(predicted_class, {"name": "Unknown", "info": "No information available"})
        result['confidence'] = confidence

        # Hapus file sementara setelah prediksi
        os.remove(temp_path)

        return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
