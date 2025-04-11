# Used Car Price Prediction
The **Used Car Price Prediction** project applies machine learning techniques to estimate the selling price of used cars based on various attributes such as brand, fuel type, model year, transmission, accident history, and title status. The model is deployed as a Flask web application, allowing users to input car details and receive a predicted price.

---
## Introduction
The used car market is highly dynamic, influenced by factors like vehicle age, condition, market demand, and brand perception. Predicting a car's price accurately can help buyers make informed decisions and assist sellers in setting competitive prices.

This project leverages machine learning algorithms and data preprocessing techniques to build a predictive model. It includes feature engineering, such as handling categorical variables, creating a 'car age' feature from the model year, and applying log transformation to the price variable to improve model performance.

---
## Dataset and Column Definitions
The dataset consists of various features that impact the price of used cars:
- **brand**: The car's manufacturer (e.g., Toyota, Ford, BMW)
- **fuel_type**: Type of fuel used (e.g., Gasoline, Diesel, Electric)
- **model_year**: The year the car was manufactured
- **transmission**: Transmission type (e.g., Automatic, Manual)
- **accident**: Whether the car has been in an accident (Yes/No)
- **clean_title**: Indicates whether the car has a clean title (Yes/No)
- **price**: The actual selling price (log-transformed for model training)

*Note: The 'car_age' feature is derived from 'model_year' but is not included in the user input form.*

---
## Key Features
- **Data Preprocessing**: Handling missing values, encoding categorical variables, feature scaling, and log transformation of price.
- **Feature Engineering**: Creating new variables like 'car age' and grouping rare brands into 'Other'.
- **Machine Learning Models**: Trained multiple regression models and selected the best-performing one for deployment.
- **Flask Web Application**: Provides an interface for users to input car details and receive price predictions.
- **Web Deployment**: The model is deployed using Flask, making it accessible via a simple web form.

---
## Project Folder Structure
```
Used_Car_Price_Prediction
│
├── app
│   ├── app.py  # Flask application
│   ├── modelHelper.py
│   ├── model_pipelne.pkl   # Trained machine learning model
│   ├── templates
│   │   ├── about.html  
│   │   ├── landing.html 
│   │   ├── model.html 
│   │   ├── tableau1.html 
│   │   ├── tableau2.html 
│   │   ├── report.html  
│   ├── static
│   │   ├── css  # Stylesheets
│   |    |	├── style.css
│   │   ├── images  # Project images
│   │   ├── js  # JavaScript files
│   |    |	├── logic.js
│   │   ├── writeup  # Additional documentation
│   |    |	|── Project_4_Report-Used_Cars_Price_Prediction.pdf  # Final report
│
├── notebooks
│   ├── data_cleaning_notebook.ipynb  # Data cleaning and preprocessing
│   ├── machine_learning_notebook.ipynb  # Model training and evaluation
│   ├── model_pipeline.ipynb  # Full pipeline implementation
│   ├── Prediction.ipynb  # Testing model predictions
│
├── Resources
│   ├── cleaned_data.csv  # Preprocessed dataset
│   ├── trained_data.csv  # Data used for model training
│   ├── test_data.csv  # Data used for model testing
│   ├── used_cars.csv  # Original dataset
│
├── documents
│   ├── Project_4_Presentation-Used_Cars_Price_Prediction.pdf  # Project presentation
│   ├── Project_4_Proposal-Used_Car_Price_Prediction.pdf  # Project proposal
│   ├── Project_4_Report-Used_Cars_Price_Prediction.pdf  # Final report
│
├── README.md  # Project documentation

```

---
## Instructions on How to Use and Interact with the Project

### Prerequisites
- **Python 3.10** installed
- Install dependencies using:
  ```
  pip install -r requirements.txt
  ```

### Running the Application
1. **Train the Model:**
   - Open `notebooks/machine_learning_notebook.ipynb` and run the notebook to train the regression model.
   - Save the trained model as `model_pipeline.pkl`.
2. **Start the Flask Web App:**
   - Navigate to the `app` directory.
   - Run the following command:
     ```
     python app.py
     ```
   - The application will be available at `http://127.0.0.1:5000/`.
3. **Using the Web App:**
   - Enter car details in the web form.
   - Click 'Predict' to receive an estimated price.

---
## Ethical Considerations
- The dataset does not include personally identifiable information (PII).
- Predictions are based on historical data and should not be considered absolute.
- The model does not account for factors like car condition, aftermarket modifications, or regional price variations.

---
## Limitations & Bias
- **Data Quality:** The accuracy of predictions depends on the dataset used for training.
- **Feature Availability:** Certain influential factors (e.g.,service history) are not included in the dataset.
- **Market Fluctuations:** The model does not dynamically update based on market trends.

---
## Future Enhancements
- **Include More Features:** Adding car condition, and region-based price trends.
- **Improve Model Performance:** Experimenting with deep learning models for better accuracy.

---
## Conclusion
The **Used Car Price Prediction** project applies machine learning to estimate car prices based on structured data. By integrating Flask for web deployment, it provides a user-friendly interface for price estimation. Future improvements will focus on enhancing model accuracy and expanding features to consider real-world price determinants.

