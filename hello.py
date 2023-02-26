import os
import time
import datetime









def ring_ring ():
    for it0 in range(3):
        for it1 in range(5):
            os.system("echo -e '\a'")
            time.sleep(0.16)
        time.sleep(1)





f = open("alarms.txt")
list = f.readlines()
f.close()

for it in list:
    print(it)

now = datetime.datetime.now()
currentTime = ("%s/%s/%s %s:%s:%s" % (now.month, now.day, now.year, now.hour, now.minute, now.second))
print("Now:: " + currentTime)

its = 0
while True:
    #update contents
    if (its % 60) == 0:
        f = open("alarms.txt")
        list = f.readlines()
        print (len(list))

    now = datetime.datetime.now()
    currentTimeA = ("%s/%s/%s %s:%s:%s\n" % (now.month, now.day, now.year, now.hour, now.minute, now.second))
    currentTimeB = ("%s:%s:%s\n" % (now.hour, now.minute, now.second))

    print(currentTimeA)
    print(currentTimeB)

    for it in list:
        if (it == currentTimeA) or (it == currentTimeB):
            print("!!ALARM!!")
            ring_ring()
    time.sleep(0.5)
    its += 1
