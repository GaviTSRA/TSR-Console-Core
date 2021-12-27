from os import name, system

def run(plugins, *args):
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')