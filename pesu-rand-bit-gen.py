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

def expand(data):
	seed = 1
	temp_data = []
	for temp in data:
		seed = ((seed+temp) ** 2)%97
		temp_data.extend(str(seed))

	return temp_data

data = expand(converter(input("data")))