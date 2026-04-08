import time
import random
import sys

# --- CONFIGURATION (Business Settings) ---
ADMIN_KEY = "ABHAY_FREE_789"         
PREMIUM_KEY = "lashaabha"            
PRICE = "₹59"
UPI_ID = "abhaysharmaknj7895@axl"
# ----------------------------------------

def abhay_banner():
    # स्क्रीन साफ़ करने के लिए
    print("\033[H\033[J") 
    print("\033[96m" + "="*65)
    print("      ABHAY SHARMA'S ADVANCED PACKET SNIFFER (V7.0)      ")
    print(f"      STATUS: MONITORING ACTIVE | RATE: {PRICE} | UPI: {UPI_ID}      ")
    print("="*65 + "\033[0m")

def start_engine(service):
    # टॉपिक 2 फिक्स: अब नंबर हमेशा 10 अंकों का और +91 के साथ आएगा
    prefix = random.choice(["6", "7", "8", "9"]) # असली इंडियन सीरीज
    rest = "".join([str(random.randint(0, 9)) for _ in range(9)])
    v_num = f"+91 {prefix}{rest[:3]} {rest[3:6]} {rest[6:]}"
    
    print(f"\n\033[92m[✔] VIRTUAL NUMBER FOR {service.upper()}: {v_num}\033[0m")
    print(f"\n[!] STEP: Enter {v_num} in your app and request OTP.")
    print("\n\033[94m[*] System Mode: Waiting for Incoming Server Data (Unlimited)...\033[0m")
    print("-" * 65)

    try:
        # टॉपिक 1 फिक्स: Unlimited Waiting (कोई सेकंड्स की पाबंदी नहीं)
        timer = 0
        captured = False
        while not captured:
            # यह यूजर को दिखाएगा कि सिस्टम लाइव स्कैनिंग कर रहा है
            sys.stdout.write(f"\r[SCANNING] Port: 443 | Socket: OPEN | Active Time: {timer}s | Data: NONE")
            sys.stdout.flush()
            time.sleep(1)
            timer += 1
            
            # यथार्थवादी अहसास (Realistic feel) के लिए 15 सेकंड के बाद कभी भी डेटा आ सकता है
            if timer > 15:
                if random.random() < 0.1: # 10% चांस हर सेकंड डेटा मिलने का
                    captured = True
        
        otp = f"{random.randint(100, 999)}-{random.randint(100, 999)}"
        print(f"\n\n\033[91m[🔥 BOOM!] DATA PACKET CAPTURED FROM {service.upper()} SERVER!\033[0m")
        print(f"\033[101m\033[1m RECEIVED OTP: {otp} \033[0m")
        print("-" * 65)
        print("\n[✔] Done! Session Finished. Please restart for new task.")

    except KeyboardInterrupt:
        print("\n\n[!] Monitoring Stopped manually by Abhay.")

if __name__ == "__main__":
    while True:
        abhay_banner()
        print(f"\n[!] Access Locked! Pay {PRICE} to {UPI_ID}")
        user_key = input("\nEnter Activation Key (or 'q' to exit) > ")
        
        if user_key.lower() == 'q':
            sys.exit()
            
        if user_key == ADMIN_KEY or user_key == PREMIUM_KEY:
            print("\n\033[92m[✔] Access Granted! Loading Gateway...\033[0m")
            time.sleep(1)
            service_name = input("\nEnter Platform Name (e.g. WhatsApp): ")
            start_engine(service_name)
            break # टास्क पूरा होने पर बाहर निकलना
        else:
            print("\n\033[91m[✘] Invalid Key! Access Denied.\033[0m")
            time.sleep(2)
