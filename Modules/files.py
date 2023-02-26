import re
import os

def get_all_disks():
    return "/"

def list_dir(path):
    dirs, files = [], []
    for object in path.iterdir():
        if object.is_dir():
            dirs.append(object.name)
        if object.is_file():
            files.append(object.name)
    return dirs, files

def has_permissions(path):
    return os.access(path, os.R_OK) and os.access(path, os.W_OK)
