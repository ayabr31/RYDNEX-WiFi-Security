import os
import sys
import time
import pyfiglet

#  Start AUTO logging
from modules.logger import start_logging
start_logging()

#  Import modules
from modules import (
    wifi_scanner, 
    fake_injector, 
    evil_twin_detector, 
    handshake_simulator, 
    handshake_detector,
    keylogger,
    visualizer
)

#  Clear terminal
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#  Banner
def show_banner():
    banner = pyfiglet.figlet_format("RYDNEX", font="slant")

    for line in banner.split("\n"):
        print("\033[91m" + line + "\033[0m")
        time.sleep(0.07)  

    print("\033[95m" + "="*60)
    print("   Wireless Security & Detection Toolkit")
    print("   Cybersecurity Project | USTO-MB")
    print("   By : Brinis Aya Zohra | Bekhlifa Nourelimene")
    print("="*60 + "\033[0m")

#  Menu
def show_menu():
    print("\n\033[94m[MAIN MENU]\033[0m")
    print("1. Scan & Detect Evil Twin")
    print("2. Simulate & Analyze WPA2 Handshake")
    print("3. Start Keylogger")
    print("4. Show Network Visualization")
    print("5. Clear Screen")
    print("6. Exit")

# Main Logic
def main():
    clear_screen()
    show_banner()

    while True:
        show_menu()
        choice = input("\n\033[93mSelect an option (1-6): \033[0m")

        #  Evil Twin Detection
        if choice == "1":
            print("\n" + "-"*40)
            print("[INFO] Running Evil Twin Detection...")

            networks = wifi_scanner.scan()
            mixed = fake_injector.inject(networks)
            evil_twin_detector.detect(mixed)

            print("-"*40)
            input("\n\033[90mPress Enter to return to menu...\033[0m")

        #  Handshake Simulation
        elif choice == "2":
            print("\n" + "-"*40)
            print("[INFO] Simulating WPA2 Handshake...")

            handshake_simulator.simulate_attack()
            handshake_detector.analyze()

            print("-"*40)
            input("\n\033[90mPress Enter to return to menu...\033[0m")

        #  Keylogger
        elif choice == "3":
            print("\n" + "-"*40)
            keylogger.start()
            print("-"*40)
            input("\nKeylogger stopped. Press Enter to continue...")

        #  Visualization
        elif choice == "4":
            print("\n" + "-"*40)
            visualizer.show()
            print("-"*40)
            input("\nClose graph and press Enter...")

        #  Clear screen
        elif choice == "5":
            clear_screen()
            show_banner()

        # Exit
        elif choice == "6":
            print("\n\033[92m[✔] Exiting... \033[0m")
            break

        #  Invalid
        else:
            print("\033[91m[ERROR] Invalid choice!\033[0m")

# Run
if __name__ == "__main__":
    main()
    clear_screen()
    show_banner()
    print("\033[92m[✔] System initialized successfully.\033[0m")
