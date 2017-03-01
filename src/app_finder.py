from toolz.curried import *
from collections import namedtuple
from tools import recursive_files
from app import App
import os

def is_app_filter(maybe):
    return os.path.basename(maybe).endswith(".app")

def app_paths(root_path):
    files = recursive_files(root_path, depth=2, dirs=True)
    return filter(is_app_filter, files)

def make_apps(root_path="/Applications"):
    paths = app_paths(root_path)
    apps = list(map(App, paths))
