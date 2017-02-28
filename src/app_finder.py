from toolz.curried import *
import os
from collections import namedtuple

APP_ROOT = "/Applications"

App = namedtuple("App", ["root", "app"])

def recursive_files(root_path, dirs=False):
    for root, dirnames, filenames in os.walk(root_path):
        for f in (filenames if not dirs else dirnames):
            yield App(root, f)

def is_app_filter(maybe):
    return maybe.app.endswith(".app")

def app_paths(root_path):
    files = recursive_files(root_path)
    return filter(is_app_filter, files)
