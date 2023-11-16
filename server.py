from flask import Flask, jsonify, render_template
from logging import FileHandler, WARNING


app = Flask(__name__, template_folder = 'templates')
file_handler = FileHandler('errorlog.txt')
file_handler.setLevel(WARNING)

# Define an endpoint to fetch the value
@app.route('/', methods=['GET'])
def fetch_value():
    # In this example, we'll return a simple JSON response with a value
    return render_template("43")

# @app.route('/fetch_value', methods=['GET'])
# def fetch_value():
#     response
#     # In this example, we'll return a simple JSON response with a value
#     return response

if __name__ == '__main__':
    app.run(port=10000, debug=True)
