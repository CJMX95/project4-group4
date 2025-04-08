function sendPredictionRequest() {
    console.log("sendPredictionRequest function called!");  // Add this line to check if function is being triggered

    // Test with dummy data
    const testFeatures = {
        model_year: 2018,
        mileage: 50000,
        car_age: 7,
        clean_title: 1,  // Assuming clean title is 'Yes'
        accident_No: 1,  // Assuming accident is 'No'
        accident_Yes: 0, 
        accident_Unknown: 0,
        brand: 'Audi',
        fuel_type: 'Gasoline',
        transmission_category: 'Automatic',
        exterior_color_category: 'Black'
    };

    console.log("Test Features:", testFeatures); // Log the dummy data to check

    // Send the features to the backend API for prediction
    $.ajax({
        url: 'http://127.0.0.1:5000/predictions',  // Ensure URL is correct
        type: 'POST',  // Make sure it's a POST request
        contentType: 'application/json',
        data: JSON.stringify(testFeatures),  // Send the testFeatures data as JSON
        success: function(response) {
            console.log("Response from server:", response);
            if (response.ok) {
                document.getElementById("prediction-result").innerText = `Estimated Car Price: $${response.prediction.toLocaleString()}`;
            } else {
                console.error("Error:", response.message);
                document.getElementById("prediction-result").innerText = "Error: Unable to fetch prediction";
            }
        },
        error: function(xhr, status, error) {
            console.error("AJAX Error:", error);
            document.getElementById("prediction-result").innerText = "Error: Unable to connect to the server";
        }
    });
}

document.addEventListener("DOMContentLoaded", function() {
    // Attach event listener to the "Get Prediction" button
    document.getElementById('predict-btn').addEventListener('click', function() {
        sendPredictionRequest();  // Send test request on button click
    });
});
