import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def send_mail(Recipients,Subject,Message):
    From="job.control@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = From
    to = ""
    for Recipient in Recipients:
      to += Recipient + ","
    to = to[:len(to)-1]
    msg['To'] = to
    msg['Subject'] = Subject
    msg.preamble = ''
    msgText = MIMEText(Message)
    msg.attach(msgText)
    #change smtp address
    mailserver = smtplib.SMTP("smtp.google.com",587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login(From, "MySecretPassword")
    mailserver.sendmail(From,Recipients,msg.as_string())
    mailserver.quit()
