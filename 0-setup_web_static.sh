#!/usr/bin/env bash
# Setups some directories
sudo apt-get update
sudo apt-get install nginx -y
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
echo "Holberton School" | /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
if ! grep 'location /hbnb_static/' /etc/nginx/sites-enabled/default; then
    sudo sed -i '29i\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n' /etc/nginx/sites-enabled/default
fi
sudo service nginx restart
