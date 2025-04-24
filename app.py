import os
import torch
import pandas as pd
from flask import Flask, render_template, request, send_file
from utils.preprocess import preprocess_data, predict_energy
from utils.report_generator import generate_pdf_report
from model import LSTMNet

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
REPORT_FOLDER = "reports"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(REPORT_FOLDER, exist_ok=True)

# Define device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Model hyperparameters
input_dim = 5
hidden_dim = 256
output_dim = 1
n_layers = 2

# Initialize and load model
model = LSTMNet(input_dim, hidden_dim, output_dim, n_layers)
model.load_state_dict(torch.load("models/lstm_model.pt", map_location=device))
model.to(device)
model.eval()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith('.csv'):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            # Preprocess and predict
            df, actuals, predictions = predict_energy(filepath, model, device)
            
            # Prepare data for visualization (first 100 points for display)
            dates = df['Datetime'].iloc[-100:].astype(str).tolist()  # Last 100 timestamps
            actual_values = actuals[-100:].flatten().tolist()  # Last 100 actual values
            predicted_values = predictions[-100:].flatten().tolist()  # Last 100 predictions

            # Save report
            pdf_path = generate_pdf_report(df, actuals, predictions, file.filename)

            filename_only = os.path.basename(pdf_path)
            return render_template("index.html", 
                                 dates=dates, 
                                 actuals=actual_values, 
                                 predictions=predicted_values, 
                                 download_link=filename_only)
        else:
            return "Invalid file format. Please upload a CSV."

@app.route('/download/<filename>')
def download(filename):
    return send_file(os.path.join(REPORT_FOLDER, filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)