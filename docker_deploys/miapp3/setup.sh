#!/bin/bash
git clone https://github.com/usergit/miapp3.git
path_repo=`pwd`
sudo docker build -t miapp3 .
sudo docker run -p 9200:9200 miapp3
