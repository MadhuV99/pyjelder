# Comparison Operator
print("Comparison Operator".center(50,"-"))
print([1,2,3, "Jack"] == [1,2,3,"Jack"])
print([1,2,3, "Jack"] == [1,2,3,"Jill"])
print([1,2,3, "Jack"] != [1,2,3,"Jill"])

# if Statement
print("if Statement".center(50,"-"))
some_coin = 1
if(some_coin == 1):
    print("you have a penny") 
    print("you have the lowest valued coin") # note the indented lines within the if statement block

some_coin = 5
if some_coin > 1 and some_coin < 10: # logical operators in condition checking
    print("you have a nickel")

# if-else Statement
print("if-else Statement".center(50,"-"))
some_coin = 5
if(some_coin == 1):
    print("you have a penny")
    print("you have the lowest valued coin")
else:
    print("you have a bigger coin")

# if-elif-else Statement
print("if-elif-else Statement".center(50,"-"))
some_coin = 5
if(some_coin == 1):
    print("you have a penny")
    print("you have the lowest valued coin")
elif(some_coin == 5):
    print("you have a nickel")
    print("better than the penny")
else:
    print("you have a bigger coin")

some_coin = 10
if(some_coin == 1):
    print("you have a penny")
    print("you have the lowest valued coin")
elif(some_coin == 5): 
    print("you have a nickel")
    print("better than the penny")
elif(some_coin == 10): 
    print("you have a dime")
    print("These are a dime a dozen...well almost")
else:
    print("you have a bigger coin")

some_coin = 10000
if(some_coin == 1):
    print("you have a penny")
    print("you have hit rock bottom")
elif(some_coin == 5): 
    print("you have a nickel")
    print("better than the lowly penny")
elif(some_coin == 10): 
    print("you have a dime")
    print("These are a dime a dozen...well almost")
elif(some_coin == 25): 
    print("you have a quarter")
    print("Well, you have no quarter for complaint.")
else:
    print("you have a bit coin")
    print("Holy Schmoly, you hit the jackpot!")


# while Loop
print("while Loop".center(50,"-"))
great_america = 150 # miles away
speed = 60 # miles/hour
hours = 0
are_we_there_yet = speed * hours 
while(are_we_there_yet < great_america):
    print("Nope, we've only gone", are_we_there_yet, "miles.") # note the indented lines within the loop
    hours += 1 # the loop increment
    are_we_there_yet = speed * hours 
print("OOPS! we've passed it! We drove ", are_we_there_yet, "miles.")


# for Loop
print("for Loop".center(50,"-"))
magic_words = "OPEN SESAME"
for letter in magic_words:
    print(letter)
    print("knock! knock!")
print("Hey! we are in!")

swindlers_list = ['Billy', "Butch", "Dillinger"]
for swindler in swindlers_list:
    print(swindler)
    print("And another one's gone")

author_hero = {
    "doyle" : "sherlock",
    "rowling" : "harry",
    "christie" : "marple"
}
for author, hero in author_hero.items():
    print(author, hero)


