#----------* CHALLENGE 22 *----------
#Ask the user to enter their first name and surname in lower case. Change the case to title case and join them together.
#Display the finished result.

firstName = input("Enter your first name:")
surname = input("Enter your surname:")

firstName.lower()
surname.lower()
name = firstName+" "+surname
name = name.title()

print(name)