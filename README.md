# RYDNEX - WiFi Security Simulation Toolkit

RYDNEX is a cybersecurity project designed to simulate wireless attacks and demonstrate detection techniques in a controlled environment.

 **Important:**  
This project is a **simulation only** and does NOT perform real attacks.  
It is intended strictly for **educational and demonstration purposes**.

---

##  Project Objective

The goal of this project is to:

- Understand how wireless attacks like **Evil Twin** work
- Simulate **WPA2 handshake capture**
- Demonstrate how detection systems identify suspicious WiFi behavior
- Provide a visual and interactive cybersecurity dashboard

---

##  Features

### 📡 WiFi Scanner (Simulation)
- Generates a list of nearby WiFi networks (simulated)
- Displays SSID and MAC addresses

---

###  Evil Twin Detection
- Detects duplicate SSIDs with different MAC addresses
- Identifies suspicious networks
- Simulates how attackers create fake WiFi access points

---

###  WPA2 Handshake Simulation
- Simulates deauthentication attack scenario
- Generates EAPOL handshake steps
- Saves capture data into a file

---

###  Handshake Analysis
- Checks if a valid handshake was captured
- Determines if the attack simulation succeeded

---

###  Keylogger (Demonstration)
- Records keyboard input locally
- Used to illustrate post-attack risks

---

###  Network Visualization
- Graph-based representation of attack scenario
- Shows interaction between:
  - Attacker
  - Victim
  - Real Router

---

###  Logging System
- Records system activity
- Stores logs in `data/system_logs.txt`

---
## 🖥️ Technologies Used

- Python
- NetworkX (Graph visualization)
- Matplotlib
- Pynput

---

## 🚀 How to Run

### Install dependencies

```bash
pip install -r requirements.txt 
```
 ### terminal version
 ```bash
python3 rydnex.py
```






### Project Structure
```bash
RYDNEX-WiFi-Security/
│
├── rydnex.py
├── modules/
│   ├── wifi_scanner.py
│   ├── fake_injector.py
│   ├── evil_twin_detector.py
│   ├── handshake_simulator.py
│   ├── handshake_detector.py
│   ├── keylogger.py
│   ├── logger.py
│   ├── visualizer.py
│
├── data/
│   ├── capture.txt
│   ├── system_logs.txt
│   ├── keylogs.txt
```




### Disclaimer

This project is developed for academic and educational purposes only.

- No real network attacks are performed  
- No unauthorized access is intended  
- All scenarios are simulated  
