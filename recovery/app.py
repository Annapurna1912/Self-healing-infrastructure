
from flask import Flask, request, jsonify
import subprocess 
import logging

app = Flask(__name__)

@app.route("/alert", methods=["POST"])
def handle_alert():
    data = request.get_json(silent=True) or {}

    alerts = data.get("alerts", [])
    recovered = []

    for alert in alerts:
        if alert.get("labels", {}).get("alertname") != "NginxExporterDown":
            continue

        result = subprocess.run(
            [
                "ansible-playbook",
                "/ansible/recover-nginx.yml"
            ],
            capture_output=True,
            text=True,
            timeout=120
        )

        recovered.append({
            "returncode": result.returncode,
            "output": result.stdout,
            "error": result.stderr
        })

    return jsonify({"results": recovered}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
