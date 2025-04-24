# ⚡ EnergyPredict  
**AI-Powered Energy Usage Forecasting for Efficiency and Sustainability**

**EnergyPredict** is a web application that leverages machine learning to forecast energy consumption based on historical data. Built with Flask and powered by an LSTM model, this tool helps users optimize energy usage, achieve sustainability goals, and make data-driven decisions through interactive visualizations and downloadable reports.

> Visualize your energy usage with interactive charts and actionable insights.

---

## 🚀 Features

- **Accurate Predictions:** Uses an LSTM model to forecast energy usage with high precision.
- **Interactive Charts:** Visualize actual vs. predicted energy usage with dynamic line graphs (Chart.js).
- **Secure Data Handling:** Processes CSV uploads securely in memory, ensuring privacy.
- **Detailed Reports:** Download comprehensive prediction reports for further analysis.
- **Modern UI:** Clean, responsive design with drag-and-drop uploader and animations.
- **Easy Deployment:** Deployed on Render without storage constraints.

---

## 🛠️ Tech Stack

- **Backend:** Flask (Python)  
- **Machine Learning:** TensorFlow (LSTM model)  
- **Frontend:** HTML, CSS, JavaScript, Chart.js  
- **Styling:** Custom CSS (Inter font, gradient backgrounds)  
- **Deployment:** Render (manual zip upload)  

---

## 📈 How It Works

1. **Upload Data:** Drag and drop or select a CSV file with `Datetime` and `COMED_MW` columns.
2. **Predict:** The LSTM model processes the data and generates future energy usage predictions.
3. **Visualize:** View interactive charts comparing actual vs. predicted values.
4. **Download:** Export a detailed report with the results.

---

## 📋 Prerequisites

- Python 3.9+
- pip (Python package manager)
- Virtualenv (recommended)

---

## ⚙️ Installation

```bash
# Clone the Repository
git clone https://github.com/yourusername/EnergyPredict.git
cd EnergyPredict

# Set Up Virtual Environment (Optional)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install Dependencies
pip install -r requirements.txt

# Run the Application
python app.py
Navigate to http://127.0.0.1:5000 in your browser.

```

## 📂 Project Structure

```bash
EnergyPredict/
├── app.py                  # Main Flask app
├── model.py                # LSTM prediction logic
├── utils/
│   ├── preprocess.py       # Data preprocessing
│   └── report_generator.py # Report generation
├── static/
│   └── styles.css          # Custom styles
├── templates/
│   └── index.html          # Frontend HTML
├── model/
│   └── lstm_model.h5       # Pre-trained model
├── requirements.txt        # Dependencies
└── Procfile                # Render config
```

---

## 🤝 Contributing

Contributions are welcome!
To contribute:

```bash
# Fork and Clone
git clone https://github.com/yourusername/EnergyPredict.git

# Create a new branch
git checkout -b feature/your-feature

# Make your changes and commit
git commit -m "Add your feature"

# Push changes
git push origin feature/your-feature

# Open a Pull Request
```

---

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for details.

