b=[]

def comma(b):

	str=""
	for i in range(len(b)-1):
		str+=b[i]
		str+=", "

	str+="and "
	str+=b[len(b)-1]
	return str

while True:
	print("Enter nothing to stop giving input to list")

	a=input()

	if a=="":
		break
	
	b.append(a)

print(comma(b))
