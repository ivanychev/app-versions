import os

class App(object):

    @staticmethod
    def __parse_name(fullpath):
         path, ext = os.path.splitext(fullpath)
         name = path.split("/")[-1]
         return name

    def __init__(self, path, name=None):
        self.path = path
        self.name = name if name is not None else App.__parse_name(path)

