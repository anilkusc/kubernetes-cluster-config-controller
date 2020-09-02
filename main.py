
import app
import schedule
import time
import threading
import os

def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()
#run once every start
app.check_volume()
app.check_expire()
app.check_cert()
app.take_backup()

if os.getenv('DEBUG') == 'true':
    schedule.every(60).seconds.do(run_threaded, app.check_volume)
    schedule.every(60).seconds.do(run_threaded, app.check_expire)
    schedule.every(60).seconds.do(run_threaded, app.check_cert)
    schedule.every(60).seconds.do(run_threaded, app.take_backup)    
else:
    schedule.every().wednesday.at("13:30").do(run_threaded, app.check_volume)
    schedule.every().day.at("10:30").do(run_threaded, app.check_expire)
    schedule.every(60).seconds.do(run_threaded, app.check_cert)
    schedule.every().day.at("01:00").do(run_threaded, app.take_backup)

while True:
    schedule.run_pending()
    time.sleep(1)
