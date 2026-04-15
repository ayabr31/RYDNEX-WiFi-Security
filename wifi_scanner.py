import subprocess

def scan():
    print("\033[94m[INFO] Scanning real WiFi networks...\033[0m\n")
    
  
    cmd = "nmcli -t -f SSID,BSSID dev wifi list"
    result = subprocess.getoutput(cmd)
    
    networks = []
    lines = result.split("\n")

    for line in lines:
        if line.strip() and ":" in line:
           
       
            parts = line.split(":")
            
       
            mac = ":".join(parts[-6:])
        
            ssid = ":".join(parts[:-6])

            if not ssid:
                ssid = "[Hidden Network]"

            networks.append((ssid, mac))
            print(f"SSID: {ssid.ljust(25)} | Real MAC: {mac}")
            
    return networks