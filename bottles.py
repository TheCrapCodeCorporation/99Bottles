import time
import bottlesConfig

def singMeAGoddamnSong(bottles, delay):
    while (bottles != -1):
        if(bottles == 0):
            print ('No More Bottles of beer on the wall, no more bottles of beer. Go to the store get some more 12 bottles of beer on the wall.')
            return
        else:
            print(str(bottles) + ' Bottles Of Beer on the Wall ' + str(bottles) + ' Bottles of beer, take one down, pass it around ' + str(bottles - 1) + ' Bottles Of Beer on the Wall.')
        bottles = bottles - 1
        time.sleep(delay)

def start():
    singMeAGoddamnSong(bottlesConfig.bottles, bottlesConfig.delay)
