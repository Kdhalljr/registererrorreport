from urllib2 import urlopen
import file_functions
from time import strftime


def getStoreList():
	return ["xxxxxx", "xxxxxx", "xxxxxx", "xxxxxx", "xxxxxx", "xxxxxx", "xxxxxx", "xxxxxx", "xxxxxx", "xxxxxx", "xxxxxx", "xxxxxx", "xxxxxx", "xxxxxx", "xxxxxx", "xxxxxx", "xxxxxx", "xxxxxx", "xxxxxx", "xxxxxx", "xxxxxx", "xxxxxx", "xxxxxx", "xxxxxx", "xxxxxx", "xxxxxx", "xxxxxx", "xxxxxx", "xxxxxx", "xxxxxx", "xxxxxx", "xxxxxx", "xxxxxx", "xxxxxx", "xxxxxx", "xxxxxx", "xxxxxx", "xxxxxx"]


def getDMList():
	return ["xxxxxx", "xxxxxx", "xxxxxx", "xxxxxx", "xxxxxx", "xxxxxx", "xxxxxx", "xxxxxx", "xxxxxx", "xxxxxx", "xxxxxx", "xxxxxx"]


def copyResponses():
	while True:
			try:
				urlopen(file_functions.getResponseSSWebAppUrl()).read()
				break
			except Exception, e:
				error_log_file.write(strftime("%c") + " Responses Copy Error " + store + " " + str(e))
	
	
def createAndSendStoreSummaries():
	for store in getStoreList():
		while True:
			try:
				urlopen(file_functions.getStoreSSWebAppUrl(store)).read()	
				break
			except Exception, e:
				error_log_file.write(strftime("%c") + " Mgr Error " + store + " " + str(e))
				break


def createAndSendDMSummaries():
	for dm in getDMList():
			while True:
				try:
					urlopen(file_functions.getDMSSWebAppUrl(dm)).read()
					break
				except Exception, e:
					error_log_file.write(strftime("%c") + " DM Error " + dm + " " + str(e))
					break
					

def createAndSendAllStoresSummary():
	while True:
			try:
				urlopen(file_functions.getCROSSWebAppUrl()).read()
				break
			except Exception, e:
				error_log_file.write(strftime("%c") + " CRO Error" + " " + str(e))
				break


if __name__ == "__main__":
	error_log_file = open('error_log.txt', 'a')

	# Copy responses to respective spreadsheets
	copyResponses()
	
	# Append summaries of store spreadsheets and send email to managers
	createAndSendStoreSummaries()
	
	# Create summaries for DMs and send email
	createAndSendDMSummaries()
	
	# Create Summaries for All Stores Spreadsheet and send email
	createAndSendAllStoresSummary()
	
	error_log_file.close()
