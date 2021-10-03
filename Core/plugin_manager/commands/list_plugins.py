import os

class Plugin:
    def __init__(self, config):
        self.name = config["name"]
        self.id = config["id"]
        self.author = config["author"]
        self.path = self.id
        self.commands = config["commands"].split(",")
        self.is_core_plugin = False
        self.version = config["version"]

class CorePlugin(Plugin):
    def __init__(self, config):
        config["name"] = "[CORE]" + config["name"]
        config["author"] = "[CORE]"
        super().__init__(config)
        self.path = self.id
        self.is_core_plugin = True

def list_plugins(*args):
    plugins = []
    core_plugin_path = os.getenv('APPDATA') + "\\TSR Console\\Core\\"
    plugin_path = os.getenv('APPDATA') + "\\TSR Console\\Plugins\\"

    for plugin_name in os.listdir(core_plugin_path):
        if os.path.isdir(core_plugin_path + plugin_name):
            with open(core_plugin_path + plugin_name + "\\plugin.conf") as fi: #TODO error handling
                config_lines = fi.readlines()

            config = {}
            for line in config_lines:
                    config[line.split("=")[0]] = line.split("=")[1].replace("\n", "") #TODO error handling

            plugin = CorePlugin(config)
            plugins.append(plugin)

        else:
            print(f"Unsupported plugin '{plugin_name}': not a folder")
            continue

    for plugin_name in os.listdir(plugin_path):
        if os.path.isdir(plugin_path + plugin_name):
            with open(plugin_path + plugin_name + "\\plugin.conf") as fi: #TODO error handling
                config_lines = fi.readlines()

            config = {}
            for line in config_lines:
                    config[line.split("=")[0]] = line.split("=")[1].replace("\n", "") #TODO error handling

            plugin = Plugin(config)
            plugins.append(plugin)

        else:
            print(f"Unsupported plugin '{plugin_name}': not a folder")
            continue

    for plugin in plugins:
        if plugin.is_core_plugin:
            print("Core plugin: " + plugin.name)
        else:
            print("Plugin: " + plugin.name + " v" + plugin.version + " by " + plugin.author)