import time
from math import ceil,sqrt
start_time = time.time()

input = 600851475143
largestFactor = 1
primesSoFar = []

def checkIfPrime(k,primes):
    if k == 2:
        return True
    for i in primes:
        if i > ceil(sqrt(k)):
            break
        if k%i == 0:        
            return False 
    return True

i = 2
process = input

while(True):
    isPrime = checkIfPrime(i,primesSoFar)
    if isPrime:
        primesSoFar.append(i)
        while process%i == 0:
            largestFactor = i
            process = process//i
    i += 1
    if i>process/2:
        if checkIfPrime(process,primesSoFar):
            largestFactor = process
        break

print("The largest prime factor of " + str(input) + " is: " + str(largestFactor))

print("Process finished --- %s seconds ---" % (time.time() - start_time))
