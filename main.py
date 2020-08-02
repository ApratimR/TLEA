import numpy as np
import os

#char array (size = 95)
char_array = list("!#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\^_]`abcdefghijklmnopqrstuvwxyz{|}~ "+'"')

display_text_header ="""
████████╗██╗        ███████╗    █████╗    
╚══██╔══╝██║        ██╔════╝   ██╔══██╗   
   ██║   ██║        █████╗     ███████║   
   ██║   ██║        ██╔══╝     ██╔══██║   
   ██║██╗███████╗██╗███████╗██╗██║  ██║██╗
   ╚═╝╚═╝╚══════╝╚═╝╚══════╝╚═╝╚═╝  ╚═╝╚═╝
   (Totally.Logical.Encryption.Algorithm)
"""

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
	key_ref_array = np.loadtxt("set2.csv",dtype=np.int8,delimiter=",")
	temp_key = [1 for x in range(95)]
	#the rounds of 16 are done here
	for _ in range(64):
		for temp1 in parameter1:
			temp_key = (temp_key+key_ref_array[(temp1+-81)%95])%95
			temp_key = np.roll(temp_key,temp1-25)
			temp_key = (temp_key+temp1-43)%95
			temp_key = np.roll(temp_key,temp1-32)

			temp_key = (temp_key+key_ref_array[(temp1+75)%95])%95
			temp_key = np.roll(temp_key,temp1+94)
			temp_key = (temp_key+temp1+45)%95
			temp_key = np.roll(temp_key,temp1-47)
	
			temp_key = (temp_key+key_ref_array[(temp1+15)%95])%95
			temp_key = np.roll(temp_key,temp1-17)
			temp_key = (temp_key+temp1+15)%95
	return temp_key


def key_expansion1(parameter1):
	key_ref_array = np.loadtxt("set2.csv",dtype=np.int8,delimiter=",")
	temp_key = [1 for x in range(95)]
	#the rounds of 16 are done here
	for _ in range(64):
		for temp1 in parameter1:
			temp_key = (temp_key+key_ref_array[(temp1+66)%95])%95
			temp_key = np.roll(temp_key,temp1-55)
			temp_key = (temp_key+temp1-46)%95
			temp_key = np.roll(temp_key,temp1-87)

			temp_key = (temp_key+key_ref_array[(temp1+74)%95])%95
			temp_key = np.roll(temp_key,temp1-53)
			temp_key = (temp_key+temp1-16)%95
			temp_key = np.roll(temp_key,temp1+71)
	
			temp_key = (temp_key+key_ref_array[(temp1+64)%95])%95
			temp_key = np.roll(temp_key,temp1+62)
			temp_key = (temp_key+temp1+51)%95
	return temp_key


def initial_vector_generator(parameter1):
	iv_ref_array = np.loadtxt("iv.csv",dtype=np.int8,delimiter=",")
	temp_key = [1 for x in range(95)]
	#the rounds of 16 are done here
	for _ in range(2):
		for temp1 in parameter1:
			temp_key = (temp_key+iv_ref_array[(temp1-76)%95])%95
			temp_key = np.roll(temp_key,temp1-91)
			temp_key = (temp_key+temp1-38)%95
			temp_key = np.roll(temp_key,temp1-22)

			temp_key = (temp_key+iv_ref_array[(temp1-5)%95])%95
			temp_key = np.roll(temp_key,temp1-17)
			temp_key = (temp_key+temp1+62)%95
			temp_key = np.roll(temp_key,temp1+11)
	
			temp_key = (temp_key+iv_ref_array[(temp1-49)%95])%95
			temp_key = np.roll(temp_key,temp1+7)
			temp_key = (temp_key+temp1-19)%95
			temp_key = np.roll(temp_key,temp1+20)
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
	"""rawdara """
	temp = main_call(rawdata,rawkey,1)
	return temp

def do_decryption(rawdata , rawkey):
	temp = main_call(rawdata,rawkey,2)
	return temp

def do_encryption_chain(rawdata ,rawkey):
	temp = main_call(rawdata,rawkey,3)
	return temp

def do_decryption_chain(rawdata ,rawkey):
	temp = main_call(rawdata,rawkey,4)
	return temp

def main_call(rawdata , rawkey ,option):
	sahdow_encryption_matrix = np.loadtxt("set1.csv",dtype=np.int8,delimiter=",")
	data = converter(padder(list(rawdata)))
	key = converter(list(rawkey))
	key1,key2 = key_expansion(key),key_expansion1(key)
	
	if option == 1 :data = encrypt(sahdow_encryption_matrix,key1,key2,data);return(convert_back(data))
	elif option == 2 :data = decrypt(sahdow_encryption_matrix,key1,key2,data);return(convert_back(data))
	elif option == 3 :iv = initial_vector_generator(key);data = encrypt_chain(sahdow_encryption_matrix,key1,key2,iv,data);return(convert_back(data))
	elif option == 4 :iv = initial_vector_generator(key);data = decrypt_chain(sahdow_encryption_matrix,key1,key2,iv,data);return(convert_back(data))


#encryption function 
#TODO need to introduce chaining below with no parallelization
#or any initial vector
def encrypt_chain(round_encryption_matrix,key1,key2,initial_vector,data):
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



def decrypt_chain(round_dencryption_matrix,key1,key2,initial_vector,data):
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

#display of header
def main():
	print(display_text_header)
	main2()

#the main function
def main2():
	rawtext = str(input("\nenter the data you want to encrypt/decrypt :"))
	password = str(input("enter the password :"))
	ModeOfOperation = int(input(f"""
enter the mode of operation
1.encryption without chaining
2.decryption without chaining

3.encryption with chaining
4.decryption with chaining

ENTER ANY OTHER KEY TO EXIT PROGRAM

PS:Output is pasted system clipboard
=>"""))

	if ModeOfOperation in (1,2,3,4):
		output = main_call(rawdata=rawtext,rawkey=password,option = ModeOfOperation)
		print(output)

		#os command to past to clip board
		# command = 'echo | set /p nul=' + output.strip() + '| clip'
		# os.system(command)
		# main2()
	else:
		exit()

#main calll
if __name__ == "__main__":
	main()