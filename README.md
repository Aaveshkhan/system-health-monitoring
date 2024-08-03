# System Health Monitoring
Script used to monitor the health of a Linux system. It checks the CPU usage, memory usage, disk space, and running processes. If any of these metrics exceed predefined thresholds (e.g., CPU usage > 80%), the script logs the output on terminal.

---

## Step 1: Install Python, PIP and VENV
`sudo apt install python3 python3-venv python3-pip`

## Step 2: Set up VENV directory
`python3 -m venv mytestenv`

## Step 3: Move files into VENV directory
`mv main.py requirements.txt mytestenv/`

## Step 4: Start up VENV
`cd mytestenv/`
`source ./bin/activate`

## Step 5: Install requirements.txt using pip
`python3 -m pip install -r requirements.txt`

## Step 6: Run the script
`python3 main.py`

---
