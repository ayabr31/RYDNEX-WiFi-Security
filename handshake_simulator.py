import time
import random

def simulate_attack():
    print("\n\033[95m[STEP 1] Starting Deauthentication Attack...\033[0m")
    print("[INFO] Sending 64 deauth packets to target client...")
    time.sleep(2) 
    
    print("\n\033[95m[STEP 2] Waiting for Client Re-authentication...\033[0m")
    packets = ["Beacon", "Probe Request", "Association Request", "EAPOL 1/4", "EAPOL 2/4", "EAPOL 3/4", "EAPOL 4/4"]
    
    for pkt in packets:
        time.sleep(0.5)
        if "EAPOL" in pkt:
            print(f"\033[92m[CAPTURE] Captured: {pkt}\033[0m")
        else:
            print(f"[SNIFF] Captured: {pkt}")

    print("\n\033[92m[SUCCESS] WPA2 Handshake captured and saved to data/capture.txt\033[0m")
    
    with open("data/capture.txt", "a") as f:
        f.write("\n\nFRAME_TYPE: BEACON\n")
        f.write("FRAME_TYPE: EAPOL_HANDSHAKE\n")
        f.write("BSSID: 9A:DE:C4:A6:18:37\n")
