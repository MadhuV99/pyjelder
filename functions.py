# Clear the screen
import os
os.system('clear')

# User Defined Functions
print("User Defined Functions".center(50,"-"))

def return_nothing_function(first_parameter, second_parameter): # function declaration defining the parameters
    print("Message from the User Defined Function, return_nothing_function:") # note the indented lines within the function block
    print("You passed in %s first, and %s next." % (first_parameter, second_parameter)) 
    return # optional last line of function if not returning any value 
    a_variable = "In no man's land. Control will never flow to these lines after return statement above"
    print("Not gonna happen: ", a_variable)

return_nothing_function("first_argument", "second_argument") # calling or invoking the function return_nothing_function, passing 2 arguement

def return_something_function(first_number, second_number, unused_parameter):
    print("Message from the User Defined Function return_something_function:")
    print("You passed in %f first, and %f next." % (first_number, second_number)) 
    result = first_number + second_number
    return result # last line of function returning result

returned_thing = return_something_function(4, 5, 6) 
print("Thing returned by return_something_function: ", returned_thing)

a_num = 23.45
b_num = 45.67
returned_thing = return_something_function(a_num, b_num, 'unused argument') 
print("Thing returned by return_something_function: ", returned_thing)
