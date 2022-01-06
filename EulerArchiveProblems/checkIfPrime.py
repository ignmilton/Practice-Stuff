def checkIfPrime(k):
     if k == 2:
         return True
     for i in range(2,ceil(sqrt(k))+1):
         if k%i == 0:
             return False
     return True
