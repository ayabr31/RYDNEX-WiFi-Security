def inject(networks):
    print("\n\033[93m[INFO] Simulating Fake Access Point Injection...\033[0m\n")

    if not networks:
        print("[WARNING] No real networks to clone. Creating a dummy one.")
        networks.append(("Aya_WiFi_Test", "00:11:22:33:44:55"))

    target_ssid = networks[0][0]
    fake_mac = "FA:KE:11:22:33:44"

    print(f"[+] Cloning SSID: {target_ssid}")
    print(f"[+] Injected Fake MAC: {fake_mac}")

    networks.append((target_ssid, fake_mac))

    return networks