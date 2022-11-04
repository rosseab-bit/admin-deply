#!/bin/bash
git clone https://github.com/usergit/miapp4.git
path_repo=`pwd`
sudo docker build -t miapp4 .
sudo docker run -p 9200:9200 miapp4
