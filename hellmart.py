import requests
from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor
import threading
import sys
import os

default_wordlist = 'wordlist.txt'
output_file = 'results.txt'

print_lock = threading.Lock()
file_lock = threading.Lock()

#Reuse TCP connection
##Reuse session
session = requests.Session()

def check_directory(url , directory):
    full_url = urljoin(url , directory)

    try:
        ##Sending Get Requests
        response = session.get(full_url , timeout=5)
        

        if response.status_code == 200:
            result = f"[+] Found directory : {full_url}"
            with print_lock:
                print(result)
            with file_lock:
                with open(output_file , 'a') as f:
                    f.write(full_url + "\n")

        elif response.status_code == 403:
             result = f"[-] forbidden : {full_url}"
             with print_lock:
                 print(result)   
        
        else:
            result = f"[x] Not found : {full_url}"
            with print_lock:
                print(result)


    except requests.exceptions.RequestException as e:
        erro_msg = f"[-] Error : {e}"
        with print_lock:
            print(erro_msg)
        with file_lock:
            with open(output_file , 'a') as f:
                f.write(erro_msg + "\n")


def main():
  try:
    ##We are fu3kers
    banner()
    
    ##Taking user input url or worlist(if have)
    url = input("Enter a url (e.g.https://google.com) : ").strip();
    wordlist = input("Enter the path of the wordlist (Press enter for default): ").strip();

    ##Validate url
    if not url.startswith('http'):
            print("URL must start with 'http' or 'https'.")
            return

    if wordlist:
        try:
            with open (wordlist , 'r') as file:
                wordlist = [line.strip() for line in file.readlines()]
                print(f"[+] Loaded custom wordlist.")
        except FileNotFoundError:
            print("[+] Error Wordlist not found!!")
            return
    else:
        try:
            ##Loaded Default wordlist
            with open (default_wordlist , 'r') as file:
                wordlist = [line.strip() for line in file.readlines()]
                print("[+] Loaded Default wordlist.")
        except FileNotFoundError:
            print(f"[+] Error : Default Wordlist file '{default_wordlist}' not found")
            return

    #Clear previous results
    open(output_file , 'w').close()

    ##Fuzzing the directories of this url
    print(f"\n[+] Fuzzing {url} for directories...\n")
    
    executor = ThreadPoolExecutor(max_workers=50)
    try:
        for directory in wordlist:
            executor.submit(check_directory, url, directory)
        executor.shutdown(wait=True)
        print(f"\n\n[+] Fuzzing Completed. Results saved in '{output_file}'.")
    
    except KeyboardInterrupt:
        print("\n[+] Process Interrupted. Waiting for active threads to finish...")
        executor.shutdown(wait=True)
        print("[+] All threads finished. Exiting safely.")
        sys.exit(0)
    
  except KeyboardInterrupt:
        # Graceful exit on Ctrl+C
        print("\n[+] Process Interrupted. Exiting safely...")
        sys.exit(0)  # Exit the program cleanly


def banner():
    print('''
          
 ██░ ██ ▓█████  ██▓     ██▓     ███▄ ▄███▓ ▄▄▄       ██▀███  ▄▄▄█████▓
▓██░ ██▒▓█   ▀ ▓██▒    ▓██▒    ▓██▒▀█▀ ██▒▒████▄    ▓██ ▒ ██▒▓  ██▒ ▓▒
▒██▀▀██░▒███   ▒██░    ▒██░    ▓██    ▓██░▒██  ▀█▄  ▓██ ░▄█ ▒▒ ▓██░ ▒░
░▓█ ░██ ▒▓█  ▄ ▒██░    ▒██░    ▒██    ▒██ ░██▄▄▄▄██ ▒██▀▀█▄  ░ ▓██▓ ░ 
░▓█▒░██▓░▒████▒░██████▒░██████▒▒██▒   ░██▒ ▓█   ▓██▒░██▓ ▒██▒  ▒██▒ ░ 
 ▒ ░░▒░▒░░ ▒░ ░░ ▒░▓  ░░ ▒░▓  ░░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░  ▒ ░░   
 ▒ ░▒░ ░ ░ ░  ░░ ░ ▒  ░░ ░ ▒  ░░  ░      ░  ▒   ▒▒ ░  ░▒ ░ ▒░    ░    
 ░  ░░ ░   ░     ░ ░     ░ ░   ░      ░     ░   ▒     ░░   ░   ░      
 ░  ░  ░   ░  ░    ░  ░    ░  ░       ░         ░  ░   ░              
                                                                      
                  BY MR V3RUS
            YOUTUBE : @Pr3fessorV3rus
    FAST MULTI-THREADED DIRECTORY FUZZING TOOL
      BUILT FOR ETHICAL HACKERS AND RECON
             JAI HIND | JAI BHARAT



    ''')

if __name__ == "__main__":
    main()
