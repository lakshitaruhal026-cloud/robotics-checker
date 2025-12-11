from flask import Flask, request, render_template, send_from_directory
import os
import sys

# Add parent folder to path so we can import checker and sim
BASE_DIR = os.path.abspath(os.path.join(os.getcwd(), ".."))
sys.path.append(BASE_DIR)

from checker import code_checker
from sim import simulation_runner

app = Flask(__name__)

UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    f = request.files.get("file")
    if not f:
        return "No file uploaded", 400

    save_path = os.path.join(UPLOAD_DIR, "submitted.zip")
    f.save(save_path)

    report = code_checker.run_checks(save_path)
    return render_template("result.html", report=report)

@app.route("/simulate")
def simulate():
    result = simulation_runner.run_simulation(None)
    return render_template("simulation.html", result=result)

@app.route("/frames/<filename>")
def frames(filename):
    frame_dir = os.path.join(BASE_DIR, "sim", "sample_frames")
    return send_from_directory(frame_dir, filename)

if __name__ == "__main__":
    app.run(debug=True)