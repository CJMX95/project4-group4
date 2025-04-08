function sendPredictionRequest() {
    const formData = {
        model_year: document.getElementById("model_year").value,
        mileage: document.getElementById("mileage").value,
        car_age: document.getElementById("car_age").value,
        clean_title: 1, // assuming it's checked or a value passed from the form
        brand_Audi: document.getElementById("brand_Audi").checked ? 1 : 0,
        brand_Mercedes_Benz: 0,  // Add any additional brands based on the form
        fuel_type_Gasoline: document.getElementById("fuel_type_Gasoline").checked ? 1 : 0,
        transmission_category_Automatic: document.getElementById("transmission_category_Automatic").checked ? 1 : 0,
        exterior_color_category_Black: document.getElementById("exterior_color_category_Black").checked ? 1 : 0,
        accident_No: document.getElementById("accident_No").checked ? 1 : 0,
    };

    // Send the data to the backend
    $.ajax({
        url: 'http://127.0.0.1:5000/predictions',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(formData),
        success: function(response) {
            if (response.ok) {
                document.getElementById("predicted-price").innerText = `Estimated Car Price: ${response.prediction}`;
            } else {
                console.error("Error:", response.message);
            }
        },
        error: function(xhr, status, error) {
            console.error("AJAX Error:", error);
        }
    });
}

// Optional: Bind the function to form input changes to update dynamically
$(document).on('change', '#car-form input', function() {
    sendPredictionRequest(); // Trigger the prediction on any input change
});
