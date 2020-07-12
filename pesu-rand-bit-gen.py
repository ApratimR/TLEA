#char array (size = 95)
char_array = list("!#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\^_]`abcdefghijklmnopqrstuvwxyz{|}~ "+'"')


#converts character list to integer values
def converter(parameter1):
	local_ar1 = []
	try:
		for temp1 in parameter1:
			local_ar1.append(char_array.index(temp1))
	except:
		print("enter valid string default set to 1")
		local_ar1=1
	return local_ar1



data = converter(input("data"))


for temp in data:
	seed = ((seed+temp) ** 2)%95
	if seed%2==1:
		print(f"0",end="")
	else:
		print(f"1",end="")

	temp = input()
	if temp == "q":
		break
	