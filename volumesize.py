import docker
def getVolumeSize(containerName,directory):
    client = docker.from_env()
    for container in client.containers.list():
      if container.name.find("POD") == -1 and container.name.find(containerName) != -1 :
        targetContainerId = container.id
        break
    container = client.containers.get(targetContainerId)
    command = "du -hs "+directory+" --apparent-size --block-size=1G | awk {'print $1'}"
    size = container.exec_run(["sh","-c",command], stderr=True, stdout=True)
    volumeSize = size.output.decode("utf-8")
    return int(volumeSize)
