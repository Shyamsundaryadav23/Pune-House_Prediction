# 🏠 Pune House Price Prediction Web App

This is a machine learning-based Flask web application that predicts house prices in Pune, India based on user input such as location, square footage, number of bedrooms (BHK), and number of bathrooms.

## 🚀 Features

- Cleaned and preprocessed real estate dataset
- Linear, Lasso, and Ridge regression models
- Best-performing model saved and deployed
- Interactive web interface built using Flask and HTML
- Predicts housing prices in lakhs based on form input

## 📊 Tech Stack

- Python
- Flask
- Scikit-learn
- Pandas, NumPy
- HTML + CSS (Jinja templates)
- Render (for deployment)

## 📁 Project Structure
├── app.py # Flask application
├── Model.pkl # Trained regression model
├── requirements.txt # Python dependencies
├── templates/
│ └── index.html # HTML form for prediction
├── Cleaned_data.csv # Cleaned dataset (optional)
└── README.md # Project documentation

## 💡 How It Works

1. User enters property details into the web form
2. The backend sends the data to the pre-trained model
3. Model predicts the price based on regression analysis
4. Predicted price is displayed on the page

## ⚙️ Setup Instructions

### 🔧 Local Development

1. Clone the repository:
   ```bash
   git clone https://github.com/Shyamsundaryadav23/Pune-House_Prediction.git
   cd Pune-House_Prediction
   python -m venv venv
   venv\Scripts\activate  
   pip install -r requirements.txt
   python app.py
## 🌐 Live Demo

🔗 [Click here to use the Pune House Price Predictor][(https://pune-house-prediction-uyax.onrender.com)]
# 📷 Screenshots
![Screenshot 2025-05-30 090838](https://github.com/user-attachments/assets/f9339f5a-86ff-400c-aae3-384f239b3f99)



