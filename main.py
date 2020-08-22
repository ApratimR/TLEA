import numpy as np
import base64

#char array (size = 64)
char_array = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")

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
	local_ar1 = list()

	if len(parameter1)==0:
		raise Exception("Paramter provided is empty")
	elif isinstance(parameter1,str)==False:
		if isinstance(parameter1,list)==False:
			raise Exception("improper data type detected")
	
	#TODO need work on converting it to base 64
	parameter1 = parameter1.encode()
	parameter1 = base64.b64encode(parameter1)
	parameter1 = parameter1.decode()
	parameter1 = list(parameter1)
	for temp1 in parameter1:
		if temp1 == "=":
			break
		else:
			local_ar1.append(char_array.index(temp1))
	return local_ar1

#this pads the data
def padder(parameter1):
	#FIXME : need to work on making a empty *string* creation operation
	parameter1 = str(parameter1)
	if len(parameter1) == 0:
		print("no data provided deafult set to spaces")
		parameter1+=" "
	else:
		if len(parameter1)%64 != 0:
			parameter1.extend([" " for x in range((64-len(parameter1)%64))])
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

def array_rotation(target,reference):
	"""rotates 2d array(target) in slice With the value in the list(reference)"""

	for temp1 in range(len(target)):
		target[temp1]=np.roll(target[temp1],reference[temp1])

	return target


#compress/expands the input array to 18 nonagenquinnary size (64-bit)
def key_expansion(parameter1):
	key_ref_array = np.loadtxt("set2.csv",dtype=np.int8,delimiter=",")
	temp_key = np.ones((64),dtype=np.uint8)
	#the rounds of 16 are done here
	for _ in range(64):
		for temp1 in parameter1:
			temp_key = (temp_key+key_ref_array[(temp1+-81)%64])%64
			temp_key = np.roll(temp_key,temp1-25)
			temp_key = (temp_key+temp1-43)%64
			temp_key = np.roll(temp_key,temp1-32)

			temp_key = (temp_key+key_ref_array[(temp1+75)%64])%64
			temp_key = np.roll(temp_key,temp1+94)
			temp_key = (temp_key+temp1+45)%64
			temp_key = np.roll(temp_key,temp1-47)

			temp_key = (temp_key+key_ref_array[(temp1+15)%64])%64
			temp_key = np.roll(temp_key,temp1-17)
			temp_key = (temp_key+temp1+15)%64
	return temp_key


def key_expansion1(parameter1):
	key_ref_array = np.loadtxt("set2.csv",dtype=np.int8,delimiter=",")
	temp_key = np.ones((64),dtype=np.uint8)
	#the rounds of 16 are done here
	for _ in range(64):
		for temp1 in parameter1:
			temp_key = (temp_key+key_ref_array[(temp1+66)%64])%64
			temp_key = np.roll(temp_key,temp1-55)
			temp_key = (temp_key+temp1-46)%64
			temp_key = np.roll(temp_key,temp1-87)

			temp_key = (temp_key+key_ref_array[(temp1+74)%64])%64
			temp_key = np.roll(temp_key,temp1-53)
			temp_key = (temp_key+temp1-16)%64
			temp_key = np.roll(temp_key,temp1+71)

			temp_key = (temp_key+key_ref_array[(temp1+64)%64])%64
			temp_key = np.roll(temp_key,temp1+62)
			temp_key = (temp_key+temp1+51)%64
	return temp_key


def initial_vector_generator(parameter1):
	iv_ref_array = np.loadtxt("set3.csv",dtype=np.int8,delimiter=",")
	temp_key = np.ones((64),dtype=np.uint8)
	#the rounds of 16 are done here
	for _ in range(2):
		for temp1 in parameter1:
			temp_key = (temp_key+iv_ref_array[(temp1-76)%64])%64
			temp_key = np.roll(temp_key,temp1-91)
			temp_key = (temp_key+temp1-38)%64
			temp_key = np.roll(temp_key,temp1-22)

			temp_key = (temp_key+iv_ref_array[(temp1-5)%64])%64
			temp_key = np.roll(temp_key,temp1-17)
			temp_key = (temp_key+temp1+62)%64
			temp_key = np.roll(temp_key,temp1+11)

			temp_key = (temp_key+iv_ref_array[(temp1-49)%64])%64
			temp_key = np.roll(temp_key,temp1+7)
			temp_key = (temp_key+temp1-19)%64
			temp_key = np.roll(temp_key,temp1+20)
	return temp_key


#encryption function
def encrypt(round_encryption_matrix,key1,key2,data):
	data_temp = []
	round_encryption_matrix=array_rotation(round_encryption_matrix,key1)

	#this is the main encryption loop over data
	for temp in range(int(len(data)/64)):
		temp_array = data[(temp*64):(temp*64)+64]

		#the encryption process
		#the rounds of 16 are done here
		for _ in range(16):
			for temp1 in range(64):
				temp_array[temp1] = round_encryption_matrix[key2[temp1]][temp_array[temp1]]

		#join the processed data to a temp to send it back
		data_temp.extend(temp_array)

	return data_temp




#decryption function
def decrypt(round_dencryption_matrix,key1,key2,data):
	data_temp = []
	round_dencryption_matrix=array_rotation(round_dencryption_matrix,key1)

	#this is the main encryption loop over data
	for temp in range(int(len(data)/64)):
		temp_array = data[(temp*64):(temp*64)+64]

		#the rounds of 16 are done here
		for _ in range(16):
			for temp1 in range(64):
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
	data = converter(rawdata)
	key = converter(rawkey)
	key1,key2 = key_expansion(key),key_expansion1(key)
	
	if option == 1 :data = encrypt(sahdow_encryption_matrix,key1,key2,data);return(convert_back(data))
	elif option == 2 :data = decrypt(sahdow_encryption_matrix,key1,key2,data);return(convert_back(data))
	elif option == 3 :iv = initial_vector_generator(key);data = encrypt_chain(sahdow_encryption_matrix,key1,key2,iv,data);return(convert_back(data))
	elif option == 4 :iv = initial_vector_generator(key);data = decrypt_chain(sahdow_encryption_matrix,key1,key2,iv,data);return(convert_back(data))


#encryption function 
#TODO need to introduce chaining below with no parallelization
#FIXME to start working
#per round IV generation for offsetting of the @parameter=round_encryption_matrix
#or any initial vector
def encrypt_chain(round_encryption_matrix,key1,key2,initial_vector,data):
	data_temp = []

	round_encryption_matrix=array_rotation(round_encryption_matrix,key1)

	#this is the main encryption loop over data
	for temp in range(int(len(data)/64)):


		round_encryption_matrix=array_rotation(round_encryption_matrix,initial_vector)


		temp_array = data[(temp*64):(temp*64)+64]

		#the encryption process
		#the rounds of 16 are done here
		for _ in range(16):
			for temp1 in range(64):
				temp_array[temp1] = round_encryption_matrix[key2[temp1]][temp_array[temp1]]

		#join the processed data to a temp to send it back
		data_temp.extend(temp_array)

	return data_temp



def decrypt_chain(round_dencryption_matrix,key1,key2,initial_vector,data):
	data_temp = []
	round_dencryption_matrix=array_rotation(round_dencryption_matrix,key1)

	#this is the main encryption loop over data
	for temp in range(int(len(data)/64)):
		temp_array = data[(temp*64):(temp*64)+64]

		#the rounds of 16 are done here
		for _ in range(16):
			for temp1 in range(64):
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