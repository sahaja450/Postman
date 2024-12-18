from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add_numbers():
    # Parse JSON data from the request
    data = request.get_json()
    
    if not data or 'num1' not in data or 'num2' not in data:
        return jsonify({"error": "Please provide both 'num1' and 'num2' in JSON format"}), 400
    
    try:
        # Extract numbers and perform addition
        num1 = float(data['num1'])
        num2 = float(data['num2'])
        result = num1 + num2
        return jsonify({"num1": num1, "num2": num2, "sum": result}), 200
    except ValueError:
        return jsonify({"error": "Invalid number format"}), 400

if __name__ == '__main__':
    app.run(debug=True)
