import os
import platform
import datetime

def check_system():
    print("=" * 40)
    print("      SYSTEM HEALTH MONITOR      ")
    print("=" * 40)
    print(f"Timestamp : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"OS        : {platform.system()} {platform.release()}")
    print(f"Machine   : {platform.machine()}")
    print("=" * 40)
    
    # Cek koneksi internet sederhana
    response = os.system("ping -c 1 8.8.8.8" if platform.system() != "Windows" else "ping -n 1 8.8.8.8 > nul")
    if response == 0:
        print("Network Status: ONLINE")
    else:
        print("Network Status: OFFLINE")

if __name__ == "__main__":
    check_system()