from importlib.metadata import files
import os
import shutil
from sqlite3.dbapi2 import Timestamp
import zipfile
from datetime import datetime
from colorama import Fore

#-----------Helper Functions----------

#CMD Functions
def CLS():
 os.system('cls')

def run(cmd):
    """Run system command"""
    os.system(cmd)


#Colours
red = Fore.RED
blue = Fore.BLUE
green = Fore.GREEN
purple = Fore.MAGENTA
cyan = Fore.CYAN

#Default Folders
DefaultFolders = [

    os.path.join(os.path.expanduser("~"), "Downloads"),
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
      print(f"{green}Added Path {path}")
      UserFolders.append(path)
      AllFolders = DefaultFolders + UserFolders
    else:
        print(f"{red}Path Does Not Exist")



def FilesToZip(folder_name):
    CLS()
    AllFolders = DefaultFolders + UserFolders
    Timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    print("Zipping Folder...")
    folder_path = AllFolders
    backup_file = os.path.join(desktop, f"{folder_name} {Timestamp}.zip")

    with zipfile.ZipFile(backup_file, 'w') as zf:
        for folder in AllFolders :
         for root, dirs, files in os.walk(folder):
          for file in files:
            file_path = os.path.join(root, file)
            zf.write(file_path, os.path.relpath(file_path, folder))


def FolderViewingMenu():
    CLS()
    AllFolders = DefaultFolders + UserFolders
    for folder in AllFolders:
        print(folder)

def CreditsMenu():
    CLS()
    print("Created By VoxelAxis")
    print("")
    print("")
    print("Documentation For Folder Zipping by : angelotommy006 on Scribd")
    print("")
    print("")
    print("Find us at VoxPy Solutions! https://discord.gg/9YvcRerxjz")


#----------------UI-------------------
def MainMenu():
    while True:
     CLS()
     print(f"""{purple}@@@@@@@   @@@@@@   @@@@@@@ @@@  @@@  @@@@@@  @@@  @@@  @@@@@@ @@@@@@@ 
 @@!  @@@ @@!  @@@ !@@      @@!  !@@ @@   @@@ @@!  @@@ !@@     @@!  @@@
 @!@!@!@  @!@!@!@! !@!      @!@@!@!    .!!@!  @!@  !@!  !@@!!  @!@!@!@ 
 !!:  !!! !!:  !!! :!!      !!: :!!   !!:     !!:  !!!     !:! !!:  !!!
 :: : ::   :   : :  :: :: :  :   ::: :.:: :::  :.:: :  ::.: :  :: : :: """)
     print("")
     print("")
     print("")
     print("")
     print("")
     print(f" {blue}[1] Backup To Zip               [2] Choose Folders")
     print("")
     print(f" {blue}[3] View Folders                [4] Credits")
     print("")
     print(f" {red}[0] Kill Application")
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
      print(f"{green}Loading Credits...")
      CreditsMenu()
      input(f"{red}Press Enter...")

     elif choice == "0":
      print(f"{red}Killing Application...")
      input(f"{red}Press Enter...")
      break

     


MainMenu()
