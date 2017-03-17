#!/usr/bin/python3
from fabric.api import run, put, env


env.hosts = ['54.90.179.127', '52.201.241.151']


def do_deploy(archive_path):
    try:
        directories = archive_path.split('/')
        file_name = directories[-1].split('.')
        new_dir = "/data/web_static/release/" + file_name[0]
        put(archive_path, "/tmp")
        run("sudo mkdir -p %s", new_dir)
        run("sudo tar -xzf /tmp/%s -C %s" % (directories[-1], new_dir))
        run("sudo rm /tmp/%s" % directories[-1])
        run("sudo mv %s/web_static/* %s/" % (new_dir, new_dir))
        run("sudo rm -rf %s/web_static" % new_dir)
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s %s/ /data/web_static/current" % new_dir)
        return True
    except Exception:
        return False
