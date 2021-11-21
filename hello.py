# Clear the screen
import os
os.system('clear')

print(".".center(50,"-"))
print("Hello World!")

# Variables
print(".".center(50,"-"))
first_name = "John" # variable naming convention; case sensitive
print(first_name)

print(".".center(50,"-"))
# String Proerties
print(len("Edgar Rice Burroughs"))
print("Edgar Rice Burroughs"[11])
print("Edgar Rice Burroughs"[6:9]) # from index position 6, extract  upto 10th position
print("Edgar Rice Burroughs"[6:]) # from index position 6, extract the rest of string 
print("Edgar Rice Burroughs"[:10]) # from beginning, extract upto 10th position
print("Quotes within quotes: " + "Happy X'mas to 'em all!") # when a quote mark is part of the string
print("Escaping the string: " + 'Happy X\'mas') # \ is an escape character that can be used within a string to print out the quote chracter
print("Tab separated names:" + "John\tTom\tRina")
print("Weekdays on new lines: " + "Sun\nMon\nTue\nThu\nFri\nSat")
# String Functions
print("In UPPER case: " + "Happy X'mas. Howdy folks!".upper())
print("In lower case: " + "Happy X'mas. Howdy folks!".lower())
print("In ReVeRsE case: " + "Happy X'mas. Howdy folks!".swapcase())
print("Capitalized: " + "Happy X'mas. Howdy folks!".capitalize()) # First letter of the string is capitalized
print("In Camel case: " + "Happy X'mas. Howdy folks!".title()) # First letter of every word is capitalized
print("Split on spaces: ", "Happy X'mas. Howdy folks!".split(' '))

# List
print(".".center(50,"-"))
first_names = ["John", "Tom", "Rina"]
print(first_names)
print(first_names[1])

# Tuple
print(".".center(50,"-"))
FIRST_NAMES = ("Sam", "Nick", "Gina")
print(FIRST_NAMES)
print(FIRST_NAMES[1])

# Dictionary
print(".".center(50,"-"))
best_friends = {
    "John" : "Sam",
    "Tom" : "Nick",
    "Rina" : "Gina"
}
print(best_friends) # No guaranteed order
print(best_friends["Tom"]) 