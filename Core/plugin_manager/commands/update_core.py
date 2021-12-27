import shutil
import os
import urllib.request
import zipfile
import time
from tsru import LoadingSpinner

def run(plugins, *args):
    installation_dir = ".\\"

    # TODO check if an update is available

    spinner = LoadingSpinner("Starting core update")
    if not os.path.exists(installation_dir + "update"): os.mkdir(installation_dir + "update")
    spinner.stop()

    spinner = LoadingSpinner("Downloading update")
    urllib.request.urlretrieve("https://github.com/GaviTSRA/TSR-Console-Core/archive/refs/heads/master.zip", ".\\update\\core.zip")
    spinner.stop()

    spinner = LoadingSpinner("Extracting update")
    with zipfile.ZipFile(installation_dir + "update\\core.zip", 'r') as zip_ref:
        zip_ref.extractall(installation_dir + "update\\core\\")
    spinner.stop()

    spinner = LoadingSpinner("Removing old files")
    shutil.rmtree(installation_dir + "Core")
    spinner.stop()

    spinner = LoadingSpinner("Copying new files")
    shutil.move(installation_dir + "update\\core\\TSR-Console-Core-master\\Core", installation_dir)
    spinner.stop()

    spinner = LoadingSpinner("Cleaning up")
    shutil.rmtree(installation_dir + "update")
    spinner.stop()

    time.sleep(0.1)
    print("Update completed, please restart tsrconsole")