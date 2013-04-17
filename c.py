import string
import math

#Problem C: Fair and Square
def isPalindrome(num):
	if num == "":
		return True
	if num[0] != num[len(num)-1]:
		return False
	return isPalindrome(num[1:len(num)-1])

#def isSquareofPalindrome(num):
#	root = math.sqrt(num)
#	if not isPalindrome(root):
#		return False
#	return isPalindrome(num)	

#def isSquare(num):
#	root = math.floor(math.sqrt(num))
#	if root**2 == num:
#		return True
#	return False	

def sumDigits(num):
	sum = 0
	while num > 0:
		sum += num % 10
		num = int(num/10)
	return sum

#Initialize up to MAX before input
MAX = 10**24
sPList = []
maxRoot = int(math.floor(math.sqrt(MAX)))
i = 1
#Using while because range() has a low limit
while i < maxRoot:
	if isPalindrome(str(i)): 
		num = i**2
		if isPalindrome(str(num)):
			sPList.append(num)
			print(str(num))
			print("Sum of digits = " + str(sumDigits(num)))
			print("Sqrt = " + str(i) + '\n')
	i += 1
print("List built.")

#Main implementation
inFile = open("input.txt", 'r')
outFile = open("output.txt", 'w')

T = int(inFile.readline())

for i in range(T):
	line = inFile.readline().partition(' ')
	A = int(line[0])
	B = int(line[2])
	count = 0
	for x in sPList:
		if x >= A and x <= B:
			count += 1
	outFile.write("Case #" + str(i+1) + ": " + str(count) + '\n')

#Just print for the hell of it
for x in sPList:
	print x 
