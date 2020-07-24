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

def padder(parameter1):
	if len(parameter1) == 0:
		print("no data provided deafult set to spaces")
		parameter1.extend([" "for x in range(95)])
	else:
		if len(parameter1)%95 != 0:
			parameter1.extend([" " for x in range((95-len(parameter1)%95))])
	return parameter1




def expand(data):
	#TODO gotta make better PRNG for IV\
	#using modified LCG algo
	adder = 289800465
	adder2 = 279880967
	seed2 = adder2
	seed = adder
	temp_data = []
	for temp in data:
		seed = ((seed * temp) + (670141274+(temp*seed2)))%95
		seed2 = ((seed2 * temp) + (153419145+(temp*seed2)))%95
		temp_data.append(str((seed+seed2)%95))


	
	return temp_data

data = expand(converter(padder(list(input("data is")))))

print(", ".join(data))