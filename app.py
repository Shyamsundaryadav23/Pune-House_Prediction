from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load model
model = pickle.load(open('Model.pkl', 'rb'))

# Load locations from your dataset or hardcode them
df = pd.read_csv('Cleaned_data.csv')  # must be same one used for model
locations = sorted(df['location'].unique())

@app.route('/')
def home():
    return render_template('index.html', locations=locations)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        total_sqft = float(request.form['total_sqft'])
        bath = float(request.form['bath'])
        bhk = int(request.form['bhk'])
        location = request.form['location']

        input_df = pd.DataFrame([[location, total_sqft, bath, bhk]],columns=['location', 'total_sqft', 'bath', 'BHK'])
        prediction = model.predict(input_df)[0]
        output = round(prediction, 2)

        return render_template('index.html', locations=locations,
                           prediction_text=f'Estimated Price: ₹{output} Lakhs')
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}", locations=locations)

if __name__ == '__main__':
    app.run(debug=True)
