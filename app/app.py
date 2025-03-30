# Import Flask from the flask package
from flask import Flask, jsonify

# Create a new Flask application instance
app = Flask(__name__)

# Define the root route that returns 'Hello, World!' when accessed
@app.route('/')
def hello_world():
    return 'Hello, this is my first Devops project!'

# Define an API endpoint at /api/data that returns a JSON response
@app.route('/api/data', methods=['GET'])
def get_data():
    # Create a dictionary with a message and status
    data = {
        'message': 'This is a simple REST API',
        'status': 'success'
    }
    # Return the dictionary as a JSON response
    return jsonify(data)

# Check if the script is executed directly (and not imported)
if __name__ == '__main__':
    # Run the application on host 0.0.0.0 and port 5000
    app.run(host='0.0.0.0', port=5000)