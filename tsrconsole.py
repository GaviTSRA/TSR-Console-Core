import os
from importlib import import_module
if __name__ == "__main__":
    try: 
        from colorama import Fore
        print(Fore.GREEN + "Colorama extension loaded" + Fore.RESET)
    except ImportError:
        print("Colorama extension not loaded")
        class Fore:
            BLACK = ""
            BLUE = ""
            CYAN = ""
            GREEN = ""
            MAGENTA = ""
            RED = ""
            WHITE = ""
            YELLOW = ""
            LIGHTBLACK_EX = ""
            LIGHTBLUE_EX = ""
            LIGHTCYAN_EX = ""
            LIGHTGREEN_EX = ""
            LIGHTMAGENTA_EX = ""
            LIGHTRED_EX = ""
            LIGHTWHITE_EX = ""
            LIGHTYELLOW_EX = ""
            RESET = ""

class Plugin:
    def load(self, config):
        try:
            self.name = config["name"]
            self.id = config["id"]
            self.author = config["author"]
            self.path = self.id
            self.commands = config["commands"].split(",")
            self.is_core_plugin = False
            self.version = config["version"]
            return True
        except KeyError as err:
            if "name" in config:
                print(f"{Fore.LIGHTRED_EX}Failed to load '{Fore.WHITE + self.name + Fore.LIGHTRED_EX}': Required key '{Fore.WHITE + err.args[0] + Fore.LIGHTRED_EX}' not found in plugin config - Exiting{Fore.RESET}")
            else:
                print(f"{Fore.LIGHTRED_EX}Name key not found for a plugin - Exiting{Fore.RESET}")
                return False

class CorePlugin(Plugin):
    def load(self, config):
        config["name"] = "[CORE]" + config["name"]
        config["author"] = "[CORE]"
        if not super().load(config): return False
        self.is_core_plugin = True
        return True

def init():
    global plugins
    plugins = []
    core_plugin_path = ".\\core\\"  #os.getenv('APPDATA') + "\\TSR Console\\Core\\"
    plugin_path = ".\\plugins\\" #os.getenv('APPDATA') + "\\TSR Console\\Plugins\\"

    for plugin_name in os.listdir(core_plugin_path):
        if os.path.isdir(core_plugin_path + plugin_name):
            with open(core_plugin_path + plugin_name + "\\plugin.conf") as fi: #TODO error handling
                config_lines = fi.readlines()

            config = {}
            for line in config_lines:
                    config[line.split("=")[0]] = line.split("=")[1].replace("\n", "") #TODO error handling

            plugin = CorePlugin()
            if plugin.load(config):
                plugins.append(plugin)
                print(f"{Fore.GREEN}Loaded plugin: '{Fore.WHITE + plugin.name + Fore.GREEN}'{Fore.RESET}")

        else:
            print(f"{Fore.LIGHTRED_EX}Unsupported plugin '{Fore.WHITE + plugin_name + Fore.LIGHTRED_EX}': not a folder{Fore.RESET}")
            continue

    for plugin_name in os.listdir(plugin_path):
        if os.path.isdir(plugin_path + plugin_name):
            with open(plugin_path + plugin_name + "\\plugin.conf") as fi: #TODO error handling
                config_lines = fi.readlines()

            config = {}
            for line in config_lines:
                    config[line.split("=")[0]] = line.split("=")[1].replace("\n", "") #TODO error handling

            plugin = Plugin()
            if plugin.load(config):
                plugins.append(plugin)
                print(f"{Fore.GREEN}Loaded plugin: '{Fore.WHITE + plugin.name + Fore.GREEN}' by {Fore.WHITE + plugin.author + Fore.RESET}")

        else:
            print(f"Unsupported plugin '{plugin_name}': not a folder")
            continue

def main():  
    args = input(">").split(" ") #TODO add support for "Text with spaces"
    for plugin in plugins:
        found = False
        for command in plugin.commands:
            if command == args[0]:
                found = True

        if args[0] in plugin.commands:
            if plugin.is_core_plugin:
                imported = import_module("core." + plugin.path + ".commands." + args[0])
            else:
                imported = import_module("plugins." + plugin.path + ".commands." + args[0])
            args.remove(args[0])

            print(args)
            imported.run(plugins, args)
            break
    else:
        print(f"{Fore.LIGHTRED_EX}Command not found{Fore.RESET}")

if __name__ == "__main__":
    init()
    while True:
        main()