from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/predict_sentiment', methods=['POST'])
def predict_sentiment():
    data = request.get_json()
    text = data.get('text', '')
    sentiment = "positive" if "good" in text else "negative"
    return jsonify({'sentiment': sentiment})

app.route('/optimize_task', methods=['POST'])
def optimize_task():
    data = request.get_json()
    priority = data.get('priority_numeric', 1)
    deadline = data.get('deadline', 1)
    workload = data.get('workload', 1)
    predicted_workload = workload * priority
    return jsonify({'predicted_workload': predicted_workload})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
    
