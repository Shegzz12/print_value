from flask import Flask, jsonify, render_template
from logging import FileHandler, WARNING


app = Flask(__name__, template_folder = 'templates')
file_handler = FileHandler('errorlog.txt')
file_handler.setLevel(WARNING)

# Define an endpoint to fetch the value
@app.route('/', methods=['GET'])
def index():
    # In this example, we'll return a simple JSON response with a value
    return render_template("index.html")

@app.route('/fetch_value')
def fetch_value():
    # Simulate dynamic JSON values
    json_data = {
        'key1': 'value1',
        'key2': 'value2',
        'key3': 'value3'
    }
    return jsonify({'value': json_data})

if __name__ == '__main__':
    app.run(port=10000, debug=True)
