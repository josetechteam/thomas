al = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
stringToEncrypt = input("Please enter a message to encrypt: ")
stringToEncrypt = stringToEncrypt.upper()
shiftAmount = int(input("Please enter a whole number from 1-25 to be your key."))
encryptedString = ""
for currentCharacter in stringToEncrypt:
	position = al.find(currentCharacter)
	newPosition = position + shiftAmount
	encryptedString = encryptedString + al[newPosition]
print("Your Encrypted message is", encryptedString)

