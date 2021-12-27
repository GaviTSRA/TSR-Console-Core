def run(plugins, *args):
    for plugin in plugins:
        print(plugin.name + "(" + plugin.id + ")" + " v" + plugin.version + " by " + plugin.author)