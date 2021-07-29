import time, paramiko, schedule

# This script schedule for disable and enable for specific SSID. Variables can be edited. 

username = "admin"
password = "123456"
host = "192.168.91.145"
enable = "08:00"
disable = "19:00"
wlan_ID = "1"

def job_1(): # Enable SSID

	wlc_session = paramiko.SSHClient()
	wlc_session.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	try:
		
		wlc_session.connect(hostname=host, port='22', username='null', password='null')
		wlc_ssh_class = wlc_session.invoke_shell()
		time.sleep(2)
		
		print('trying to login'+' '+str(host))
		
		wlc_ssh_class.send(username+'\n')
		time.sleep(1)
		wlc_ssh_class.send(password+'\n')
		time.sleep(1)
		
		print('login successful'+' '+str(host))		
	except:
		print('unable to connect'+' '+str(host))
		
	wlc_ssh_class.send('config wlan enable'+' '+wlan_ID+'\n')
	time.sleep(1)
	print('Job_SSID_Enable done')

def job_2(): # Disable SSID

	wlc_session = paramiko.SSHClient()
	wlc_session.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	try:
		
		wlc_session.connect(hostname=host, port='22', username='null', password='null')
		wlc_ssh_class = wlc_session.invoke_shell()
		time.sleep(2)
		
		print('trying to login'+' '+str(host))
		
		wlc_ssh_class.send(username+'\n')
		time.sleep(1)
		wlc_ssh_class.send(password+'\n')
		time.sleep(1)
		
		print('login successful'+' '+str(host))
		
	except:
		print('unable to connect'+' '+str(host))
		
	wlc_ssh_class.send('config wlan disable'+' '+wlan_ID+'\n')
	time.sleep(1)
	print('Job_SSID_Disable done')

schedule.every().monday.at(enable).do(job_1)
schedule.every().friday.at(disable).do(job_2)

while True:
    schedule.run_pending()
    time.sleep(5) 
    print("checking")
