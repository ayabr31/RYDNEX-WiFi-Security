def detect(networks):
    print("\n\033[94m[INFO] Running Detection Engine...\033[0m\n")
    
    ssid_dict = {}
    is_attack = False

    for ssid, mac in networks:
        if ssid not in ssid_dict:
            ssid_dict[ssid] = []
        ssid_dict[ssid].append(mac)

    for ssid, macs in ssid_dict.items():
        if len(macs) > 1:
            print(f"\033[91m[ALERT] EVIL TWIN DETECTED: SSID '{ssid}' is using multiple MAC addresses!\033[0m")
            for m in macs:
                print(f" -> Device MAC: {m}")
            is_attack = True
            
    if not is_attack:
        print("\033[92m[OK] Network environment looks safe.\033[0m")