#!/usr/bin/python3
"""
Fabric script that generates .tgz archive
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    generates a .tgz archive
    """
    try:
        local('mkdir -p versions')
        date_format = "%Y%m%d%H%M%S"
        arch_path = "version/web_static_{}.tgz".format(
            datetime.now().strftime(date_format))
        local('tar -cvzf {} web_static'.format(arch_path))
        local('web_static packed: {} -> {}'.format(arch_path,
              os.path.getsize(arch_path)))
    except:
        return None
