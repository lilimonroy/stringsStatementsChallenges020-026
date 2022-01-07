#Pig Latin takes the first consonant of a word, moves it to the end of the word and adds on an “ay”. If a word begins with a vowel you just add
# “way” to the end. For example, pig becomes igpay, banana becomes ananabay, and aadvark becomes aadvarkway. Create a program that will ask the
#user to enter a word and change it into Pig Latin. Make sure the new word is displayed in lower case.

word = input("Enter a word: ")

lenghWord = len(word)
word.lower()
firstLetter = word[0]

if firstLetter == "a" and "e" and "i" and "o" and "u":
    print(word+"ay")
else:
    print(word[1:lenghWord+1]+word[0]+"ay")