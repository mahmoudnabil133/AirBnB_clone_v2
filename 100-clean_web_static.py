#!/usr/bin/python3
"compress web_stack locally"
import tarfile
from fabric.api import local
from datetime import datetime
import os


def do_clean(number=0):
    "compress"
    date = datetime.now().strftime('%Y%m%d%H%M%S')
    # print(os.path.exists("versions"))
    res = local("ls versions/")
    print(res)
