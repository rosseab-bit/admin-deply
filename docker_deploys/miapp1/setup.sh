#!/bin/bash
path_repo=`pwd`
sudo docker build -t miapp1 .
sudo docker run -p 9200:9200 miapp1
