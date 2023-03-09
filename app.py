from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/check_integer', methods=['POST'])
def check_integer():
    data = request.get_json()
    value = data.get('integer')
    if value is not None:
        if value > 100:
            result = "high"
        else:
            result = "low"
        return jsonify({"result": result})
    else:
        return jsonify({"error": "Invalid input"})

if __name__ == '__main__':
    app.run()
