power = int(input("enter power amount"))
field = int(input("enter the field size"))
seed = int(input("enter seed"))


while(True):
	seed = (seed ** power)%field
	if seed%2==1:
		print(f"0",end="")
	else:
		print(f"1",end="")

	temp = input()
	if temp == "q":
		break