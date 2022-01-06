"""
import time
start_time = time.time()

fibonacciList = []
fibonacciList.append(0)
fibonacciList.append(1)

k = 0
n = 2

while k <= 4_000_000:
    k = fibonacciList[n-1] + fibonacciList[n-2]
    fibonacciList.append(k)
    n = n + 1
   # print(k)
fibonacciList.pop()

sum = 0

for q in range(0,len(fibonacciList)):
    if fibonacciList[q]%2 == 0:
        sum = sum + fibonacciList[q]
    else:
        sum = sum + 0

print("The sum is: " + str(sum)) 

print("Process finished --- %s seconds ---" % (time.time() - start_time))
"""

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