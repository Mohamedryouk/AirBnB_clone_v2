#!/usr/bin/python3
"""
Fabric script that generates a .tgz
archive from the contents of the web_static folder of your
AirBnB Clone repo, using the function do_pack.
"""

from os.path import isdir
from datetime import datetime
from fabric.api import local


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.

    The archive will be stored in the versions directory, and its name will
    include the current date and time.

    Returns:
        str: The path to the created .tgz archive if successful.
        None: If there was an error during the process.
    """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if not isdir("versions"):
            local("mkdir versions")
        archive_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(archive_name))
        return archive_name
    except Exception:
        return None
