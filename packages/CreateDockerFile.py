import json
import os
from . import BuildDockerFile


def createDockerFile(**kwargs):
    #os.system('> tmp/Dockerfile')
    print('Argumentos puros: ',kwargs)
    print('Argumento del path: ', kwargs['github_repo'])
    if not kwargs:
        print('No se ingresaron argumentos')
    template_file = f"""
FROM {kwargs["docker_image"]}
WORKDIR /{kwargs['github_repo']}
COPY {kwargs['github_repo']}/ /{kwargs['github_repo']}
RUN pip install -r /{kwargs['github_repo']}/conf.d/requeriments.txt
CMD ["python3", "/{kwargs['github_repo']}/app.py"]"""
    try:
        dir_docker_build = 'docker_deploys/%s'%(kwargs['github_repo'])
        docker_file = dir_docker_build+'/Dockerfile'
        os.mkdir(dir_docker_build)
        dump_file = open(docker_file, 'w')
        dump_file.write(template_file)
        BuildDockerFile.runDockerFile(github_repo=kwargs["github_repo"])
        return json.dumps({'Dockerfile': 'success', 'path': docker_file})
    except:
        cause = 'Dockerfile Already exist'
        return json.dumps({'Dockerfile': 'error', 'cause': cause})
    