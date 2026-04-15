from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/start_agent', methods=['POST'])
def start_agent():
    # Code to start the AI agent
    return jsonify({'message': 'AI agent started'}), 200

@app.route('/stop_agent', methods=['POST'])
def stop_agent():
    # Code to stop the AI agent
    return jsonify({'message': 'AI agent stopped'}), 200

@app.route('/process_input', methods=['POST'])
def process_input():
    data = request.json.get('input')
    # Code to process input received
    return jsonify({'message': 'Input processed', 'data': data}), 200

@app.route('/capture_voice', methods=['POST'])
def capture_voice():
    # Code to capture voice data
    return jsonify({'message': 'Voice data captured'}), 200

@app.route('/capture_vision', methods=['POST'])
def capture_vision():
    # Code to capture vision data
    return jsonify({'message': 'Vision data captured'}), 200

@app.route('/run_tool/<string:tool>', methods=['POST'])
def run_tool(tool):
    tools_map = {
        'nmap': 'nmap',
        'dns_lookup': 'dig',
        'ping': 'ping',
        'whois': 'whois',
        'traceroute': 'traceroute',
        'sqlmap': 'sqlmap',
        'nikto': 'nikto'
    }

    if tool not in tools_map:
        return jsonify({'message': 'Tool not found'}), 404

    command = tools_map[tool]
    # Example of running the command (make sure to handle with caution in production)
    output = subprocess.run([command], capture_output=True, text=True)
    return jsonify({'message': f'Executed {tool}', 'output': output.stdout}), 200

if __name__ == '__main__':
    app.run(debug=True)