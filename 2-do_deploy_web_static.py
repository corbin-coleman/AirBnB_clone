#!/usr/bin/python3
from fabric.api import run, put, env


env.hosts = ['54.90.179.127', '52.201.241.151']

def do_deploy(archive_path):
    try:
        directories = archive_path.split('/')
        file_name = directories[-1].split('.')
        new_dir = "/data/web_static/release/" + file_name[0]
        put(archive_path, "/tmp")
        run("mkdir -p %s", new_dir)
        run("tar -xzf /tmp/%s -C %s" % (directories[-1], new_dir))
        run("rm /tmp/%s" % directories[-1])
        run("mv %s/web_static/* %s/" % (new_dir, new_dir))
        run("rm -rf %s/web_static" % new_dir)
        run("rm -rf /data/web_static/current")
        run("ln -s %s/ /data/web_static/current" % new_dir)
        return True
    except Exception:
        return False
