import requests

def update_core(*args):
    res = requests.request("GET", "https://github.com/GaviTSRA/TSR-Console-Core")