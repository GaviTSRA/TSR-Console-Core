from os import name, system

def cls(*args):
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')