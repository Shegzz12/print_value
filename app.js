function updateValue() {
    // Get a value from app.js (replace this with your estimated price)
    let valueFromAppJS = 43;

    // Make a GET request to the server's endpoint
    fetch("http://127.0.0.1:5000/fetch_value")
        .then(response => response.json())
        .then(data => {
            // Get the value from the server's response
            let valueFromServer = data.value;

            // Update the content of the HTML element with the ID "output"
            let outputElement = document.getElementById("output");
            outputElement.textContent = "Value from server: " + valueFromServer;
        })
        .catch(error => {
            console.error("Error fetching value from server: " + error);
        });

    // Replace with your estimated price
    
    // Update the content of the HTML element with the ID "output"
    let outputElement = document.getElementById("output");
    outputElement.textContent = "Value from app.js: " + valueFromAppJS;
}
