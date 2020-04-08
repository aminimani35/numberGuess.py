import random


print('###############   Bazie Hadse Adad    ################')


def random_number():
	value = random.randrange(0,100)
	return value

loop = True
counter = 0 
adad = random_number()
print (adad)
while loop:
	
	
	hads = int(input('adad ra hads bezanid : >> '))
	counter +=1
	if (hads>adad):
		print('Kamtaresh kon')
	elif(hads<adad):
		print('Bishtaresh kon')
	elif(hads == adad) :
		print(f'Yeeeees Hamineee VA To {counter} hads zadi ta be natije residi :)')
		play_again = input('mikhay bazam bazi koni??? y/n : >> ')
		if (play_again == 'y'):
			counter = 0
			adad = random_number()
		else:
			print (' Bye Bye :)')
			loop = False



