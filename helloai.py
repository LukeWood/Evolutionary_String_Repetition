import random
import string
import time
from datetime import datetime
import sys
def hamming_distance(a,b):
	if(len(a)!=len(b)):
		return None
	return sum(a0 != b0 for a0,b0 in zip(a,b))

def randomLetter():
	return random.choice(string.printable)

def randomString(stringlength):
	toret = ""
	for i in range(0,stringlength):
		toret+=randomLetter()
	return toret

def checkstring(tocheck):
	for letter in tocheck:
		if not letter in string.printable:
			return False
	return True
		
print("\nWelcome to helloai")
print("This AI program will learn how to print the string you input")
print("Please enter your string:")
random.seed(datetime.now())
target = input()
if not checkstring(target):
	print("please enter a valid string")
	sys.exit()

fullList =list();

print("Would you like to pause after each generation to see the program work over time?(Y/N)")
sleep = input()
while sleep not in ("Y","N","n","y"):
	print("please enter a valid value")
	sleep = input()
if sleep in ("Y","y"):
	sleep = True
else:
	sleep = False
targetlen = len(target)
machineguess=randomString(targetlen)
generation = 1;
generationlength =100
mutationrate = 5
currentfit = hamming_distance(machineguess,target)

while not machineguess == target:
	print("Generation {gen}: ".format(gen=generation)+machineguess)
	fullList.append([generation,currentfit]);
	if(sleep):
		time.sleep(1)
	generation+=1
	generationlength = int(float(generationlength) * 1.2)
	for i in range(0, generationlength):
		tempguess = list(machineguess)
		for z in range(0,mutationrate): 
			if bool(random.getrandbits(1)):
				index = random.randint(0,targetlen-1)
				tempguess[index] = randomLetter()
		tempguess = "".join(tempguess)	
		tempfit = hamming_distance(tempguess,target)
		if tempfit < currentfit:
			machineguess = tempguess
			currentfit = tempfit
print("Generation {gen}: ".format(gen=generation)+machineguess)
print("The program has successfully written back your string.")
with open("matlabvisualization.m","w+") as f:
	f.write("x = [");
	for i in fullList:
		f.write("{fitness};".format(fitness=i[1]));
	f.write("];\nplot(x)\nxlabel('Generations');\nylabel('Accuracy');\ntitle('Evolutionary String Repetition');");
