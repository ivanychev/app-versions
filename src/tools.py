import subprocess
from toolz.curried import *

def _form_command(root_path, dirs, depth, name):
    find_type = "d" if dirs else "f"
    command = ["find"]
    command.append(" \"{}\"".format(root_path))
    command.append("" if name is None else " -name \"{}\" ".format(name))
    command.append(" -maxdepth {}".format(depth))
    command.append(" -type {}".format(find_type))
    return "".join(command)

def recursive_files(root_path, dirs=False, depth=2, name=None):
    cmd = _form_command(root_path, dirs, depth, name)
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    output, _ = process.communicate()
    return output.splitlines()
