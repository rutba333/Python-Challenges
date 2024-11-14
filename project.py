import random

# A function to shuffle all the characters of a string
def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

# Main program starts here
uppercaseLetter1 = chr(random.randint(65, 90)) # Generate a random uppercase letter (based on ASCII code)
uppercaseLetter2 = chr(random.randint(65, 90)) # Generate another random uppercase letter

# Generate more characters here
# ...

# Generate password using all the characters, in random order
password = uppercaseLetter1 + uppercaseLetter2 # + ... (add more characters here)
password = shuffle(password)

# Output
print(password)
