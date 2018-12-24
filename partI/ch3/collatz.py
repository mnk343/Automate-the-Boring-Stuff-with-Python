import sys

def collatz(number):

	if number%2 :
		print(3*number+1) 
		return 3*number+1
	else:
		print(number//2)
		return number//2

number = input()

try :
	number = int(number)

except ValueError:
	print("Please enter integer numbers!!")
	sys.exit()
while True:

	number = collatz(number)

	if number == 1:
		break

