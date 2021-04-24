
# A short program that accepts a string inputted by a user and encrypts/decrypts by shifting each character in the
# string backwards/forwards three indexes.

nums = range(1,26) #list that will track index position for the 26 letters in the alphabet

alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


# Function that immediately appends spaces and capitalizes any lowercase letters. It then checks to see the index of
# that letter in the alphabet. That numerical index is then decreased by three in order to perform the shift.
# The corresponding char is then appended to the empty crypt list throughout each iteration in order to return the
# encrypted list equivalent.
def encrypt(str):
    crypt = []
    for char in str:
        if(char.isspace()):
            crypt.append(value)
        else:
            if(char.islower()):
                char = char.capitalize()
            idx = alph.index(char)
            idx = idx - 3
            value = alph[idx]
            crypt.append(value)
    return(crypt)

# Function that immediately appends spaces and increases the numerical index of the encrypted list equivalent of the
# initially provided string by three. It also checks to make sure that a string including the first three letters of the
# alphabet doesn't exceed the length. # The corresponding char is then appended to the empty crypt list throughout each
# iteration in order to return the the original string input.
def decrypt(arr):
    crypt = []
    for char in arr:
        if(char.isspace()):
            crypt.append(value)
        else:
            idx = alph.index(char)
            idx = idx + 3
            if(idx >= (len(nums))):
                idx = (idx - len(nums)) - 1
            value = alph[idx]
            crypt.append(value)
    return(crypt)

word = input("Choose a word to encrypt: ")
print('')

output = encrypt(word)
print(output)
print('')

output = decrypt(output)
print(output)

