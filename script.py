import os
import subprocess
import shutil



def create_reaper_project():


# Paths
    repertory = "D:\Enregistrements\\2023"
    reaper_executable_path = "D:\Program Files (x86)\\reaper.exe"


# Project name
    project_name = input("Veuillez choisir un nom pour votre projet.")
    project_path = os.path.join(repertory, project_name)

    print(project_path)


# Test -- Does the folder already exist ?
    if os.path.exists( project_path ) and os.path.isdir( project_path ) :
        folderDontExist = False
    else :
        folderDontExist = True

    try :
        os.makedirs( project_path, exist_ok = folderDontExist )
        os.chdir( project_path )
    except OSError as e:
        print (f"Impossible de créer le projet car : {e}")


# File copy
    origin_file = "D:\Python\Actionbar\\reaper_files\\empty.rpp"
    target_file = project_path + '\\' + project_name + '.rpp'
    shutil.copy(origin_file, target_file)


# Reaper
    try:
        subprocess.run([reaper_executable_path, target_file])

    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution de Reaper : {e}")


# Function call
if __name__ == "__main__":
    create_reaper_project()
