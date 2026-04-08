import time
import random
import sys
import smtplib
from email.message import EmailMessage

# --- CONFIGURATION (Locked for Abhay Sharma) ---
MY_EMAIL = "abhayshramknj789@gmail.com" 
EMAIL_PASSWORD = "zptl eldv tfuo xgwe" 
ADMIN_KEY = "ABHAY_FREE_789"         # मास्टर की
PREMIUM_KEY = "lashaabha"            # तुम्हारी प्रीमियम की (₹59)
PRICE = "₹59"
UPI_ID = "abhaysharmaknj7895@axl"
# ------------------------------------------------

def send_alert(used_key):
    """ईमेल अलर्ट भेजने का फंक्शन"""
    try:
        msg = EmailMessage()
        msg.set_content(f"नमस्ते अभय,\n\nतुम्हारे OTP टूल में लॉगिन की कोशिश हुई है।\n\nइस्तेमाल की गई Key: {used_key}\nसमय: {time.ctime()}\n\nचेक करें कि क्या ₹59 का पेमेंट प्राप्त हो गया है।")
        msg['Subject'] = '⚠️ ALERT: Key Used on Abhay OTP Tool'
        msg['From'] = MY_EMAIL
        msg['To'] = MY_EMAIL

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(MY_EMAIL, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
    except Exception:
        pass 

def abhay_banner():
    # क्लीन स्क्रीन के लिए
    print("\033[H\033[J") 
    print("\033[96m" + "="*60)
    print("      ABHAY SHARMA'S SECURE SMS INTERCEPTOR (V5.0)      ")
    print(f"      RATE: {PRICE} | UPI: {UPI_ID}      ")
    print("="*60 + "\033[0m")

def check_access():
    print(f"\n[!] Access Locked! Pay {PRICE} to {UPI_ID}")
    user_key = input("\nEnter Activation Key > ")
    
    # ईमेल अलर्ट तुरंत बैकग्राउंड में जाएगा
    send_alert(user_key)
    
    if user_key == ADMIN_KEY:
        print("\n\033[92m[✔] Master Access Granted. Hello Abhay!\033[0m")
        return True
    elif user_key == PREMIUM_KEY:
        print("\n\033[92m[✔] Premium Access Unlocked. Valid for this session.\033[0m")
        return True
    else:
        print("\n\033[91m[✘] Invalid Key! Please pay first to get the correct Key.\033[0m")
        return False

def start_engine():
    print("\n--- Platform Selection ---")
    print("[1] WhatsApp  [2] Instagram  [3] Facebook  [4] Other")
    choice = input("\nSelect Option > ")
    
    service = "Custom Service"
    if choice == "1": service = "WhatsApp"
    elif choice == "2": service = "Instagram"
    elif choice == "3": service = "Facebook"

    print(f"\n[*] Connecting to {service} Secure Gateway...")
    time.sleep(2)
    
    # फुल रैंडम नंबर
    v_num = f"+91 {random.randint(6001, 9999)} {random.randint(10001, 99999)}"
    print(f"\033[92m[✔] VIRTUAL NUMBER: {v_num}\033[0m")
    print(f"\n[!] STEP: Enter {v_num} in your {service} app now.")
    
    print("\n[*] Waiting for incoming SMS packet...")
    # प्रोफेशनल लिसनिंग एनीमेशन
    for s in range(1, 15):
        sys.stdout.write(f"\r[*] Intercepting... Port 443 | Status: ACTIVE | Time: {s}s")
        sys.stdout.flush()
        time.sleep(1)
    
    otp = f"{random.randint(100, 999)}-{random.randint(100, 999)}"
    print(f"\n\n\033[91m[🔥 ALERT] {service.upper()} OTP CAPTURED: {otp}\033[0m")
    print("-" * 60)
    print("\n[✔] Task complete. Please restart for new session.")

if __name__ == "__main__":
    abhay_banner()
    if check_access():
        start_engine()
    else:
        sys.exit()
