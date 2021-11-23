# Clear the screen
import os
os.system('clear')

# Built-in Functions
print("Built-in Functions".center(50,"-"))
print("print() function".center(50,"-")) # Like in mathematics, the concept of a function is fundamental to understanding Data Science, or any science for that matter.
print("Hello World!") # Print is the name of the built-in python function. built-in, because it is already defined and declared for you to use, call or invoke. 'Hello World' is the arguement you pass to the function. The output is what this function does.  

# Variables
print("Variables".center(50,"-"))
first_name = "John" # a variable is a named container to hold a value, like a customer 'sname or product's cost.
print(first_name) # variable naming conventions are: case sensitive, underscore as word delimiter, all CAPS for constant values that will stay constant throuout the program.  


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
print(min(1, 2, 3)) # the minimum value is output 
print(max(1, 2, 3)) # the maximum value is output 
print(pow(2, 3)) # The first parameter raised to the power of the second paraemter
print(round(10.0 / 3, 4)) # round output to 4 decimal places; ensure at least one of the operands is a float! 

#casting
print("casting".center(50,"-"))
print(int(10 / 3)) # convert the decimal result to integer type
print(float(10 * 3)) # convert the integer result to float(decimal) type
print("30 degrees is " + str(30 * (3.14 / 180)) + " radians") # convert the float expression result to string type and concatenate
print(bin(24)) # convert from decimal to binary. Output binary number begins with 0b.
print(oct(24)) # convert from decimal to octal. Output octal number has a leading 0.
print(hex(24)) # convert from decimal to hexadecimal. Output hexadecimal number begins with 0x.



# List
print("List".center(50,"-"))
first_names = ["John", "Tom", "Rina"]
print(first_names) # prints the entire list
print(len(first_names)) # outputs the number of elements in the list
print(first_names[1]) # outputs the list element in position 1
first_names[1] = "Nick" # Overwrite the element in position 1
print(first_names[len(first_names) - 1]) # outputs the last element n the list
del first_names[1] # deletes the list element at position 1
print(first_names)
duplicate_names = first_names[:] # Returns a copy of the first_names list
print(duplicate_names)
del duplicate_names[:] # Removes all the elements from the list first_names
print(duplicate_names)

# List functions
print("List Functions".center(50,"-"))
first_names = ["John", "Tom", "Rina"]
first_names.append("Mario") # appends an element to the end of the list
print(first_names)
first_names = ["John", "Tom", "Rina", "Tom", "Sam", "Rina", "Tom"]
print(first_names.count('Tom')) # Returns the number of elements with the value 'Tom'
print(first_names.index('Rina')) # Returns the index of the first element with the value 'Rina'
first_names.remove('Rina') # Removes the first element with the value 'Rina'
print(first_names)
first_names.insert(2, 'Kim') # Adds element 'Kim' at the index position 2
print(first_names)
first_names.pop(2) # pops (removes and outputs) the element at index position 2
print(first_names)
more_names = ["Jerry", "Perry", "Terry"]
first_names.extend(more_names) # Adds the elements of list more_names to the end of the list first_names
print(first_names)
duplicate_names = first_names.copy() # Returns a copy of the first_names list
print(duplicate_names)
duplicate_names.clear() # Removes all the elements from the list duplicate_names
first_names.reverse() # Reverses the order of the list first_names
print(first_names)
first_names.sort() # Sorts the list first_names
print(first_names)

# Tuple
print("Tuple".center(50,"-"))
FIRST_NAMES = ("Rina", "Tina", "Gina")
print(FIRST_NAMES)
print(FIRST_NAMES[1]) # Output is Tina, NOT Rina. Indexing starts with 0
LAST_NAMES = ("Green", "Brown", "Gray")
print(LAST_NAMES)
NEW_NAMES = FIRST_NAMES[0:2] + LAST_NAMES[1:1] # Indexing and slicing rules are the same for tuples too.
print(NEW_NAMES)
print(type(LAST_NAMES[1:1])) # sliced tuples are tuples too
print(type(LAST_NAMES[1])) # An indexed tuple element is the corresponding element's data type. 
ALL_NAMES = (FIRST_NAMES[0], LAST_NAMES[0]) \
            + (FIRST_NAMES[1], LAST_NAMES[1]) \
            + (FIRST_NAMES[2], LAST_NAMES[2]) # Note the line continuation character "backslash". 
print(ALL_NAMES) # concatenating corresponding elements from the tuples FIRST_NAMES and LAST_NAMES and assigning the result to the new tuple ALL_NAMES
print(tuple(zip(FIRST_NAMES, LAST_NAMES))) # more slick combination by culling one corresponding item from each of the two tuples. Note use of the TUPLE function to convert the zip object back to a tuple


# Tuple Functions
print("Tuple Functions".center(50,"-"))
full_name = ("Rin", "Tin", "Tin")
print(full_name.count('Tin')) # Returns the number of elements with the value 'Tin'
print(full_name.index('Tin')) # Returns the index of the first element with the value 'Tin'

# Dictionary
print("Dictionary".center(50,"-"))
best_friends = {
    "John" : "Sam",
    "Tom" : "Nick",
    "Rina" : "Gina"
}
print(best_friends) # No guaranteed order
print(best_friends["John"]) 
best_friends["Tom"] = "Tina" # Update the value to 'Tina" of the key element "Tom" in the dictionary best_friends
print(best_friends) # No guaranteed order
del best_friends["Rina"] # Delete the key value pair for the key "Rina" from the dictionary best_friends 
print(best_friends) # No guaranteed order

# Dictionary Functions
print("Dictionary Functions".center(50,"-"))
best_friends = {
    "John" : "Sam",
    "Tom" : "Nick",
    "Rina" : "Gina"
}
print(best_friends) # No guaranteed order
best_friends.update({"Jack" : "Jill"})
print(best_friends) # No guaranteed order







