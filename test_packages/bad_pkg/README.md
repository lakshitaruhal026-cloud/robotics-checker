# Robotics Checker – Assignment Submission

This repository contains my submission for the Robotics Checker assignment.  
It includes a Flask-based web application that:

1. **Checks ROS package structure**
2. **Detects syntax errors in Python ROS nodes**
3. **Extracts node information (publishers, subscribers, init function)**
4. **Simulates motion and generates frame images**
5. **Displays results in a simple web interface**

---

## 📁 Project Structurerobotics-checker/
│
├── checker/
│   ├── code_checker.py        # Checks syntax and structure of uploaded ROS package
│
├── sim/
│   ├── simulation_runner.py   # Generates simple simulated frames
│
├── web/
│   ├── app.py                 # Flask web application
│   ├── templates/
│   │   ├── index.html         # Upload page
│   │   ├── result.html        # Checker report output
│   │   ├── simulation.html    # Simulation result page
│   └── sample_frames/         # Automatically generated sample simulation frames
│
├── test_packages/
│   ├── good_pkg.zip           # Example valid ROS package
│   ├── bad_pkg.zip            # Example invalid ROS package
│
├── uploads/                   # Folder where uploaded ZIP files are stored
│
├── requirements.txt           # Python dependencies
└── README.md
---

## ▶️ How to Run the Application

### **1. Create virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate
INSTALL DEPENDENCIES
pip install -r requirements.txt
RUN THE FLASK APPLICATIONcd web
python3 app.py
OPEN IN BROWSER:
http://127.0.0.1:5000
Features Implemented

✔ ROS Package Checker
	•	Validates folder structure
	•	Checks for __init__
	•	Lists publishers & subscribers
	•	Detects syntax errors
	•	Outputs a detailed JSON report

✔ Simulation Preview
	•	Generates dummy motion frames
	•	Displays success status & joint positions

✔ Web Interface
	•	Upload ROS package
	•	View checker results
	•	Run simulation preview
Example Output

Checker Report
{
  "status": "PASSED",
  "structure_valid": true,
  "syntax_errors": [],
  "node_info": {
    "has_init": false,
    "pubs": 0,
    "subs": 0
  }
}
Simulation Result
	•	Success: True
	•	Joint positions: [0.0, 0.5, 1.0, 0.2, -0.2, 0.0]
Author

Lakshita Ruhal (lakshitaruhal026-cloud)
Robotics Checker Assignment
