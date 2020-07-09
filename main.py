import numpy as np

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

#this pads the data
def padder(parameter1):
	if len(parameter1) == 0:
		print("no data provided deafult set to spaces")
		parameter1.extend([" "for x in range(95)])
	else:
		if len(parameter1)%95 != 0:
			parameter1.extend([" " for x in range((95-len(parameter1)%95))])
	return parameter1

#converts integer value list to string
def convert_back(parameter1):
	output = str()

	try:
		for temp1 in parameter1:
			output+= char_array[temp1]
	except:
		print("error encountered while indexing")
	return output




#compress/expands the input array to 18 nonagenquinnary size (95-bit)
def key_expansion(parameter1):
	key_ref_array = np.loadtxt("ref_array.csv",dtype=np.int8,delimiter=",")
	temp_key = [0 for x in range(95)]
	#the rounds of 16 are done here
	for _ in range(64):
		for temp1 in parameter1:
			temp_key = np.roll(temp_key,-65)
			temp_key = (temp_key+key_ref_array[temp1])%95
			temp_key = np.roll(temp_key,46)
			temp_key = (temp_key+key_ref_array[(temp1+43)%95])%95
			temp_key = np.roll(temp_key,24)
			temp_key = (temp_key+key_ref_array[(temp1+92)%95])%95
	return temp_key


def key_expansion1(parameter1):
	key_ref_array = np.loadtxt("ref_array.csv",dtype=np.int8,delimiter=",")
	temp_key = [0 for x in range(95)]
	#the rounds of 16 are done here
	for _ in range(64):
		for temp1 in parameter1:
			temp_key = np.roll(temp_key,-16)
			temp_key = (temp_key*key_ref_array[temp1])%95
			temp_key = np.roll(temp_key,-43)
			temp_key = (temp_key*key_ref_array[(temp1+30)%95])%95
			temp_key = np.roll(temp_key,63)
			temp_key = (temp_key+key_ref_array[(temp1+32)%95])%95
	return temp_key

#encryption function
def encrypt(round_encryption_matrix,key1,key2,data):
	data_temp = []
	for temp1 in range(95):
		round_encryption_matrix[temp1] = np.roll(round_encryption_matrix[temp1],key1[temp1])

	#this is the main encryption loop over data
	for temp in range(int(len(data)/95)):
		temp_array = data[(temp*95):(temp*95)+95]

		#the encryption process
		#the rounds of 16 are done here
		for _ in range(16):
			for temp1 in range(95):
				temp_array[temp1] = round_encryption_matrix[key2[temp1]][temp_array[temp1]]

		#join the processed data to a temp to send it back
		data_temp.extend(temp_array)

	return data_temp




#decryption function
def decrypt(round_dencryption_matrix,key1,key2,data):
	data_temp = []
	for temp1 in range(95):
		round_dencryption_matrix[temp1] = np.roll(round_dencryption_matrix[temp1],key1[temp1])

	#this is the main encryption loop over data
	for temp in range(int(len(data)/95)):
		temp_array = data[(temp*95):(temp*95)+95]

		#the rounds of 16 are done here
		for _ in range(16):
			for temp1 in range(95):
				temp_array[temp1] = round_dencryption_matrix[key2[temp1]].tolist().index(temp_array[temp1])

		data_temp.extend(temp_array)

	return data_temp


def do_encryption(rawdata , rawkey):
	temp = main_call(rawdata,rawkey,1)
	return temp

def do_decryption(rawdata , rawkey):
	temp = main_call(rawdata,rawkey,2)
	return temp


#this is some messed up stuff
def main_call(rawdata , rawkey ,option):
	sahdow_encryption_matrix = np.loadtxt("main_array.csv",dtype=np.int8,delimiter=",")
	data = converter(padder(list(rawdata)))
	key = converter(list(rawkey))
	key1,key2 = key_expansion(key),key_expansion1(key)
	
	if option == 1 :data = encrypt(sahdow_encryption_matrix,key1,key2,data);return(convert_back(data))
	elif option == 2 :data = decrypt(sahdow_encryption_matrix,key1,key2,data);return(convert_back(data))
	elif option == 3 :data = encrypt_chain(sahdow_encryption_matrix,key1,key2,data);return(convert_back(data))
	elif option == 4 :data = decrypt_chain(sahdow_encryption_matrix,key1,key2,data);return(convert_back(data))


#encryption function 
#TODO need to introduce chaining below with no parallelization
#or any initial vector
def encrypt_chain(round_encryption_matrix,key1,key2,data):
	data_temp = []
	for temp1 in range(95):
		round_encryption_matrix[temp1] = np.roll(round_encryption_matrix[temp1],key1[temp1])

	#this is the main encryption loop over data
	for temp in range(int(len(data)/95)):
		temp_array = data[(temp*95):(temp*95)+95]

		#the encryption process
		#the rounds of 16 are done here
		for _ in range(16):
			for temp1 in range(95):
				temp_array[temp1] = round_encryption_matrix[key2[temp1]][temp_array[temp1]]

		#join the processed data to a temp to send it back
		data_temp.extend(temp_array)

	return data_temp



def decrypt_chain(round_dencryption_matrix,key1,key2,data):
	data_temp = []
	for temp1 in range(95):
		round_dencryption_matrix[temp1] = np.roll(round_dencryption_matrix[temp1],key1[temp1])

	#this is the main encryption loop over data
	for temp in range(int(len(data)/95)):
		temp_array = data[(temp*95):(temp*95)+95]

		#the rounds of 16 are done here
		for _ in range(16):
			for temp1 in range(95):
				temp_array[temp1] = round_dencryption_matrix[key2[temp1]].tolist().index(temp_array[temp1])

		data_temp.extend(temp_array)

	return data_temp