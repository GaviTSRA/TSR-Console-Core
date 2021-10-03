import shutil
import os
import urllib.request
import zipfile

def update_core(*args):
    installation_dir = os.getenv("APPDATA") + "\\TSR Console\\"

    # TODO check if an update is available

    print("Starting core update...")
    if not os.path.exists(installation_dir + "update"): os.mkdir(installation_dir + "update")

    print("Downloading updated core...")
    urllib.request.urlretrieve("https://github.com/GaviTSRA/TSR-Console-Core/archive/refs/heads/master.zip", os.getenv("APPDATA") + "\\TSR Console\\update\\core.zip")
    print("Done")  

    print("Extracting...")
    with zipfile.ZipFile(installation_dir + "update\\core.zip", 'r') as zip_ref:
        zip_ref.extractall(installation_dir + "update\\core\\")
    print("Done")

    print("Removing old files...")
    shutil.rmtree(installation_dir + "Core")
    print("Done")

    print("Copying new files...")
    shutil.move(installation_dir + "update\\core\\TSR-Console-Core-master\\Core", installation_dir)
    print("Done")

    print("Cleaning up...")
    shutil.rmtree(installation_dir + "update")
    print("Done")

    print("Update completed")