from flask import Flask, jsonify, render_template
from logging import FileHandler, WARNING
# from flask_cors import CORS

app = Flask(__name__, template_folder = 'templates')
file_handler = FileHandler('errorlog.txt')
file_handler.setLevel(WARNING)
# CORS(app)
# Define an endpoint to fetch the value
@app.route('/', methods=['GET'])
def fetch_value():
    # In this example, we'll return a simple JSON response with a value
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
