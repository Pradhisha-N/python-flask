from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask!"

@app.route('/add', methods=['POST'])
def add():
    data = request.json
    a = data.get('a')
    b = data.get('b')
    if a is None or b is None:
        return jsonify({"error": "Missing 'a' or 'b' in JSON"}), 400
    return jsonify({"result": a + b})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
