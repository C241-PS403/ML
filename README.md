# BatiKu Motif Classification API

This repository contains a Flask application for classifying batik motifs using a pre-trained Keras model. The application accepts image uploads and returns the predicted batik motif along with the confidence level.

## Project Structure

- `app.py`: Main Flask application file that handles HTTP requests and runs the model prediction.
- `model.h5`: Pre-trained Keras model used for classifying the batik motifs.

## Setup and Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.6+
- Flask
- Keras
- TensorFlow
- NumPy

### Installation

1. Clone the repository and switch to the `deploy-model` branch:

   ```bash
   git clone https://github.com/C241-PS403/ML.git
   cd ML
   git checkout deploy-model
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Place your pre-trained model (`model.h5`) in the project directory.

## Running the Application

1. Ensure your model is named `model.h5` and is placed in the root directory of the project.
2. Start the Flask application:

   ```bash
   python app.py
   ```

3. The application will be running at `http://127.0.0.1:5000/`.

## Usage

### Predicting Batik Motifs

To classify a batik motif, send a POST request to the `/predict` endpoint with an image file.

Example using `curl`:

```bash
curl -X POST -F 'file=@path_to_your_image.jpg' http://127.0.0.1:5000/predict
```
