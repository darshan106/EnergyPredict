EnergyPredict ⚡
AI-Powered Energy Usage Forecasting for Efficiency and Sustainability
EnergyPredict is a web application that leverages machine learning to predict energy consumption based on historical data. Built with Flask and powered by an LSTM model, this tool helps users optimize energy usage, achieve sustainability goals, and make data-driven decisions through interactive visualizations and detailed reports.
Visualize your energy usage with interactive charts and actionable insights.

🚀 Features

Accurate Predictions: Uses an LSTM model to forecast energy usage with high precision.
Interactive Charts: Visualize actual vs. predicted energy usage with dynamic line graphs powered by Chart.js.
Secure Data Handling: Processes CSV uploads securely in memory, ensuring data privacy.
Detailed Reports: Download comprehensive reports with prediction results for further analysis.
Modern UI: Clean, responsive design with a drag-and-drop file uploader and loading animations.
Easy Deployment: Deployed on Render for seamless hosting without storage constraints.


🛠️ Tech Stack

Backend: Flask (Python)
Machine Learning: TensorFlow (LSTM model)
Frontend: HTML, CSS, JavaScript, Chart.js
Styling: Custom CSS with a modern SaaS design (Inter font, gradient backgrounds)
Deployment: Render (manual zip upload)


📈 How It Works

Upload Data: Drag and drop or select a CSV file with historical energy data (Datetime, COMED_MW).
Predict: The app processes the data using a pre-trained LSTM model to generate predictions.
Visualize: View actual vs. predicted energy usage on an interactive chart.
Download: Export a detailed report with your results.


📋 Prerequisites
To run this project locally, ensure you have the following installed:

Python 3.9+
pip (Python package manager)
Virtualenv (recommended for dependency isolation)


⚙️ Installation

Clone the Repository:
git clone https://github.com/yourusername/EnergyPredict.git
cd EnergyPredict


Set Up a Virtual Environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:
pip install -r requirements.txt


Run the Application:
python app.py

Open your browser and navigate to http://127.0.0.1:5000.



📂 Project Structure
EnergyPredict/
├── app.py                  # Main Flask application
├── model.py                # LSTM model loading and prediction logic
├── utils/
│   ├── preprocess.py       # Data preprocessing functions
│   └── report_generator.py # Report generation logic
├── static/
│   └── styles.css          # Custom CSS for styling
├── templates/
│   └── index.html          # Main HTML template
├── model/
│   └── lstm_model.h5       # Pre-trained LSTM model
├── requirements.txt        # Python dependencies
└── Procfile                # Render deployment configuration


🌐 Deployment
This project is deployed on Render using a manual zip upload method, making it easy to host without GitHub.
Deploy on Render

Zip your project folder:zip -r EnergyPredict.zip EnergyPredict


Go to render.com and create a new Web Service.
Choose “Upload a zip file” and upload EnergyPredict.zip.
Configure:
Runtime: Python
Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app
Instance Type: Free tier


Deploy and access your app at the provided URL (e.g., https://energypredict.onrender.com).


📊 Example Usage

Visit the deployed app (e.g., https://energypredict.onrender.com).
Scroll to the "Predict Your Energy Usage" section.
Upload a CSV file with Datetime and COMED_MW columns.
View the interactive chart comparing actual and predicted usage.
Download the generated report for detailed insights.


🤝 Contributing
Contributions are welcome! If you’d like to contribute:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Commit your changes (git commit -m "Add your feature").
Push to the branch (git push origin feature/your-feature).
Open a Pull Request.


📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

📬 Contact
For questions or feedback, reach out to me at your.email@example.com or open an issue on GitHub.

Built with ❤️ by Your Name
