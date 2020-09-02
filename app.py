import json
import volumesize
import mail
import os
import crt
import backup
import docker
from datetime import date

with open('settings.json') as config_file:
    settings = json.load(config_file)

def check_volume():
    volumeSizeSettings = settings['volumeSize']

    for container in volumeSizeSettings:
        if volumesize.getVolumeSize(container["name"],container["directory"]) > container["treshold"]:
            Recipients = container["recipients"].split(',')
            Subject = '(Production) Volume Size Warning!('+container["name"]+')'
            Message = 'Volume Size of '+container["name"]+' Workload is Now Bigger Than '+str(container["treshold"])+ 'Gi.'
            mail.send_mail(Recipients,Subject,Message)
def check_cert():
    cert_settings = settings["certificates"]
    for cert in cert_settings:
        crt.check_cert(cert["address"],cert["directory"])
def check_expire():
    cert_settings = settings["certificates"]
    for cert in cert_settings:
        crt.check_expire(cert["name"],cert["expireDate"],cert["tresholdDay"],cert["recipients"])
def take_backup():
    backup_settings = settings["backup"]
    client = docker.from_env()
    for setting in backup_settings:
        for container in client.containers.list():
            if container.name.find("POD") == -1 and container.name.find(setting["name"]) != -1 :
                name = container.name
                break
        if not os.path.exists(setting["target"]):
                os.makedirs(setting["target"])
        targetDir = setting["target"] + str(date.today())
        backup.copy_from_container(name,setting["source"],targetDir)
        command = "find "+setting["target"]+"* -type d -ctime +"+str(setting["tresholdDay"])+" -exec rm -rf {} \;"
        os.system(command)
