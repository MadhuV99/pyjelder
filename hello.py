# Clear the screen
import os
os.system('clear')

print("print() function".center(50,"-"))
print("Hello World!")

# Variables
print("Variables".center(50,"-"))
first_name = "John" # variable naming convention; case sensitive
print(first_name)

# String Properties
print("String Properties".center(50,"-"))
print(len("Edgar Rice Burroughs"))
print("Edgar Rice Burroughs"[11])
print("Edgar Rice Burroughs"[6:10]) # from index position 6, extract  upto, but NOT including the 10th position
print("Edgar Rice Burroughs"[6:]) # from index position 6, extract the rest of string 
print("Edgar Rice Burroughs"[:10]) # from the beginning, extract upto, but NOT including the 10th position
print("Quotes within quotes: " + "Happy X'mas to 'em all!") # when quote marks are part of the string
print("Escaping the string: " + 'Happy X\'mas') # \ is an escape character that can be used within a string to print out the quote chracter
print("Tab separated names:" + "John\tTom\tRina")
print("Weekdays on new lines: " + "Sun\nMon\nTue\nThu\nFri\nSat")

# String Functions
print("String Functions".center(50,"-"))
print("In UPPER case: " + "Happy X'mas. Howdy folks!".upper())
print("In lower case: " + "Happy X'mas. Howdy folks!".lower())
print("In ReVeRsE case: " + "Happy X'mas. Howdy folks!".swapcase())
print("Capitalized: " + "Happy X'mas. Howdy folks!".capitalize()) # First letter of the string is capitalized
print("In Camel case: " + "Happy X'mas. Howdy folks!".title()) # First letter of every word is capitalized
print("Split on spaces: ", "Happy X'mas. Howdy folks!".split(' '))

# math functions
print("math functions".center(50,"-"))
print(abs(-25.67)) # The absolute value of the parameter
print(cmp(2, 3)) # if equal, returns 0. if first numeber is less than second parameter, outputs a -ve value, else outputs +ve value.
print(pow(2, 3)) # The first parameter raised to the power of the second paraemter
print(round(10.0 / 3, 4)) # round output to 4 decimal places; ensure at least one of the operands is a float! 


#casting
print("casting".center(50,"-"))
print(int(10 / 3)) # convert the decimal result to integer type
print(float(10 / 5)) # convert the integer result to float(decimal) type
print("30 degrees is " + str(30 * (3.14 / 180)) + " radians") # convert the float expression result to string type and concatenate
print(bin(24)) # convert from decimal to binary. Output binary number begins with 0b.
print(oct(24)) # convert from decimal to octal. Output octal number has a leading 0.
print(hex(24)) # convert from decimal to hexadecimal. Output hexadecimal number begins with 0x.



# List
print("List".center(50,"-"))
first_names = ["John", "Tom", "Rina"]
print(first_names)
print(first_names[1])

# Tuple
print("Tuple".center(50,"-"))
FIRST_NAMES = ("Sam", "Nick", "Gina")
print(FIRST_NAMES)
print(FIRST_NAMES[1])

# Dictionary
print("Dictionary".center(50,"-"))
best_friends = {
    "John" : "Sam",
    "Tom" : "Nick",
    "Rina" : "Gina"
}
print(best_friends) # No guaranteed order
print(best_friends["Tom"]) 



