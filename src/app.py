import os
from tools import recursive_files
from operator import methodcaller

class App(object):

    @staticmethod
    def _find_plists(root):
        paths = recursive_files(root, depth=3, name="Info.plist")
        return sorted(paths, key=methodcaller("count", "/"))

    def __init__(self, path, name=None):
        self.path = path
        self.name = name if name is not None else os.path.basename(path)
        self.plists = App._find_plists(self.path)

    def __str__(self):
        return "[{} -> {}, plists:{}]".format(self.path, self.name, self.plists)
