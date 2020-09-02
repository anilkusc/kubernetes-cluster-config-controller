import os
from datetime import date
import docker
import tarfile

def copy_from_container(name,source,target):
    client = docker.from_env()
    container = client.containers.get(name)
    f = open(os.path.join(os.getcwd(),target+".tar"),"wb")
    bits, stat = container.get_archive(source)
    for chunk in bits:
        f.write(chunk)
    f.close()
    
