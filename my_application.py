# My Application

#import my_module
#from my_module import *
#from my_module import my_swapper, my_arithmetic
from my_module import my_swapper as swap

arg_one, arg_two = "Prefix", "Suffix"
#arg_one, arg_two = my_module.my_swapper(arg_one, arg_two)
#arg_one, arg_two = my_swapper(arg_one, arg_two)
arg_one, arg_two = swap(arg_one, arg_two)

print("Swapped Arguements:", arg_one, arg_two)

