string1 = str(input("enter a string"))

print(string1)

#spliting data
string1 = string1.split()


string1.sort()


reduceddata = {} 

for temp in string1:
	if temp in reduceddata.keys():
		#reduction
		reduceddata[temp]+=1
	else:
		#maps
		reduceddata.update({temp : 1})

print(reduceddata)
primelist=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]

reduceddata_key_pro={}

#prime divisible counter
for temp in reduceddata.keys():
	for temp2 in primelist:
		if int(temp)% (int(temp2))==0:
			if temp in reduceddata_key_pro.keys():
				#reduction
				reduceddata_key_pro[temp2]+=1
			else:
				#maps
				reduceddata_key_pro.update({temp2 : 1})





print(reduceddata_key_pro)