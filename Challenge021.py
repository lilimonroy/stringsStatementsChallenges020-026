#----------* CHALLENGE 21 *----------
#Ask the user to enter their first name and then ask them to enter their surname. Join them together with a space between
#and display the name and the length of whole name.

name = input("Enter your fist name: ")
surname= input("Enter your surname: ")

completeName = name + surname

totalLenght = len(completeName)

print(name+" "+surname+"\nThe total lenght of your name without space is",totalLenght)