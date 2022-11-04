#!/bin/bash
git clone https://github.com/usergit/miapp5.git
path_repo=`pwd`
sudo docker build -t miapp5 .
sudo docker run -p 9200:9200 miapp5
