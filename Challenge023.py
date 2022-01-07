#----------* CHALLENGE 23 *----------
#Ask the user to type in the first line of a nursery rhyme and display the length of the string.
#Ask for a starting number and an ending number and then display just that section of the text
#(remember Python starts counting from 0 and not 1).

song = input("Enter the first line of some nursery rhyme: ")
start = int(input("Enter the start number of display: "))
end = int(input("Enter the last number of display: ")) 

fragment = song[start-1:end] #I assumed that people don't start counting since 0. That's why I add +1
lenghtFragment = len(fragment)
print(fragment+" The lenght is",lenghtFragment)