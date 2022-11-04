import json
import os

def runDockerFile(**kwargs):
    repo_name = kwargs['github_repo']
    # https://github.com/usergit/repo.git
    repo_url = f"https://github.com/usergit/{repo_name}.git"
    cmd_clone_repo = f"git clone {repo_url}"
    up_docker = f"""#!/bin/bash
{cmd_clone_repo}
path_repo=`pwd`
sudo docker build -t {kwargs['github_repo']} .
sudo docker run -p 9200:9200 {kwargs['github_repo']}"""
    cmd_updocker = f"cd docker_deploys/{kwargs['github_repo']} && echo '{up_docker}' > setup.sh"
    os.system(cmd_updocker)