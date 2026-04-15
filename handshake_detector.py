def analyze():
    print("\n\033[94m[INFO] Analyzing Capture File for WPA Handshake...\033[0m\n")
    
    try:
        with open("data/capture.txt", "r") as f:
            content = f.read()
            
            if "EAPOL_HANDSHAKE" in content:
                print("\033[92m[✔] VALID HANDSHAKE DETECTED!\033[0m")
                print("[ANALYSIS] Found EAPOL frames. Ready for Offline Brute-force Attack simulation.")
            else:
                print("\033[91m[X] ERROR: Incomplete Handshake. Missing EAPOL frames.\033[0m")
    except FileNotFoundError:
        print("\033[91m[ERROR] No capture file found. Run Simulator first!\033[0m")