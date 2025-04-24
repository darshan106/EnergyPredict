import torch
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from model import LSTMNet  # Ensure model.py is in the project
import os

# Set device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# === Load your trained model ===
input_dim = 5
hidden_dim = 256
output_dim = 1
n_layers = 2

model = LSTMNet(input_dim, hidden_dim, output_dim, n_layers)
model.load_state_dict(torch.load("models/lstm_model.pt", map_location=device))
model.to(device)
model.eval()

# === Load CSV ===
csv_path = "uploads/COMED_hourly.csv"
df = pd.read_csv(csv_path, parse_dates=["Datetime"])
print(f"Dataset size: {len(df)} rows")

# === Feature Engineering ===
df["hour"] = df["Datetime"].dt.hour
df["dayofweek"] = df["Datetime"].dt.dayofweek
df["month"] = df["Datetime"].dt.month
df["dayofyear"] = df["Datetime"].dt.dayofyear

# Reorder columns
df = df[["COMED_MW", "hour", "dayofweek", "month", "dayofyear"]]

# === Scaling ===
label_col_index = 0
scaler = MinMaxScaler()
label_scaler = MinMaxScaler()

data = scaler.fit_transform(df.values)
label_scaler.fit(df.iloc[:, label_col_index].values.reshape(-1, 1))

# === Create sequences (optimized) ===
def create_sequences(data, window_size, input_cols, label_col):
    num_sequences = len(data) - window_size
    inputs = np.zeros((num_sequences, window_size, len(input_cols)))
    labels = np.zeros((num_sequences, 1))

    for i in range(num_sequences):
        inputs[i] = data[i:i + window_size, input_cols]
        labels[i] = data[i + window_size, label_col]
        if i % 10000 == 0:
            print(f"Created {i} sequences...")
    return inputs, labels

window_size = 24  # Reduced from 90
input_cols = list(range(5))

X, y = create_sequences(data, window_size, input_cols, label_col_index)
print(f"Sequences created: X shape = {X.shape}, y shape = {y.shape}")

# === Batch Processing for Predictions ===
batch_size = 512  # Increased from 128
predictions = []
actuals = []

for i in range(0, len(X), batch_size):
    print(f"Processing batch {i // batch_size + 1}/{(len(X) + batch_size - 1) // batch_size}")
    X_batch = torch.from_numpy(X[i:i + batch_size]).float().to(device)
    y_batch = y[i:i + batch_size]

    h = model.init_hidden(X_batch.shape[0], device)

    with torch.no_grad():
        outputs, _ = model(X_batch, h)

    batch_predictions = outputs.cpu().numpy()
    batch_predictions = label_scaler.inverse_transform(batch_predictions)
    batch_actuals = label_scaler.inverse_transform(y_batch)

    predictions.extend(batch_predictions)
    actuals.extend(batch_actuals)

predictions = np.array(predictions)
actuals = np.array(actuals)

# === Display sample ===
print("\nSample Predictions (first 10):\n")
for i in range(min(10, len(actuals))):
    print(f"Actual: {actuals[i][0]:.2f} MW | Predicted: {predictions[i][0]:.2f} MW")