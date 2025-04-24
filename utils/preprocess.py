import torch
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def preprocess_data(df):
    # Feature engineering
    df["hour"] = df["Datetime"].dt.hour
    df["dayofweek"] = df["Datetime"].dt.dayofweek
    df["month"] = df["Datetime"].dt.month
    df["dayofyear"] = df["Datetime"].dt.dayofyear
    df = df[["COMED_MW", "hour", "dayofweek", "month", "dayofyear"]]
    
    # Scaling
    label_col_index = 0
    scaler = MinMaxScaler()
    label_scaler = MinMaxScaler()
    
    data = scaler.fit_transform(df.values)
    label_scaler.fit(df.iloc[:, label_col_index].values.reshape(-1, 1))
    
    return data, label_scaler

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

def predict_energy(filepath, model, device):
    # Load and preprocess
    df = pd.read_csv(filepath, parse_dates=["Datetime"])
    data, label_scaler = preprocess_data(df)
    
    # Create sequences
    window_size = 24
    input_cols = list(range(5))
    label_col_index = 0
    
    X, y = create_sequences(data, window_size, input_cols, label_col_index)
    print(f"Sequences created: X shape = {X.shape}, y shape = {y.shape}")
    
    # Batch processing for predictions
    batch_size = 512
    predictions = []
    
    for i in range(0, len(X), batch_size):
        print(f"Processing batch {i // batch_size + 1}/{(len(X) + batch_size - 1) // batch_size}")
        X_batch = torch.from_numpy(X[i:i + batch_size]).float().to(device)
        
        h = model.init_hidden(X_batch.shape[0], device)
        
        with torch.no_grad():
            outputs, _ = model(X_batch, h)
        
        batch_predictions = outputs.cpu().numpy()
        predictions.extend(batch_predictions)
    
    predictions = np.array(predictions)
    actuals = y
    
    # Inverse transform
    predictions = label_scaler.inverse_transform(predictions)
    actuals = label_scaler.inverse_transform(actuals)
    
    return df.iloc[window_size:], actuals, predictions
