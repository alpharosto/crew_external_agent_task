from flask import Flask, request, jsonify
from coordinator_agent import CoordinatorAgent

app = Flask(__name__)

# Initialize the CoordinatorAgent
coordinator_agent = CoordinatorAgent(verbose=True)

@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.json
    if not data or 'weather_data' not in data or 'recipient' not in data:
        return jsonify({"error": "Invalid input"}), 400
    
    weather_data = data['weather_data']
    recipient = data['recipient']
    
    coordinator_agent.run(weather_data, recipient)
    return jsonify({"message": "Email sent successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
