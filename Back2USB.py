#Created By VoxelAxis Version 1.2


from importlib.metadata import files
import os
from pickle import GET
import shutil
from sqlite3.dbapi2 import Timestamp
from sys import version
import zipfile
from datetime import datetime
from colorama import Fore
from time import sleep

#-----------Helper Functions----------

#Software Version
def GetVersionNumber():
 return "Version 1.2"

#CMD Functions
def CLS():
 os.system('cls')

def run(cmd):
    """Run system command"""
    os.system(cmd)


def MemoryAppData():
    try:
        base = os.getenv("LOCALAPPDATA")
        
        if base is None:
            raise Exception("LOCALAPPDATA not found")

        app_folder = os.path.join(base, "Back2USB")
        os.makedirs(app_folder, exist_ok=True)

        return app_folder

    except Exception as e:
        print(f"{red}Failed: {e}")
        return None

def SaveUserFolders():
    appdata_path = MemoryAppData()

    if appdata_path is None:
        return
    else:
        save_file = os.path.join(appdata_path, "SaveData.txt")
        with open(save_file, "w") as f:
          for folder in UserFolders:
            f.write(folder + "\n")
    


def LoadUserFolders():
  appdata_path = MemoryAppData()

  if appdata_path is None:
    return
  save_file = os.path.join(appdata_path, "SaveData.txt")
  if not os.path.exists(save_file):
      return

  with open(save_file, "r") as f:
     for line in f:
        path = line.strip()
        if path and path not in UserFolders:
            UserFolders.append(path)

#Colours
red = Fore.RED
blue = Fore.BLUE
green = Fore.GREEN
purple = Fore.MAGENTA
cyan = Fore.CYAN

#Default Folders
DefaultFolders = [

    #os.path.join(os.path.expanduser("~"), "Downloads"), #Removed For Now because logically nobody needs (second hash incase i readd later)
    os.path.join(os.path.expanduser("~"), "Documents"),
    os.path.join(os.path.expanduser("~"), "Pictures"),
    os.path.join(os.path.expanduser("~"), "Videos")
]

#Users added folders
UserFolders = [
    
    
    ]

#Locators (For Verifying Locations)
downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
documents_path = os.path.join(os.path.expanduser("~"), "Documents")
pictures_path = os.path.join(os.path.expanduser("~"), "Pictures")
videos_path = os.path.join(os.path.expanduser("~"), "Videos")

#Retrieve Home
home = os.path.expanduser("~")
desktop = os.path.join(home, "Desktop")

AllFolders = DefaultFolders + UserFolders

#---------Logic-------------

def FolderChoosingMenu():
    CLS()
    print(f"{blue} Please type a file directory...")
    print("")
    print("")
    path = input(f" {blue}-> ")
    if(os.path.exists(path)):
     if path not in UserFolders:
      print(f"{green}Added Path {path}")
      UserFolders.append(path)
      SaveUserFolders()
      AllFolders = DefaultFolders + UserFolders
    
     else:
         print(f"{red}Path Already Exists")
    else:
     print(f"{red}Path Does Not Exist")



