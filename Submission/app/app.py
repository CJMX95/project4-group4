from flask import Flask, jsonify, render_template, request
from modelHelper import ModelHelper
import logging
from flask_cors import CORS

# Flask Setup
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# Initialize the model helper
modelHelper = ModelHelper()

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Helper Function for Encoding
def one_hot_encode_feature(value, valid_options):
    """ Helper function to one-hot encode categorical features """
    return {f"{feature}_{value}": int(value == feature) for feature in valid_options}

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

@app.route('/predictions', methods=['POST'])
def get_prediction():
    try:
        # Get the data from the incoming request (JSON format)
        data = request.get_json()

        # Extract relevant features from the data (making sure all expected features are present)
        clean_title = data.get('clean_title', 0)
        model_year = data.get('model_year', 0)
        mileage = data.get('mileage', 0)
        car_age = data.get('car_age', 0)

        # Extract brand features (default to 0 if not provided)
        brand_Acura = data.get('brand_Acura', 0)
        brand_Audi = data.get('brand_Audi', 0)
        brand_BMW = data.get('brand_BMW', 0)
        brand_Cadillac = data.get('brand_Cadillac', 0)
        brand_Chevrolet = data.get('brand_Chevrolet', 0)
        brand_Dodge = data.get('brand_Dodge', 0)
        brand_Ford = data.get('brand_Ford', 0)
        brand_GMC = data.get('brand_GMC', 0)
        brand_Honda = data.get('brand_Honda', 0)
        brand_Hyundai = data.get('brand_Hyundai', 0)
        brand_INFINITI = data.get('brand_INFINITI', 0)
        brand_Jeep = data.get('brand_Jeep', 0)
        brand_Kia = data.get('brand_Kia', 0)
        brand_Land = data.get('brand_Land', 0)
        brand_Lexus = data.get('brand_Lexus', 0)
        brand_Lincoln = data.get('brand_Lincoln', 0)
        brand_Mazda = data.get('brand_Mazda', 0)
        brand_Mercedes_Benz = data.get('brand_Mercedes_Benz', 0)
        brand_Nissan = data.get('brand_Nissan', 0)
        brand_Other = data.get('brand_Other', 0)
        brand_Porsche = data.get('brand_Porsche', 0)
        brand_RAM = data.get('brand_RAM', 0)
        brand_Subaru = data.get('brand_Subaru', 0)
        brand_Tesla = data.get('brand_Tesla', 0)
        brand_Toyota = data.get('brand_Toyota', 0)
        brand_Volkswagen = data.get('brand_Volkswagen', 0)

        # Extract fuel type features
        fuel_type_Diesel = data.get('fuel_type_Diesel', 0)
        fuel_type_E85_Flex_Fuel = data.get('fuel_type_E85_Flex_Fuel', 0)
        fuel_type_Electric = data.get('fuel_type_Electric', 0)
        fuel_type_Gasoline = data.get('fuel_type_Gasoline', 0)
        fuel_type_Hybrid = data.get('fuel_type_Hybrid', 0)
        fuel_type_Plug_In_Hybrid = data.get('fuel_type_Plug_In_Hybrid', 0)
        fuel_type_Unknown = data.get('fuel_type_Unknown', 0)

        # Extract transmission category features
        transmission_category_Automatic = data.get('transmission_category_Automatic', 0)
        transmission_category_Dual_Shift = data.get('transmission_category_Dual_Shift', 0)
        transmission_category_Manual = data.get('transmission_category_Manual', 0)
        transmission_category_Other = data.get('transmission_category_Other', 0)

        # Extract exterior color features
        exterior_color_category_Black = data.get('exterior_color_category_Black', 0)
        exterior_color_category_Blue = data.get('exterior_color_category_Blue', 0)
        exterior_color_category_Gray = data.get('exterior_color_category_Gray', 0)
        exterior_color_category_Green = data.get('exterior_color_category_Green', 0)
        exterior_color_category_Other = data.get('exterior_color_category_Other', 0)
        exterior_color_category_Red = data.get('exterior_color_category_Red', 0)
        exterior_color_category_Silver = data.get('exterior_color_category_Silver', 0)
        exterior_color_category_White = data.get('exterior_color_category_White', 0)

        # Extract accident features
        accident_Yes = data.get('accident_Yes', 0)
        accident_No = data.get('accident_No', 0)
        accident_Unknown = data.get('accident_Unknown', 0)

        # Use ModelHelper to get prediction
        predicted_price = modelHelper.predictions(
            clean_title, model_year, mileage, car_age, brand_Acura, brand_Audi,
            brand_BMW, brand_Cadillac, brand_Chevrolet, brand_Dodge, brand_Ford,
            brand_GMC, brand_Honda, brand_Hyundai, brand_INFINITI, brand_Jeep,
            brand_Kia, brand_Land, brand_Lexus, brand_Lincoln, brand_Mazda,
            brand_Mercedes_Benz, brand_Nissan, brand_Other, brand_Porsche, brand_RAM,
            brand_Subaru, brand_Tesla, brand_Toyota, brand_Volkswagen, fuel_type_Diesel,
            fuel_type_E85_Flex_Fuel, fuel_type_Electric, fuel_type_Gasoline, fuel_type_Hybrid,
            fuel_type_Plug_In_Hybrid, fuel_type_Unknown, transmission_category_Automatic,
            transmission_category_Dual_Shift, transmission_category_Manual,
            transmission_category_Other, exterior_color_category_Black,
            exterior_color_category_Blue, exterior_color_category_Gray,
            exterior_color_category_Green, exterior_color_category_Other,
            exterior_color_category_Red, exterior_color_category_Silver,
            exterior_color_category_White, accident_Yes, accident_No, accident_Unknown
        )

        # Return the result in the response
        return jsonify({'ok': True, 'predicted_price': predicted_price})

    except Exception as e:
        return jsonify({'ok': False, 'message': str(e)}), 500

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
