import os, sys
from time import sleep
import subprocess as sb


#shit
fpath = os.path.dirname(os.path.realpath(__file__))
c=0

def exit():
    print(f"{bcolors.ENDC}{bcolors.HEADER}Exiting in 3...", end="\r");sleep(1)
    print(f"{bcolors.HEADER}Exiting in 2...", end="\r");sleep(1)
    print(f"{bcolors.HEADER}Exiting in 1...", end="\r");sleep(1)
    print(f"{bcolors.HEADER}Exiting in 0...", end="\r");sleep(0.4)
    sys.exit()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if int(os.getuid()) > 0:
    print(f"{bcolors.FAIL}Run this as root{bcolors.ENDC}")
    exit()

#code
bootan=[]
print(f"{bcolors.FAIL}Select bootanimation:\n{bcolors.ENDC}")

for file in os.listdir(fpath+"/ANIMATIONS"):
    bootan.append(file)

for an in bootan:
    c+=1
    print(f"{bcolors.HEADER}{c}{bcolors.ENDC} {an.replace('.zip','').upper()}")

ch=str(input(f"\n{bcolors.WARNING}>> {bcolors.ENDC}")).lower().replace(".zip","")

if ch.replace("\n","").isdigit():
    try:
        ach=bootan[int(ch)-1]
    except Exception as e:
        print(f"{bcolors.FAIL}Invalid input!! Check the log :'({bcolors.ENDC}")
        with open("anim.log","w") as log:
            log.write(str(e))
else:
    bch=f"{ch}.zip"
    ach=ch

    if ch+".zip" not in bootan:
        print(f"{bcolors.FAIL}No bootanimation found ({ch} in {bootan}){bcolors.ENDC}")
        exit()

print(f"\n{bcolors.OKBLUE}You choose {bcolors.UNDERLINE}{ach}{bcolors.ENDC}")
print(f"{bcolors.OKBLUE}Searching for magisk module folder...")

tmpcmd=sb.run("find /dev -type f -name sign_81818thisfileisafile.txt", shell=True, stdout=sb.PIPE, encoding="utf-8").stdout
folder=tmpcmd.split("\n")[0].replace("sign_81818thisfileisafile.txt","") #Is like my flag sign_81818thisfileisafile.txt

if folder=="":
    print(f"\n{bcolors.FAIL}Magisk module not found, please install it from magisk manager.{bcolors.ENDC}")
    exit()
else:
    print(f"\n{bcolors.OKGREEN}Magisk module found :D {folder}")
    print(f"Copiyng {bcolors.UNDERLINE}{ach}{bcolors.ENDC}{bcolors.OKGREEN} in module folder...\n")

try:
    os.system(f"sudo cp ANIMATIONS/{ach} {folder}system/media/bootanimation.zip")
except Exception as e:
    print(f"{bcolors.FAIL}Something shitty happened over here:\n{e}{bcolors.ENDC}")

print(f"\n{bcolors.WARNING}Tryng to play bootanimation...{bcolors.ENDC}")
os.system("bootanimation")
print(f"{bcolors.OKGREEN}Done\n")
exit()
