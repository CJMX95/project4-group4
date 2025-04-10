from flask import Flask, jsonify, render_template, request
from modelHelper import ModelHelper
import numpy as np
from flask_cors import CORS

# Flask Setup
app = Flask(__name__)
CORS(app)  # Enables cross-origin requests
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# Initialize the model helper
modelHelper = ModelHelper()

# Routes for HTML pages
@app.route('/')
def landing():
    return render_template('landing.html')

@app.route("/model")
def model():
    return render_template("index.html")

@app.route("/tableau1")
def tableau1():
    return render_template("tableau1.html")

@app.route("/tableau2")
def tableau2():
    return render_template("tableau2.html")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/works_cited")  
def works_cited():
    return render_template("works_cited.html") 

# Define all possible categories (these should match the categories used in training)
brands = [
    "Acura", "Audi", "BMW", "Cadillac", "Chevrolet", "Dodge", "Ford", "GMC", "Honda",
    "Hyundai", "INFINITI", "Jeep", "Kia", "Land", "Lexus", "Lincoln", "Mazda", "Mercedes_Benz",
    "Nissan", "Other", "Porsche", "RAM", "Subaru", "Tesla", "Toyota", "Volkswagen"
]

fuel_types = [
    "Diesel", "E85_Flex_Fuel", "Electric", "Gasoline", "Hybrid", "Plug_In_Hybrid", "Unknown"
]

transmission_categories = ["Automatic", "Dual_Shift", "Manual", "Other"]

exterior_colors = [
    "Black", "Blue", "Gray", "Green", "Other", "Red", "Silver", "White"
]

@app.route('/makePredictions', methods=['POST'])
def make_predictions():
    data = request.json['data']
    # Extract numerical features
    model_year = float(data['model_year'])
    mileage = float(data['mileage'])
    car_age = data['car_age']  # Car age should be passed as well

    # One-hot encode categorical variables
    brand_features = {f"brand_{b}": 0 for b in brands}
    fuel_features = {f"fuel_type_{f}": 0 for f in fuel_types}
    transmission_features = {f"transmission_category_{t}": 0 for t in transmission_categories}
    color_features = {f"exterior_color_category_{c}": 0 for c in exterior_colors}

    # Set the selected category to 1
    if f"brand_{data['brand']}" in brand_features:
        brand_features[f"brand_{data['brand']}"] = 1

    if f"fuel_type_{data['fuel_type']}" in fuel_features:
        fuel_features[f"fuel_type_{data['fuel_type']}"] = 1

    if f"transmission_category_{data['transmission_category']}" in transmission_features:
        transmission_features[f"transmission_category_{data['transmission_category']}"] = 1

    if f"exterior_color_category_{data['exterior_color_category']}" in color_features:
        color_features[f"exterior_color_category_{data['exterior_color_category']}"] = 1

    # Binary encoding for accident
    accident_yes = 1 if data['accident'].lower() == "yes" else 0
    accident_no = 1 if data['accident'].lower() == "no" else 0
    accident_unknown = 1 if data['accident'].lower() not in ["yes", "no"] else 0

    # Clean title encoding
    clean_title = 1 if str(data['clean_title']).strip().lower() == 'yes' else 0

    # Combine all features into a list, matching the model’s feature names
    feature_vector = [
        model_year, mileage, car_age,  # Numerical features
        *brand_features.values(),
        *fuel_features.values(),
        *transmission_features.values(),
        *color_features.values(),
        accident_yes, accident_no, accident_unknown,  # Accident binary encoding (order matters)
        clean_title  # Clean title encoding
    ]

    # Ensure the feature vector length matches the model's expected input shape
    expected_length = 52  # Based on the model's expected input feature count
    if len(feature_vector) != expected_length:
        return jsonify({'error': f"Expected {expected_length} features, but got {len(feature_vector)}."})

    # Unpack the feature_vector and pass it as individual arguments to predict()
    predicted_price_log = modelHelper.predict(*feature_vector)

    # Convert from log price to actual price
    predicted_price = np.exp(predicted_price_log[0])

    return jsonify({'prediction': predicted_price})


@app.after_request
def add_header(r):
    """ Add headers to disable caching """
    r.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

# Run the App
if __name__ == '__main__':
    app.run(debug=True)