def FilesToZip(folder_name):
    CLS()
    LoadUserFolders()
    AllFolders = DefaultFolders + UserFolders
    Timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    print("Zipping Folders...")

    backup_file = os.path.join(desktop, f"{folder_name} {Timestamp}.zip")
    with zipfile.ZipFile(backup_file, 'w') as zf:
        for folder in AllFolders:
            if not os.path.exists(folder):
                print(f"{red}Skipping {folder} (Folder Inaccessible or Not Found)")
                continue

            folder_base = os.path.basename(folder)
            for root, dirs, files in os.walk(folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    try:
                        rel_path = os.path.join(folder_base, os.path.relpath(file_path, folder))
                        zf.write(file_path, rel_path)
                    except Exception as e:
                        print(f"{red}Failed to add {file_path}: {e}")

    print(f"{green}Finished zipping all folders to {backup_file}")

def ZipUserFolders(folder_name):
    CLS()
    LoadUserFolders()
    if not UserFolders:
      print(f"{red}Nothing to backup, please choose folders")
    else:
     Timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    print("Zipping Folders...")

    backup_file = os.path.join(desktop, f"{folder_name} {Timestamp}.zip")
    with zipfile.ZipFile(backup_file, 'w') as zf:
        for folder in UserFolders:
            if not os.path.exists(folder):
                print(f"{red}Skipping {folder} (Folder Inaccessible or Not Found)")
                continue

            folder_base = os.path.basename(folder)
            for root, dirs, files in os.walk(folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    try:
                        rel_path = os.path.join(folder_base, os.path.relpath(file_path, folder))
                        zf.write(file_path, rel_path)
                    except Exception as e:
                        print(f"{red}Failed to add {file_path}: {e}")
        print(f"{green}Finished zipping all folders to {backup_file}")


def FolderViewingMenu():
    CLS()
    LoadUserFolders()
    AllFolders = DefaultFolders + UserFolders
    for folder in AllFolders:
        print(folder)


def UserFolderViewingMenu():
    CLS()
    LoadUserFolders()
    if not UserFolders:
     print(f"{red}Folder has nothing to view...")
    else:
     for folder in UserFolders:
      print(folder)

def CreditsMenu():
    CLS()
    print(f"{cyan}Created By VoxelAxis")
    print("")
    print("")
    print(f"{cyan}Documentation For Folder Zipping by : angelotommy006 on Scribd")
    print("")


#----------------UI-------------------
def MainMenu():
    versionNo = GetVersionNumber()
    while True:
     CLS()
     print(f"""{purple}@@@@@@@   @@@@@@   @@@@@@@ @@@  @@@  @@@@@@  @@@  @@@  @@@@@@ @@@@@@@ 
 @@!  @@@ @@!  @@@ !@@      @@!  !@@ @@   @@@ @@!  @@@ !@@     @@!  @@@
 @!@!@!@  @!@!@!@! !@!      @!@@!@!    .!!@!  @!@  !@!  !@@!!  @!@!@!@ 
 !!:  !!! !!:  !!! :!!      !!: :!!   !!:     !!:  !!!     !:! !!:  !!!
 :: : ::   :   : :  :: :: :  :   ::: :.:: :::  :.:: :  ::.: :  :: : :: """)
     print("")
     print(f"{cyan} {versionNo}")
     print("")
     print("")
     print("")
     print(f" {blue}[1] Backup To Zip               [2] Choose Folders")
     print("")
     print(f" {blue}[3] View Folders                [4] View User Folders")
     print("")
     print(f" {blue}[5] Only Backup User Folders    [6] Credits")
     print("")
     print("")
     print(f" {red}[0] Kill Application")
     print("")
     print("")
     choice = input(f" {blue}-> ")
    
     if choice == "1":
       print(f"{green}Running Back2USB...")
       FilesToZip(f'Back2USB')
       input(f"{red}Press Enter...")
        
     elif choice == "2":
      print(f"{green}Opening Folder Choosing Menu...")
      FolderChoosingMenu()
      input(f"{red}Press Enter...")
  
     elif choice == "3":
      print(f"{green}Showing Folder Locations")
      FolderViewingMenu()
      input(f"{red}Press Enter...")
        
     elif choice == "4":
       print(f"{green}Showing User Folder Locations")
       UserFolderViewingMenu()
       input(f"{red}Press Enter...")

     elif choice == "5":
       print(f"{green}Running Back2USB...")
       ZipUserFolders(f'UserFolders-Back2USB')
       input(f"{red}Press Enter...")

     elif choice == "6":
      print(f"{green}Loading Credits...")
      CreditsMenu()
      input(f"{red}Press Enter...")

     elif choice == "0":
      print(f"{red}Killing Application...")
      break

     


MainMenu()
