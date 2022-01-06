import time
start_time = time.time()

pprev = 0
prev = 1
evenSum = 0

while(True):
    k = pprev + prev
    pprev = prev
    prev = k
    if k > 4_000_000:
        break
    elif k%2 == 0:
        evenSum += k

print("The sum is: " + str(evenSum)) 

print("Process finished --- %s seconds ---" % (time.time() - start_time))