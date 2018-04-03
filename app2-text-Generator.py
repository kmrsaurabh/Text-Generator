# This takes the combination of 3 letters and generates a Random string
import random
import string

vowels = 'aeiou'
consonants = 'bcdfghjklmnopqrstuvwxyz'
letters = string.ascii_lowercase

letter_input_1 = input("What letter do you wnat, Enter 'v' for the Vowel, Enter 'c' for the Consonants, Enter 'l' for other letter :")
letter_input_2 = input("What letter do you wnat, Enter 'v' for the Vowel, Enter 'c' for the Consonants, Enter 'l' for other letter :")
letter_input_3 = input("What letter do you wnat, Enter 'v' for the Vowel, Enter 'c' for the Consonants, Enter 'l' for other letter :")

print(letter_input_1 + letter_input_2 + letter_input_3)

def generator():

# For the First letter
    if letter_input_1 == 'v':
        letter1 = random.choice(vowels)
    elif letter_input_1 =='c':
        letter1 = random.choice(consonants)
    elif letter_input_1 == 'l':
        letter1 = random.choice(letters)
    else:
        letter1 = letter_input_1 # if user enters different letter than 'v', 'c', 'l'
        #  then that input will also be considered as the input i.e it will be included in the Output

# For the 2nd letter
    if letter_input_2 == 'v':
        letter2 = random.choice(vowels)
    elif letter_input_2 =='c':
        letter2 = random.choice(consonants)
    elif letter_input_2 == 'l':
        letter2 = random.choice(letters)
    else:
        letter2 = letter_input_2

# For the 3rd letter
    if letter_input_3 == 'v':
        letter3 = random.choice(vowels)
    elif letter_input_3 =='c':
        letter3 = random.choice(consonants)
    elif letter_input_3 == 'l':
        letter3 = random.choice(letters)
    else:
        letter3 = letter_input_3
    name = letter1 + letter2 + letter3
    return name

# To generate the list of strings then we can use the loop
for i in range(10):
    print(generator())
