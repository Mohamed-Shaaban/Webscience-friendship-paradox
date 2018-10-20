import re
import math
import statistics


def paresingxml():
	count = 0
	with open('xml.txt', 'r') as searchfile:
		with open('freindscount.txt','w') as wf:
			for line in searchfile:
				if '"friend_count"' in line:
					count = count +1
					counter = str(int(count))
					wf.write(line)
			#wf.write("The total friends number is " +counter)


def extractingnumber():
	with open('freindscount.txt','r') as fc ,open('numbers count.txt ','w') as nc:
			for line in fc:
				second="".join(re.findall(r'\d+',line)) +"\n"
				nc.write(second)


def calculateMean():
	lis=[]
	with open ('numbers count.txt ','r') as nc:
		total = sum(int(x)
		for line in nc
		for x in line.split())
		#print ("Total = ",total)
	mean = total /154 
	print ("Mean = ",mean)
	return mean



def calculateSD(m):
	ls=[]
	i= 0
	with open ('numbers count.txt ','r') as nc:
		for line in nc:
			subNo = int(line) - m
			SqureSubno= subNo *subNo
			ls.append(SqureSubno)
		SqTotal = sum(ls)
		Mean= SqTotal/ m
		STD= math.sqrt(SqTotal)
		print ("STD = ",STD) 


 



def calculateMedian():
	ls=[]
	with open ('numbers count.txt ','r') as nc:
		for line in nc:
			ls.append(line.strip('\n'+''))
		ls =list(map(int, ls))
		#print (ls)
		Median = statistics.median(ls)
		print ("Median = ",Median)



#calculateMean()
paresingxml()
extractingnumber()
mean = calculateMean()
calculateSD(mean)
calculateMedian()