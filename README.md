# BatiKu Model Deployment

This repository contains code for deploying a machine learning model for Batik motif classification using a Flask web application. The model predicts the motif of a Batik image provided by the user.

## Project Structure

- **dataset/**: Contains the raw Batik image dataset.
- **output_dataset/**: Contains the Batik image dataset after preprocessing.
- **split_dataset/**: Contains the Batik image dataset split into training, validation, and test sets.
- **.gitignore**: Specifies files and directories to be ignored by git.
- **README.md**: This file, providing an overview and setup instructions.
- **app.py**: Flask web application for deploying the trained model and making predictions.
- **batiku.ipynb**: Jupyter notebook for training the Batik motif classification model.
- **model.h5**: Trained machine learning model.
- **requirements.txt**: List of dependencies required to run the application.

## Installation

To run the application locally, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/C241-PS403/ML.git
   cd ML
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install the dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Training the Model

The `batiku.ipynb` notebook contains the code to preprocess the dataset, augment images, train the model, and evaluate its performance. To train the model, run the notebook in a Jupyter environment.

## Running the Flask Application

1. **Ensure the model file is in the correct path**:

   Make sure the `model.h5` file is located at the specified path in `app.py`.

2. **Run the Flask application**:

   ```bash
   python app.py
   ```

3. **Access the application**:

   Open your browser and go to `http://127.0.0.1:5000/` to see the Flask app running.

## Making Predictions

To make predictions, you can use the `/predict` endpoint. You can send a POST request with an image file. The application will return the predicted Batik motif and the confidence score.

### Example

Use the following `curl` command to make a prediction:

```bash
curl -X POST -F 'file=@path_to_your_image.jpg' http://127.0.0.1:5000/predict
```
