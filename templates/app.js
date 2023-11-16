function updateValue() {
    console.log("button was clicked!");

    // Get a value from app.js (replace this with your estimated price)
    let valueFromAppJS = 43;

    // Make a GET request to the server's endpoint
    fetch("https://jkl-si93.onrender.com/fetch_value")
        .then(response => response.json())
        .then(data => {
            // Get the value from the server's response
            let valueFromServer = data.value;

            // Choose whether to display the value from the server or app.js
            let finalValue = valueFromServer; // Change this assignment based on your preference

            // Update the content of the HTML element with the ID "output"
            let outputElement = document.getElementById("output");
            outputElement.textContent = "Final Value: " + finalValue;
        })
        .catch(error => {
            console.error("Error fetching value from server: " + error);

            // If there's an error, display the value from app.js
            let outputElement = document.getElementById("output");
            outputElement.textContent = "Value from app.js: " + valueFromAppJS;
        });
}
