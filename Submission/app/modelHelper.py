import pandas as pd
import pickle
import numpy as np
import xgboost as xgb

class ModelHelper():
    def __init__(self):
        try:
            # Load trained XGBoost model
            with open("model_pipeline.pkl", 'rb') as model_file:
                self.model = pickle.load(model_file)
            print("Model loaded successfully.")
        except Exception as e:
            print(f"Error loading model: {e}")
            self.model = None

    def predict(self, model_year, mileage, car_age, brand_Acura, brand_Audi,
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
                    exterior_color_category_White, accident_Yes, accident_No, accident_Unknown, clean_title):

        if self.model is None:
            raise ValueError("Model is not loaded. Check 'model_pipeline.pkl' path.")

        # Prepare input data
        data = [
            model_year, mileage, car_age, brand_Acura, brand_Audi,
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
            exterior_color_category_White, accident_Yes, accident_No, accident_Unknown, clean_title
        ]

        # Convert input data to DataFrame
        input_data = pd.DataFrame([data], columns=self.model.get_booster().feature_names)

        # Ensure correct data types
        input_data = input_data.astype(float)

        # Make prediction
        predicted_log_price = self.model.predict(input_data)
        
        return predicted_log_price
