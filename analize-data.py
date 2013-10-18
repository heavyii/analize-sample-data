import string, os, sys
import sys
from data import SampleData

class HandleData:
	def __init__(self, datafile):
		self.sdata = SampleData(datafile)

	def getItem(self):
			# data format: [2bytes moteID][2bytes counter][3bytes ignore]
			# data: 04-F2-A2-69-63-CD
			data = self.sdata.getData()
			if not data:
				return (None, None)

			array = data.split('-')
			moteID = int(array[0]+array[1], 16)
			counter = int(array[2]+array[3], 16)
			return (moteID, counter)

	def process(self):
		#get first counter
		errCount = 0
		(moteID, pcCounter) = self.getItem()
		while True:
			(moteID, counter) = self.getItem()
			if not moteID:
				break

			pcCounter = pcCounter + 1
			if pcCounter > 0xffff:
				pcCounter = 0
			if pcCounter != counter:
				print 'LOST:  %d --> %d' % (pcCounter, counter)
				pcCounter = counter
				errCount = errCount + 1

		del self.sdata
		if errCount > 0:
			print 'DONE: lost packet count = %d' % errCount
		else:
			print 'DONE: no packet lost'


if __name__ == '__main__':
	print 'INFO: analize %s' % sys.argv[1]
	dataHandler = HandleData(sys.argv[1])
	dataHandler.process()

	
