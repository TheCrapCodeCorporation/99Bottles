import time


bottles = 99
while (bottles != -1):
	print str(bottles) + ' Bottles Of Beer on the Wall ' + str(bottles) + ' Bottles of beer, take one down, pass it around ' + str(bottles - 1) + ' Bottles Of Beer on the Wall.'
	bottles = bottles - 1
	time.sleep(6)
