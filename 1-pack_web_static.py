#!/usr/bin/python3
"""
a Fabric script that generates a .tgz
archive from the contents of the web_static folder of your
AirBnB Clone repo, using the function do_pack.
"""


from os.path import isdir
from datetime import datetime
from fabric import local


def do_pack():
    """
    generates tgz
    """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        Name = "versions/web_static_{}.tgz".format(date)
        local("tgz -cvzf {} web_static".format(Name))
        return Name
    except ValueError as e:
        return None
