import string, os, sys
import sys

class SampleData:
	def __init__(self, dataFile):
		self.date = None
		self.time = None
		self.recvOrder = None
		self.seqCount = None
		self.src = None
		self.dst = None
		self.isSend = None
		self.sType = None
		self.sSuccess = None
		self.dType = None
		self.rsi = None
		self.lqi = None	
		self.data = None

		self.openFile(dataFile)

	def closeFile(self):
		(self.infile)
		
	def openFile(self, dataFile):
		self.infile = open(dataFile)
		self.headline = self.infile.readline()
		#print self.headline.split()
		
	def getData(self):
		del self.data
		try:
			[self.date,self.time,self.recvOrder,self.seqCount,self.src, \
				self.dst,self.isSend,self.sType,self.sSuccess,self.dType, \
				self.rsi,self.lqi,self.data] = self.infile.readline().split()
		except ValueError:
			return None

		#print 'data %s' % self.data
		return self.data


if __name__ == '__main__':
	sdata = SampleData()
	sdata.openFile('sampledata.txt')
	data = sdata.getData()
	while data:
		print data
		data = sdata.getData()
	del sdata

