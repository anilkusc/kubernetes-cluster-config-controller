import os
import datetime
import mail
from datetime import date

def pull(directory):
    command="cd "+directory+" && git pull"
    os.system(command)

def clone(directory,address):
    command="cd "+directory+" && git clone "+address+" ."
    os.system(command)

def check_cert(address,directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    if not os.path.exists(directory+"/.git"):    
        clone(directory,address)
    pull(directory)

def check_expire(name,expiredate,treshold,recipients):
    expire_date =  datetime.datetime.strptime(expiredate, '%d.%m.%Y')
    tresholdDate = expire_date + datetime.timedelta(days=-10)
    today = datetime.datetime.strptime(date.today().strftime("%d.%m.%Y"), '%d.%m.%Y')
    if tresholdDate < today:
        Recipients = recipients.split(',')
        Subject = '(Production) Certificate Expire Date is Coming!('+name+')'
        Message = 'This certificate('+name+') expire date('+str(expire_date)+') is incoming.Please renew it.'
        mail.send_mail(Recipients,Subject,Message)
