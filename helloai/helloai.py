import random
import string

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
entered = raw_input()
if checkstring(entered):
	print("Thank you")
else:
	print("You suck")
