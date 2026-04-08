import time
import random

def abhay_banner():
    print("\033[96m" + "="*45)
    print("      DEVELOPED BY: ABHAY SHARMA          ")
    print("      PROJECT: OTP BYPASS & GEN PRO       ")
    print("="*45 + "\033[0m")

def start():
    print("\n[!] Connection secured by Abhay's Server...")
    time.sleep(1)
    print("\nSelect Country:\n[1] USA\n[2] UK\n[3] India")
    
    choice = input("\nChoice > ")
    print(f"\n[*] Abhay is generating a premium number for option {choice}...")
    time.sleep(2)
    print(f"\033[92m[✔] Number Assigned: +{random.randint(1,99)} {random.randint(100,999)}-XXXX\033[0m")
    
    print("\n[*] Waiting for OTP capture...")
    time.sleep(4)
    print(f"\n\033[93m[RECEIVED] Your OTP: {random.randint(111111, 999999)}\033[0m")

if __name__ == "__main__":
    abhay_banner()
    start()
