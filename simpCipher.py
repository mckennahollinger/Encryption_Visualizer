# A short program that accepts a string inputted by a user and encrypts/decrypts it according to the numerical index
# associated with each respective letter in the alphabet.
#TODO have functions break to prevent runtime error and reprompt user for string if space is char


nums = range(1,26) #list that will track index position for the 26 letters in the alphabet

alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


# Function that capitalizes any lowercase character and checks to see the index of that letter in the alphabet. That
# numerical index is then incremented by 1 as the length of a list has one more value than an index. That value is then
# appended to the empty crypt list throughout each iteration in order to return the encrypted list equivalent.
def encrypt(str):
    crypt = []
    for char in str:
        if(char.islower()):
            char = char.capitalize()
        idx = alph.index(char)
        idx = idx + 1
        crypt.append(idx)
    return(crypt)


# Function that decreases the numerical index of the encrypted list equivalent of the initially provided string as
# an index has one less value than the length of a list. That iteration's numerical index of the alphabet is then
# accessed and the corresponding letter is appended to crypt in order to return the original string input.
def decrypt(arr):
    crypt = []
    for num in arr:
        num = num - 1
        char = alph[num]
        crypt.append(char)
    return(crypt)


word = input("Choose a word to encrypt: ")
print('')

print(alph)
print('')
print(word)
print('')

output = encrypt(word)
print(output)
print('')

output = decrypt(output)
print(output)

