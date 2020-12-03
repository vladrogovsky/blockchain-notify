import urllib, json
import win32api
import time
from datetime import datetime
import winsound
duration = 3000  # millisecond
freq = 440  # Hz
print "Enter Transaction TxHash:",
transiction = raw_input()
confirmations = 0
lastError = ""
while True:
	try:
		if (lastError != ""):
			print("Trying to fix things up....")
			lastError = ""
		transictionURL = "https://blockchain.info/rawtx/"+str(transiction)
		transictionResponse = urllib.urlopen(transictionURL)
		CurTransictionData = json.loads(transictionResponse.read())
		lastBlockResponce = urllib.urlopen("http://blockchain.info/latestblock")
		lastBlockData = json.loads(lastBlockResponce.read())
		curConfirm = int(lastBlockData["height"]) - int(CurTransictionData["block_height"]) + 1
		if (int(confirmations) != int(curConfirm)):
			confirmations = int(curConfirm)
			the_time = datetime.now().time()
			the_time = the_time.replace(second=0, microsecond=0)
			winsound.Beep(freq, duration)
			win32api.MessageBox(0, 'Total number of confirmations: '+str(confirmations), 'New confirmations!')
			print(">>Time - "+str(the_time)+"<<\n\r")
			print("New confirm! Total number of confirmations: "+str(confirmations)+"\n\r")
		time.sleep(60)
	except Exception as e:
		lastError = e
		print(e)
		print("Try again...")
		continue
	except:
		print("KEY!")
		break