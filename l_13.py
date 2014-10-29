#!/usr/bin/python

import pylab

def loadFile():
	inFile = open('julytemps','r')
	l = []
	h = []


	for line in inFile:
	
		fields = line.split(' ')
	
		if len(fields) != 3 or 'Boston' == fields[0] or 'Day' == fields[0]:
			continue
		else:
			h.append(int(fields[1]))
			l.append(int(fields[2]))

	diffTemps = [h[x]-l[x] for x in range(len(h))]
	
	pylab.figure(1)	
	pylab.plot(range(1,32), diffTemps)
	
	pylab.title('Day by Day Ranges in Temperature in Boston in July 2012')
	pylab.xlabel('Days')
	pylab.ylabel('Temperature Ranges')
	pylab.show()

if __name__ == "__main__":	
	loadFile()
	print 'tadaaa'
