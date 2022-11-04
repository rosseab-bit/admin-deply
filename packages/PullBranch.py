import json
import os

def pullBranch(**kwargs):
    pull_branch = f"cd {kwargs['github_repo']} && git checkout {kwargs['branch']} && git pull"
    try:
        docker_apps = f"docker_deploys/{kwargs['github_repo']}"
        cmd_action = f"cd {docker_apps} && echo '{pull_branch}'>pullBranch.sh"
        os.system(cmd_action)
        return {'pull_branch': 'success'}
    except:
        return {'pull_branch':'failed'}