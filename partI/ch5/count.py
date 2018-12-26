print("enter a message : ")
message = input()

count = {}

for char in message : 
	count.setdefault(char,0)
	count[char] += 1

for i in count:
	print("Occurence of {0} is : {1}".format(i , count[i] ))