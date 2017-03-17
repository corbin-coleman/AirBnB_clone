#!/usr/bin/python3
from fabric.api import local
from datetime import datetime


def do_pack():
    local('mkdir -p versions')
    time_created = datetime.now().strftime("%Y%m%d%H%M%S")
    local('tar -cvzf "versions/web_static_%s.tgz" ./web_static' % time_created)
