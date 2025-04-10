$(document).ready(function() {
    console.log("Page Loaded");
    
    $("#predict-btn").click(function() {
        makePredictions();
    });
});

function makePredictions() {
     // Check if the function is triggered
    let payload = {
        "data": {
            "clean_title": $("#clean_title option:selected").val(),
            "model_year": parseInt($("#model_year").val()),
            "mileage": parseFloat($("#mileage").val()),
            "car_age": parseInt($("#car_age").val()),
            "brand": $("#brand option:selected").val(),
            "fuel_type": $("#fuel option:selected").val(),
            "transmission_category": $("#transmission option:selected").val(),
            "exterior_color_category": $("#exterior_color option:selected").val(),
            "accident": $("#accident option:selected").val()
        }
    };

    console.log("Payload:", payload);  // Check what you're sending

    // Send POST request to Flask API
    fetch('/makePredictions', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)  // Send the correct payload
    })
    .then(response => response.json())  // Parse the response as JSON
    .then(data => {
        // Handle the prediction response
        console.log(data);
        if (data.prediction) {
            document.getElementById('prediction-result').innerHTML = `Predicted Price: $${data.prediction.toFixed(2)}`;
        } else {
            document.getElementById('prediction-result').innerHTML = 'Error: No prediction received.';
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('prediction-result').innerHTML = 'Error: ' + error.message;
    });
}

