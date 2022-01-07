import time
start_time = time.time()

def checkIfPalindrome(newNum):
    if str(newNum) == str(newNum)[::-1]:
        return True
    else:
        return False

largestPalindrome = 0

for num1 in range(100,999):
    for num2 in range(100,999):
                newNum = num1 * num2
                if checkIfPalindrome(newNum) and newNum > largestPalindrome:
                    largestPalindrome = newNum

print("The largest palindrome is: " + str(largestPalindrome))

print("Process finished --- %s seconds ---" % (time.time() - start_time))