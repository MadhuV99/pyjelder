
# Function Definitions
def my_greetings(person, occasion):
    message = "Hi %s, Wish you a Very, Very Happy %s" % (person, occasion)
    print(message)
    return

def my_arithmetic(expression):
    result = eval(expression)
    return result

def my_swapper(param_one, param_two):
    temp = param_one
    param_one = param_two
    param_two = temp
    return (param_one, param_two) # function returning multiple result items as a tuple

#Test the Functions:
def test_functions():
    print("calling my_greetings()")
    my_greetings("Tim", "B'day")

    print("calling my_arithmetic()")
    the_sum = my_arithmetic("2 + 3")
    print(the_sum)

    arg_one = "Before"
    arg_two = "After"
    arg_one, arg_two = my_swapper(arg_one, arg_two)
    print("Swapped Arguements:", arg_one, arg_two)


if __name__ == "__main__":
    test_functions()

