from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# Define an endpoint to fetch the value
@app.route('/fetch_value', methods=['GET'])
def fetch_value():
    # In this example, we'll return a simple JSON response with a value
    response = jsonify({'value': 42})  # You can replace 42 with the actual value
    return response

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
